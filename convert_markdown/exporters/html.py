class HTMLExporter:
    def export(self, html: str) -> bytes:
        """Convert HTML string to bytes
        
        Args:
            html: Input HTML string
            
        Returns:
            bytes: HTML document as bytes
        """
        return html.encode('utf-8') 