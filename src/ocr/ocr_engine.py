"""
OCR Engine - Main interface for text extraction
Supports both Python and C++ implementations
"""

import os
import sys
from typing import Optional, Dict, Any
from pathlib import Path

try:
    # Try to import C++ implementation first
    from .cpp_ocr import CppOCREngine
    CPP_AVAILABLE = True
except ImportError:
    CPP_AVAILABLE = False
    CppOCREngine = None

from .python_ocr import PythonOCREngine


class OCREngine:
    """
    Main OCR Engine that can use either C++ or Python implementation
    """
    
    def __init__(self, use_cpp: bool = True, **kwargs):
        """
        Initialize OCR Engine
        
        Args:
            use_cpp: Whether to use C++ implementation if available
            **kwargs: Additional arguments for the OCR engine
        """
        self.use_cpp = use_cpp and CPP_AVAILABLE
        self.kwargs = kwargs
        
        if self.use_cpp:
            self._engine = CppOCREngine(**kwargs)
            print("Using C++ OCR implementation")
        else:
            self._engine = PythonOCREngine(**kwargs)
            print("Using Python OCR implementation")
    
    def extract_text(self, image_path: str, **kwargs) -> str:
        """
        Extract text from image
        
        Args:
            image_path: Path to the image file
            **kwargs: Additional arguments for text extraction
            
        Returns:
            Extracted text as string
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        return self._engine.extract_text(image_path, **kwargs)
    
    def extract_text_with_confidence(self, image_path: str, **kwargs) -> Dict[str, Any]:
        """
        Extract text with confidence scores
        
        Args:
            image_path: Path to the image file
            **kwargs: Additional arguments for text extraction
            
        Returns:
            Dictionary with 'text' and 'confidence' keys
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        return self._engine.extract_text_with_confidence(image_path, **kwargs)
    
    def preprocess_image(self, image_path: str, **kwargs) -> str:
        """
        Preprocess image for better OCR results
        
        Args:
            image_path: Path to the image file
            **kwargs: Preprocessing options
            
        Returns:
            Path to preprocessed image
        """
        return self._engine.preprocess_image(image_path, **kwargs)
    
    def get_supported_languages(self) -> list:
        """
        Get list of supported languages
        
        Returns:
            List of supported language codes
        """
        return self._engine.get_supported_languages()
    
    def set_language(self, language: str):
        """
        Set OCR language
        
        Args:
            language: Language code (e.g., 'eng', 'vie')
        """
        self._engine.set_language(language)
    
    def is_cpp_available(self) -> bool:
        """
        Check if C++ implementation is available
        
        Returns:
            True if C++ implementation is available
        """
        return CPP_AVAILABLE
    
    def get_implementation_info(self) -> Dict[str, Any]:
        """
        Get information about current implementation
        
        Returns:
            Dictionary with implementation details
        """
        info = {
            'cpp_available': CPP_AVAILABLE,
            'using_cpp': self.use_cpp,
            'engine_type': type(self._engine).__name__
        }
        
        if hasattr(self._engine, 'get_info'):
            info.update(self._engine.get_info())
        
        return info 