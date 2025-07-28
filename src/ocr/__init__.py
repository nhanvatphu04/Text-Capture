"""
OCR module for TextCapture application
Supports both Python and C++ implementations
"""

from .ocr_engine import OCREngine
from .cpp_ocr import CppOCREngine, is_cpp_available, get_cpp_dependencies, get_cpp_version

__all__ = [
    'OCREngine',
    'CppOCREngine', 
    'is_cpp_available',
    'get_cpp_dependencies',
    'get_cpp_version'
] 