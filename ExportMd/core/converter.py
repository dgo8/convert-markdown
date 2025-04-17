import os
import json
from pathlib import Path
from bs4 import BeautifulSoup
import markdown
import plotly.graph_objects as go
import io
import base64
import re
import sys
from contextlib import redirect_stdout, redirect_stderr, contextmanager
import matplotlib
matplotlib.use('Agg')  # Set matplotlib backend to non-interactive
import matplotlib.pyplot as plt
import plotly.io as pio
import plotly.express as px
from ..static.styles import style, style1, style2, style3  # Import styles
pio.renderers.default = None  # Disable plotly's default browser opening

class MarkdownConverter:
    def __init__(self):
        # Define styles mapping
        self.styles = {
            'style': style,
            'style1': style1,
            'style2': style2,
            'style3': style3
        }
        
        # Base template
        self.base_template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="icon" href="data:,">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
</head>
<body>
    <div class="content">
        {{content}}
    </div>
</body>
</html>"""
            
    def convert_to_html(self, markdown_text: str, style: str = 'style1', custom_css: str = None) -> str:
        """Convert markdown with Python code blocks to HTML"""
        try:
            # Extract and convert code blocks
            code_blocks = self._extract_code_blocks(markdown_text)
            html_with_code = self._replace_code_blocks(markdown_text, code_blocks)
            
            # Convert remaining markdown to HTML
            html = markdown.markdown(html_with_code, extensions=['tables'])
            
            # Get CSS content
            if style == 'custom' and custom_css:
                css = custom_css
            else:
                if style not in self.styles:
                    print(f"Warning: Style {style} not found, using default style")
                    style = 'style'
                css = self.styles[style]
                    
            # Insert into base template with CSS
            template = self.base_template.replace('{{content}}', html)
            template = template.replace('</head>', f'<style>{css}</style></head>')
            
            return template
            
        except Exception as e:
            print(f"Error converting markdown to HTML: {e}")
            raise

    def _extract_code_blocks(self, markdown_text: str) -> list:
        """Extract Python code blocks"""
        code_regex = r':::python\s*([\s\S]*?)\s*:::'
        code_regex2 = (r'```python\s*([\s\S]*?)\s*```')
        code_blocks = []
        
        for match in re.finditer(code_regex, markdown_text):
            code_blocks.append({
                'code': match.group(1),
                'match': match.group(0)
            })
        for match in re.finditer(code_regex2, markdown_text):
            code_blocks.append({
                'code': match.group(1),
                'match': match.group(0)
            })
                
        return code_blocks

    @contextmanager
    def _suppress_show(self):
        """Context manager to suppress plt.show() and capture the figure"""
        original_show = plt.show
        try:
            plt.show = lambda: None  # Replace show with no-op
            yield
        finally:
            plt.show = original_show  # Restore original show

    def _capture_output(self, code: str) -> str:
        """Execute code and capture all output"""
        stdout = io.StringIO()
        stderr = io.StringIO()
        return_value = None
        
        try:
            # Create namespace for execution with common imports
            namespace = {
                '__name__': '__main__',
                'plt': plt,
                'matplotlib': matplotlib,
                'np': __import__('numpy'),
                'pd': __import__('pandas'),
                'go': go,
                'px': px,
                'sns': __import__('seaborn'),
                'Figure': go.Figure
            }
            
            # Redirect stdout and stderr and suppress plt.show()
            with redirect_stdout(stdout), redirect_stderr(stderr), self._suppress_show():
                exec(code, namespace)
                
                # Handle different types of outputs
                if 'fig' in namespace:
                    fig = namespace['fig']
                    try:
                        # Check the type of figure
                        fig_type = type(fig).__module__.split('.')[0]  # Get the root module name
                        
                        if fig_type == 'plotly':
                            # Handle Plotly figure
                            img_bytes = pio.to_image(
                                fig,
                                format="png",
                                scale=4.0,
                                engine="kaleido"
                            )
                            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
                            return_value = f'<img src="data:image/png;base64,{img_base64}" class="chart-container" />'
                        else:
                            # Handle matplotlib/seaborn figure
                            buf = io.BytesIO()
                            fig.savefig(buf, format='png', dpi=300, bbox_inches='tight', facecolor='white')
                            buf.seek(0)
                            img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                            return_value = f'<img src="data:image/png;base64,{img_base64}" class="chart-container" />'
                            plt.close('all')  # Clean up
                            
                    except Exception as e:
                        print(f"Error converting figure: {e}")
                        return_value = f"<pre class='code-error'>Error converting figure: {str(e)}</pre>"
                
                # Check for matplotlib/seaborn figures even if no fig variable
                elif hasattr(plt, 'get_fignums') and plt.get_fignums():
                    # Handle matplotlib/seaborn figure
                    fig = plt.gcf()
                    buf = io.BytesIO()
                    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight', facecolor='white')
                    buf.seek(0)
                    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                    return_value = f'<img src="data:image/png;base64,{img_base64}" class="chart-container" />'
                    plt.close('all')  # Clean up
                
            stdout_content = stdout.getvalue()
            stderr_content = stderr.getvalue()
            
            # Combine outputs
            output = []
            if stdout_content:
                output.append(f"<pre class='code-output'>{stdout_content}</pre>")
            if stderr_content and 'FigureCanvasAgg is non-interactive' not in stderr_content:
                output.append(f"<pre class='code-error'>{stderr_content}</pre>")
            if return_value:
                output.append(return_value)
                
            return '\n'.join(output) if output else ''
            
        except Exception as e:
            return f"<pre class='code-error'>Error executing code: {str(e)}</pre>"
        finally:
            stdout.close()
            stderr.close()

    def _replace_code_blocks(self, markdown_text: str, code_blocks: list) -> str:
        """Replace Python code blocks with their output"""
        html = markdown_text
        
        # Sort code blocks in reverse order to handle nested blocks correctly
        # and prevent mismatched replacements
        code_blocks.sort(key=lambda x: markdown_text.index(x['match']), reverse=True)
        
        for block in code_blocks:
            try:
                output = self._capture_output(block['code'])
                if output:
                    # Add a div wrapper to keep code and output together
                    wrapped_output = f'<div class="code-block-output">{output}</div>'
                    html = html.replace(block['match'], wrapped_output)
                else:
                    html = html.replace(block['match'], 
                                      '<div class="code-block-output"><pre class="code-output">No output generated</pre></div>')
            except Exception as e:
                html = html.replace(
                    block['match'],
                    f'<div class="code-block-output"><pre class="code-error">Error executing code: {str(e)}</pre></div>'
                )
        return html 