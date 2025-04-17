import pytest
import exportmd
import os

SAMPLE_MARKDOWN = """
# Sample Report

This comprehensive report analyzes current market trends and future projections, incorporating data from multiple sectors and providing actionable insights for stakeholders.

## Executive Summary

The global financial markets have shown remarkable resilience in the face of various challenges. Key findings include:

* Sustained growth in the technology sector despite market volatility, with particularly strong performance in AI and cloud services
* Emerging markets showing strong recovery patterns driven by improved commodity prices and increased foreign direct investment

## Market Share Distribution

Current market share analysis shows interesting patterns:

```python
import plotly.express as px
import pandas as pd

data = {
    'Provider': ['AWS', 'Azure', 'Google Cloud', 'Alibaba Cloud', 'Others'],
    'Share': [34, 33, 16, 10, 7]
}
df = pd.DataFrame(data)
fig = px.pie(df, values='Share', names='Provider', title='Cloud Market Share 2024')
```

The cloud computing market continues to evolve rapidly, with major providers competing for market share.

## Government Spending Analysis

Understanding the flow of public funds provides crucial insights into economic priorities:

| Spending Category | 2023 Budget | 2024 Budget | YoY Change | % of Total |
|-------------------|-------------|-------------|------------|------------|
| Healthcare        | $1,200B     | $1,320B     | +10%       | 28%        |
| Social Security   | $1,100B     | $1,150B     | +4.5%      | 24%        |
| Defense          | $750B       | $780B       | +4%        | 16%        |
| Education        | $480B       | $520B       | +8.3%      | 11%        |
| Infrastructure   | $350B       | $420B       | +20%       | 9%         |
| Research & Dev   | $280B       | $310B       | +10.7%     | 6%         |
| Other Programs   | $290B       | $300B       | +3.4%      | 6%         |
| Total            | $4,450B     | $4,800B     | +7.9%      | 100%       |

### Market Trends

Analysis of market movements and future projections reveals several important patterns:

```python
import plotly.graph_objects as go

# Create sample data
dates = ["2023-01", "2023-03", "2023-06", "2023-09", "2023-12", "2024-03"]
stock_a = [100, 120, 150, 140, 180, 190]
stock_b = [90, 95, 85, 110, 120, 135]

# Create figure with multiple traces
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(
    x=dates,
    y=stock_a,
    mode='lines+markers',
    name='Stock A'
))

fig.add_trace(go.Scatter(
    x=dates,
    y=stock_b,
    mode='lines+markers',
    name='Stock B'
))

# Update layout
fig.update_layout(
    title='Market Performance Trends',
    xaxis_title='Date',
    yaxis_title='Price ($)'
)
```

## Resource Distribution

This Sankey diagram illustrates the complex flow between funding sources and spending categories:

```python
import plotly.graph_objects as go

# Data for Sankey diagram
labels = ["Income Tax", "Corporate Tax", "Other Revenue", 
          "Healthcare", "Social Security", "Defense", "Other Spending"]
colors = ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", 
          "#fb9a99", "#e31a1c", "#fdbf6f"]

# Source and target indices
source = [0, 1, 2, 0, 1, 2]
target = [3, 4, 5, 6, 6, 6]
value = [1200, 800, 600, 900, 700, 1000]

# Create Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=colors
    ),
    link=dict(
        source=source,
        target=target,
        value=value
    )
)])

fig.update_layout(
    title='Federal Budget Flow (Billions USD)',
    font_size=10
)
```

## Retail Sector Performance

The retail sector has undergone significant transformation, with several key trends emerging:

* Increased adoption of e-commerce platforms with seamless integration between physical stores and digital channels for omnichannel experiences
* Integration of AR/VR technologies in shopping experiences, allowing customers to virtually try products before making purchase decisions
* Strategic focus on sustainability and ethical sourcing practices, with enhanced transparency in supply chain management and carbon footprint
* Revolutionary improvements in last-mile delivery solutions through AI-powered route optimization and autonomous delivery vehicles

## Risk Assessment

Several key risk factors require careful monitoring:

1. Geopolitical tensions affecting trade relations
2. Inflationary pressures in major economies
3. Regulatory changes in technology sector
4. Climate-related disruptions to supply chains

> **Strategic Recommendation**: Focus on diversification across sectors while maintaining adequate liquidity buffers to manage potential market volatility.

---

**Note**: This analysis is based on current market data and projections. Regular updates will be provided as new information becomes available.
"""


def test_docx_export():
    # Test DOCX export
    docx_bytes = exportmd.to(
        markdown=SAMPLE_MARKDOWN, 
        format='docx',
        style='style1'
    )
    assert len(docx_bytes) > 0
    assert isinstance(docx_bytes, bytes)
    
    with open('test_output.docx', 'wb') as f:
        f.write(docx_bytes)

def test_pptx_export():
    pptx_bytes = exportmd.to(markdown=SAMPLE_MARKDOWN, format='pptx', style='style1')
    assert len(pptx_bytes) > 0
    assert isinstance(pptx_bytes, bytes)
    
    with open('test_output.pptx', 'wb') as f:
        f.write(pptx_bytes)

def test_file_output():
    # Test saving to file
    output_file = "test_output.pdf"
    exportmd.to(SAMPLE_MARKDOWN, format='pdf', output_file=str(output_file))
    assert os.path.exists(output_file)
    assert os.path.getsize(output_file) > 0

def test_invalid_format():
    # Test invalid format
    with pytest.raises(ValueError):
        exportmd.to(SAMPLE_MARKDOWN, format='invalid')

def test_different_styles():
    # Test different styles
    for style in ['style1', 'style2', 'style3']:
        pdf_bytes = exportmd.to(markdown=SAMPLE_MARKDOWN, format='pdf', style=style)
        assert len(pdf_bytes) > 0
        assert isinstance(pdf_bytes, bytes)
        
        # Save for inspection
        with open(f'test_output_{style}.pdf', 'wb') as f:
            f.write(pdf_bytes)

def test_custom_style():
    # Test custom CSS style
    custom_css = """
    body {
        font-family: Arial, sans-serif;
        line-height: 1.4;
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
    }
    
    h1 {
        color: #2563eb;
        font-size: 2.2em;
        border-bottom: 2px solid currentColor;
    }
    
    .chart-container {
        width: 80%;
        margin: 2em auto;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    """
    
    pdf_bytes = exportmd.to(
        SAMPLE_MARKDOWN, 
        format='pdf',
        style='custom',
        custom_css=custom_css
    )
    
    assert len(pdf_bytes) > 0
    assert isinstance(pdf_bytes, bytes)
    
    # Save for inspection
    with open('test_output_custom.pdf', 'wb') as f:
        f.write(pdf_bytes)

def test_html_export():
    # Test HTML export
    html_bytes = exportmd.to(
        markdown=SAMPLE_MARKDOWN, 
        format='html',
        style='style1'
    )
    assert len(html_bytes) > 0
    assert isinstance(html_bytes, bytes)
    
    # Verify it's valid HTML
    html_str = html_bytes.decode('utf-8')
    assert html_str.startswith('<!DOCTYPE html>')
    assert '<html' in html_str
    assert '</html>' in html_str
    
    # Save for inspection
    with open('test_output.html', 'wb') as f:
        f.write(html_bytes)

def test_output_file_behavior():
    """Test both output methods - direct bytes and file output"""
    
    # Test bytes output
    pdf_bytes = exportmd.to(
        markdown=SAMPLE_MARKDOWN,
        format='pdf'
    )
    assert isinstance(pdf_bytes, bytes)
    assert len(pdf_bytes) > 0
    
    # Test direct file output
    output_file = "test_direct.pdf"
    result = exportmd.to(
        markdown=SAMPLE_MARKDOWN,
        format='pdf',
        output_file=str(output_file)
    )
    assert result is None  # Should return None when using output_file
    assert os.path.exists(output_file)
    assert os.path.getsize(output_file) > 0
    
    # Compare outputs are identical
    with open(output_file, 'rb') as f:
        file_bytes = f.read()
    assert file_bytes == pdf_bytes 