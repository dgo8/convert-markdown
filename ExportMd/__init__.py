import os
import warnings
from pathlib import Path
from .core.converter import MarkdownConverter
from .exporters.html import HTMLExporter
from .exporters.pdf import PDFExporter
from .exporters.docx import DOCXExporter
from .exporters.pptx import PPTXExporter


class ExportMd:
    def __init__(self):
        self.converter = MarkdownConverter()
        self._exporters = {
            'pdf': PDFExporter(),
            'docx': DOCXExporter(),
            'pptx': PPTXExporter()
        }
        
        # Get package static directory
        self.static_dir = Path(__file__).parent / 'static'
        self.template_dir = Path(__file__).parent / 'templates'

    @staticmethod
    def to(markdown: str, format: str = 'pdf', output_file: str = None, 
               style: str = 'style', custom_css: str = None) -> bytes:
        """
        Convert markdown to the specified format
        
        Args:
            markdown (str): Input markdown text
            format (str): Output format ('html', 'pdf', 'docx', or 'pptx')
            output_file (str): Optional output file path
            style (str): CSS style to use ('style', 'style1', 'style2', 'style3' or 'custom')
            custom_css (str): Custom CSS string to use when style='custom'
            
        Returns:
            bytes: Converted document as bytes (or None if output_file is specified)
        """
        exporters = {
            'html': HTMLExporter(),
            'pdf': PDFExporter(),
            'docx': DOCXExporter(),
            'pptx': PPTXExporter()
        }
        if format not in exporters:
            raise ValueError(f"Unsupported format: {format}")
            
        # Convert markdown to HTML with specified style
        converter = MarkdownConverter()
        html = converter.convert_to_html(markdown, style=style, custom_css=custom_css)
        
        # Convert to requested format
        exporter = exporters[format]
        output = exporter.export(html)
        
        # Save to file if specified
        if output_file:
            mode = 'wb' if format != 'html' else 'w'
            with open(output_file, mode) as f:
                if format == 'html':
                    f.write(html)
                else:
                    f.write(output)
            return None  # Return None when saving to file
                
        return output

# Create a module-level instance
_instance = ExportMd()

# Expose the convert method at module level
to = _instance.to 