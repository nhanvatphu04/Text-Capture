"""
OCR module for TextCapture application
Supports both Python and C++ implementations
"""

from .ocr_engine import OCREngine
from .image_processor import ImageProcessor

__all__ = ['OCREngine', 'ImageProcessor'] 