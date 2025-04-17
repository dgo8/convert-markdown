from abc import ABC, abstractmethod

class BaseExporter(ABC):
    @abstractmethod
    def export(self, html: str) -> bytes:
        """Convert HTML to the target format"""
        pass 