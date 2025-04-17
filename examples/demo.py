import exportmd

# Sample markdown with Python code blocks
SAMPLE_MARKDOWN = """
# Execute Markdown Code Blocks & Export to HTML, PDF, DOCX & PPTX

Python package that converts markdown text with executed code blocks to various formats. Create visual reports with charts from LLM outputs.

## Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(-10, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
plt.figure(figsize=(6, 3.4))
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')
plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
```

## Plotly

```python
import plotly.express as px

# Load and prepare sample data
df = px.data.stocks()

# Create an interactive line plot
fig = px.line(df, x='date', y=['GOOG', 'AAPL', 'AMZN'], 
              title='Stock Prices Over Time',
              labels={'value': 'Stock Price (USD)', 'variable': 'Company'})

# Update layout
fig.update_layout(
    legend_title='Companies',
    hovermode='x unified'
)
```

## Print Statements

Let's start with a simple example showing how print statements are captured:

```python
import numpy as np

# Generate some random data
data = np.random.normal(100, 15, 1000)

# Calculate basic statistics
mean = np.mean(data)
std = np.std(data)

print(f"Sample Statistics:")
print(f"- Mean: {mean:.2f}")
print(f"- Standard Deviation: {std:.2f}")
print(f"- Sample Size: {len(data)}")
```




## Seaborn

Seaborn is excellent for statistical visualizations. Here's an example using its built-in dataset:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips')

# Create a figure with multiple plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# First subplot: Box plot
sns.boxplot(data=tips, x='day', y='total_bill', hue='time', ax=ax1)
ax1.set_title('Bill Distribution by Day and Time')

# Second subplot: Scatter plot with regression line
sns.regplot(data=tips, x='total_bill', y='tip', ax=ax2)
ax2.set_title('Tips vs Total Bill')

plt.tight_layout()
plt.show()
```
> **Strategic Recommendation**: Focus on diversification across sectors while maintaining adequate liquidity buffers to manage potential market volatility.


## Bullet points visualization

The retail sector has undergone significant transformation, with several key trends emerging:

* Increased adoption of e-commerce platforms with seamless integration between physical stores and digital channels for omnichannel experiences
* Integration of AR/VR technologies in shopping experiences, allowing customers to virtually try products before making purchase decisions
* Strategic focus on sustainability and ethical sourcing practices, with enhanced transparency in supply chain management and carbon footprint
* Revolutionary improvements in last-mile delivery solutions through AI-powered route optimization and autonomous delivery vehicles

## Table visualization

Understanding the flow of public funds provides crucial insights into economic priorities:

| Spending Category | 2023 Budget | 2024 Budget | % Change | 
|-------------------|-------------|-------------|------------|
| Healthcare        | $1,200B     | $1,320B     | +10%       | 
| Social Security   | $1,100B     | $1,150B     | +4.5%      | 
| Defense          | $750B       | $780B       | +4%        | 
| Education        | $480B       | $520B       | +8.3%      | 
| Infrastructure   | $350B       | $420B       | +20%       | 
| Research & Dev   | $280B       | $310B       | +10.7%     | 
| Other Programs   | $290B       | $300B       | +3.4%      | 
| Total            | $4,450B     | $4,800B     | +7.9%      | 

## Summary

This demo shows how you can create publication-ready documents with LLM outputs.


**Note**: All code blocks are executed in real-time when the document is converted. You can modify
the code and re-run the conversion to update all outputs automatically.
"""

def main():
    formats = ['pdf', 'docx', 'pptx', 'html']
    
    for format in formats:
        print(f"\nExporting to {format}...")
        try:
            output_bytes = exportmd.to(
                markdown=SAMPLE_MARKDOWN,
                format=format,
                style='style1'
            )
            with open(f'output.{format}', 'wb') as f:
                f.write(output_bytes)
            print(f"Successfully exported to output.{format}")
            
        except Exception as e:
            print(f"Error exporting to {format}: {e}")

if __name__ == "__main__":
    main() 