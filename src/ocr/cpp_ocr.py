"""
Python wrapper for C++ OCR engine
This module provides a fallback to Python implementation if C++ is not available
"""

import os
import sys
from typing import Dict, Any, Optional

try:
    # Try to import C++ implementation
    from .cpp.cpp_ocr import OCREngine as _CppOCREngine
    CPP_AVAILABLE = True
except ImportError:
    try:
        # Try alternative import path for compiled module
        import sys
        import os
        release_path = os.path.join(os.path.dirname(__file__), '..', 'Release')
        if release_path not in sys.path:
            sys.path.append(release_path)
        from cpp_ocr import OCREngine as _CppOCREngine
        CPP_AVAILABLE = True
    except ImportError:
        CPP_AVAILABLE = False
        _CppOCREngine = None


class CppOCREngine:
    """
    C++ OCR Engine wrapper with fallback to Python implementation
    """
    
    def __init__(self, **kwargs):
        """
        Initialize C++ OCR engine
        
        Args:
            **kwargs: Configuration options
        """
        if not CPP_AVAILABLE:
            raise ImportError(
                "C++ OCR engine not available. "
                "Please install required dependencies: OpenCV, Tesseract, pybind11"
            )
        
        self._engine = _CppOCREngine()
        self.language = kwargs.get('language', 'eng')
    
    def initialize(self, language: str = 'eng') -> bool:
        """
        Initialize the C++ OCR engine with specified language

        Args:
            language: Language code for OCR

        Returns:
            True if initialization successful, False otherwise
        """
        self.language = language
        return self._engine.initialize(language)
    
    def enable_external_tokenizer(self, enable: bool = True, service_url: str = "http://localhost:5001") -> None:
        """
        Enable external Vietnamese tokenizer service
        
        Args:
            enable: Whether to enable external tokenizer
            service_url: URL of the tokenizer service
        """
        self._engine.set_tokenizer_service_url(service_url)
        self._engine.enable_external_tokenizer(enable)
    
    def is_external_tokenizer_available(self) -> bool:
        """
        Check if external tokenizer service is available
        
        Returns:
            True if service is available, False otherwise
        """
        return self._engine.is_external_tokenizer_available()
    
    def extract_text(self, image_path: str, **kwargs) -> str:
        """
        Extract text from image
        
        Args:
            image_path: Path to the image file
            **kwargs: Additional options
            
        Returns:
            Extracted text
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        return self._engine.extract_text(image_path)
    
    def extract_text_with_confidence(self, image_path: str, **kwargs) -> Dict[str, Any]:
        """
        Extract text with confidence scores
        
        Args:
            image_path: Path to the image file
            **kwargs: Additional options
            
        Returns:
            Dictionary with text and confidence information
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        result = self._engine.extract_text_with_confidence(image_path)
        
        return {
            'text': result.text,
            'confidence': result.confidence,
            'text_parts': result.text_parts,
            'confidences': result.confidences,
            'bounding_boxes': result.bounding_boxes
        }
    
    def preprocess_image(self, image_path: str, **kwargs) -> str:
        """
        Preprocess image for better OCR results
        
        Args:
            image_path: Path to the image file
            **kwargs: Preprocessing options
            
        Returns:
            Path to preprocessed image
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        return self._engine.preprocess_image(
            image_path,
            kwargs.get('enhance_contrast', True),
            kwargs.get('enhance_sharpness', True),
            kwargs.get('denoise', True),
            kwargs.get('grayscale', True)
        )
    
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
            language: Language code
        """
        if self._engine.set_language(language):
            self.language = language
        else:
            raise RuntimeError(f"Failed to set language: {language}")
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get engine information
        
        Returns:
            Dictionary with engine information
        """
        return {
            'engine': 'C++',
            'cpp_available': CPP_AVAILABLE,
            'language': self.language,
            'info': self._engine.get_info()
        }
    
    def __repr__(self):
        return f"CppOCREngine(language='{self.language}', cpp_available={CPP_AVAILABLE})"


def is_cpp_available() -> bool:
    """
    Check if C++ implementation is available
    
    Returns:
        True if C++ implementation is available
    """
    return CPP_AVAILABLE


def get_cpp_dependencies() -> Dict[str, str]:
    """
    Get required C++ dependencies
    
    Returns:
        Dictionary with dependency information
    """
    if CPP_AVAILABLE:
        try:
            from .cpp.cpp_ocr import get_dependencies
            return get_dependencies()
        except ImportError:
            pass
    
    return {
        'opencv': '4.x',
        'tesseract': '5.x',
        'pybind11': '2.x'
    }


def get_cpp_version() -> str:
    """
    Get C++ module version
    
    Returns:
        Version string
    """
    if CPP_AVAILABLE:
        try:
            from .cpp.cpp_ocr import get_version
            return get_version()
        except ImportError:
            pass
    
    return "Not available" 