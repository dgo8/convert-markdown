import plotly.graph_objects as go
import plotly.io as pio
from pathlib import Path
import json
import base64
from io import BytesIO

class ChartHandler:
    def __init__(self):
        # Configure plotly for high resolution output
        pio.kaleido.scope.default_scale = 2.0
        pio.kaleido.scope.default_width = 1200
        pio.kaleido.scope.default_height = 800
        
    def render_chart(self, config: dict) -> str:
        """Render a chart configuration to HTML"""
        fig = go.Figure(config)
        # Set higher resolution for web display
        fig.update_layout(
            width=1200,
            height=800,
            font=dict(size=18)
        )
        return fig.to_html(include_plotlyjs=False, full_html=False)
        
    def chart_to_image(self, config: dict, format: str = 'png') -> bytes:
        """Convert a chart configuration to an image"""
        fig = go.Figure(config)
        # Ensure high quality for static images
        img_bytes = pio.to_image(
            fig,
            format=format,
            scale=2.0,
            width=1200,
            height=800
        )
        return img_bytes
        
    def chart_to_base64(self, config: dict, format: str = 'png') -> str:
        """Convert a chart to base64 encoded image"""
        img_bytes = self.chart_to_image(config, format)
        return base64.b64encode(img_bytes).decode('utf-8') 