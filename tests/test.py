import pytest
import ExportMd
import os

SAMPLE_MARKDOWN = """
# Sample Report

This comprehensive report analyzes current market trends and future projections, incorporating data from multiple sectors and providing actionable insights for stakeholders.

## Executive Summary

The global financial markets have shown remarkable resilience in the face of various challenges. Key findings include:

* Sustained growth in the technology sector despite market volatility, with particularly strong performance in AI and cloud services
* Emerging markets showing strong recovery patterns driven by improved commodity prices and increased foreign direct investment

## Cloud Provider Distribution

Current market share analysis of major cloud providers shows interesting patterns:

:::chart
{
  "data": [{
    "type": "pie",
    "values": [34, 33, 16, 10, 7],
    "labels": ["AWS", "Azure", "Google Cloud", "Alibaba Cloud", "Others"]
  }],
  "layout": {
    "title": "Cloud Market Share 2024"
  }
}
:::

The cloud computing market continues to evolve rapidly, with major providers competing for market share. Key developments include:

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
| **Total**        | **$4,450B** | **$4,800B** | **+7.9%**  | **100%**   |

### Market Trends

Analysis of market movements and future projections reveals several important patterns:

:::chart
{
  "data": [{
    "type": "scatter",
    "mode": "lines+markers",
    "x": ["2023-01", "2023-03", "2023-06", "2023-09", "2023-12", "2024-03"],
    "y": [100, 120, 150, 140, 180, 190],
    "name": "Stock A"
  }, {
    "type": "scatter",
    "mode": "lines+markers",
    "x": ["2023-01", "2023-03", "2023-06", "2023-09", "2023-12", "2024-03"],
    "y": [90, 95, 85, 110, 120, 135],
    "name": "Stock B"
  }],
  "layout": {
    "title": "Market Performance Trends",
    "xaxis": { "title": "Date" },
    "yaxis": { "title": "Price ($)" }
  }
}
:::

## Cloud Computing Sector Analysis

The cloud computing market continues to evolve rapidly, with major providers competing for market share. Key developments include:

* Infrastructure expansion in emerging markets with significant investments in data centers across Southeast Asia and Latin America
* Enhanced focus on security and compliance frameworks to address growing concerns about data sovereignty and privacy regulations
* Integration of advanced AI and machine learning capabilities enabling automated scaling and predictive maintenance across cloud platforms
* Growing demand for edge computing solutions driven by the increasing need for real-time processing and reduced latency requirements




### Resource Distribution

This Sankey diagram illustrates the complex flow between funding sources and spending categories:

:::chart
{
  "data": [{
    "type": "sankey",
    "orientation": "h",
    "node": {
      "label": ["Income Tax", "Corporate Tax", "Other Revenue", "Healthcare", "Social Security", "Defense", "Other Spending"],
      "color": ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f"]
    },
    "link": {
      "source": [0, 1, 2, 0, 1, 2],
      "target": [3, 4, 5, 6, 6, 6],
      "value": [1200, 800, 600, 900, 700, 1000]
    }
  }],
  "layout": {
    "title": "Federal Budget Flow (Billions USD)"
  }
}
:::

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

pptx_bytes = ExportMd.to(markdown=SAMPLE_MARKDOWN, style='style1', format='pptx')
with open('test_output.pptx', 'wb') as f:
    f.write(pptx_bytes)

