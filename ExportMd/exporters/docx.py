import warnings
from pathlib import Path
import tempfile
from pdf2docx import Converter
from .pdf import PDFExporter

class DOCXExporter:
    def __init__(self):
        self.pdf_exporter = PDFExporter()
        
    def export(self, html: str) -> bytes:
        """Convert HTML to DOCX via PDF for better quality
        
        Args:
            html: Input HTML string
            
        Returns:
            bytes: DOCX document as bytes
        """
        try:
            # First convert to PDF
            pdf_bytes = self.pdf_exporter.export(html)
            
            # Create temporary files for conversion
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as pdf_file:
                pdf_file.write(pdf_bytes)
                pdf_path = pdf_file.name
                
            with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as docx_file:
                docx_path = docx_file.name
            
            # Convert PDF to DOCX
            cv = Converter(pdf_path)
            cv.convert(docx_path)
            cv.close()
            
            # Read DOCX bytes
            with open(docx_path, 'rb') as f:
                docx_bytes = f.read()
                
            # Cleanup temp files
            Path(pdf_path).unlink()
            Path(docx_path).unlink()
            
            return docx_bytes
            
        except Exception as e:
            print(f"Error converting to DOCX: {e}")
            raise 