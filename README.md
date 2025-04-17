# Export Markdown with executed Code Blocks 

Python package that converts markdown text with executed code blocks to various formats. 

## Create visual reports with charts from LLM outputs.
![new](https://github.com/user-attachments/assets/e8841ff6-3340-453b-9f5a-4b247dc53acc)



## Features

- **Code Execution**: Execute Python code blocks directly in your markdown
- **Multiple Export Formats**: Markdown to PDF, Markdown to DOCX, Markdown to PPTX, and Markdown to HTML
- **Data Visualization**: Support for Matplotlib, Plotly, and Seaborn
- **Custom Styling**: Choose from built-in styles or define your own CSS
- **Professional Output**: Generate publication-ready documents

## Installation

```bash
pip install -r requirements.txt
pip install ExportMd
```

## Quick Start

```python
import ExportMd

markdown_content = """
# Analysis Report

## Data Visualization

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title("Sine Wave")
plt.show()
```"""

# Method 1: Get bytes and save manually
output = ExportMd.to(
    markdown=markdown_content,
    style='style1', # default: 'style', 'style1', 'style2', 'style3', 'custom'
    format='pdf'    # default: 'pdf', 'docx', 'pptx', 'html'
)
with open('output.pdf', 'wb') as f:
    f.write(output)

# Method 2: Direct to file (returns None)
ExportMd.to(
    markdown=markdown_content,
    format='pdf',
    output_file='output.pdf'  # File is saved directly
)
```

Parameters:
- `markdown`: Input markdown text
- `format`: Output format ('pdf', 'docx', 'pptx', 'html')
- `output_file`: Optional path to save the output (if specified, returns None)
- `style`: CSS style to use (default: 'style', 'style1', 'style2', 'style3', 'custom')
- `custom_css`: Custom CSS string when style='custom'

Returns:
- `bytes`: Converted document as bytes (or None if output_file is specified)

## Code Block Support

Use standard markdown code blocks with Python:

```python
# Print statements
print("Hello, World!")

# Matplotlib
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 2, 3])
plt.show()

# Plotly
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

# Seaborn
import seaborn as sns
tips = sns.load_dataset('tips')
sns.boxplot(data=tips, x='day', y='total_bill')
plt.show()
```

## Styling Options

### Built-in Styles

Choose from three built-in styles:
- `style1`: Corporate finance theme
- `style2`: Modern business theme
- `style3`: Clean documentation theme

```python
ExportMd.to(
    markdown=content,
    format='pdf',
    style='style2'
)
```

### Custom CSS

Apply your own styling:

```python
custom_css = """
body {
    font-family: Arial, sans-serif;
    max-width: 900px;
    margin: 0 auto;
}
"""

ExportMd.to(
    markdown=content,
    format='pdf',
    style='custom',
    custom_css=custom_css
)
```

## Pre-imported Libraries

The following libraries are available in Python code blocks:
- numpy (as np)
- pandas (as pd)
- matplotlib.pyplot (as plt)
- plotly.graph_objects (as go)
- plotly.express (as px)
- seaborn (as sns)

## Examples

See the [examples](examples/) directory for more detailed examples, including:
- Basic print statements
- Matplotlib visualizations
- Plotly interactive charts
- Seaborn statistical plots
- Complex data analysis reports

## License

MIT License - see LICENSE file for details.
