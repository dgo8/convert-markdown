from . import BaseExporter
from weasyprint import HTML
class PDFExporter(BaseExporter):
    def export(self, html: str) -> bytes:
        """Convert HTML to PDF"""
        pdf = HTML(string=html).write_pdf()
        return pdf 