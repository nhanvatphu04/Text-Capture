"""
Python OCR Implementation using EasyOCR and Tesseract
"""

import os
import sys
import tempfile
from typing import Dict, Any, List, Optional
from pathlib import Path

try:
    import easyocr
    EASYOCR_AVAILABLE = True
except ImportError:
    EASYOCR_AVAILABLE = False

try:
    import pytesseract
    from PIL import Image, ImageEnhance, ImageFilter
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False


class PythonOCREngine:
    """
    Python implementation of OCR engine using EasyOCR and Tesseract
    """
    
    def __init__(self, **kwargs):
        """
        Initialize Python OCR engine
        
        Args:
            **kwargs: Configuration options
        """
        self.language = kwargs.get('language', 'en')
        self.use_easyocr = kwargs.get('use_easyocr', True)
        self.use_tesseract = kwargs.get('use_tesseract', True)
        
        # Initialize OCR readers
        self.easyocr_reader = None
        if self.use_easyocr and EASYOCR_AVAILABLE:
            try:
                self.easyocr_reader = easyocr.Reader([self.language])
            except Exception as e:
                print(f"Failed to initialize EasyOCR: {e}")
                self.use_easyocr = False
        
        # Check Tesseract availability
        if self.use_tesseract and not TESSERACT_AVAILABLE:
            print("Tesseract not available, disabling Tesseract OCR")
            self.use_tesseract = False
        
        # Set default OCR method
        if self.use_easyocr and self.easyocr_reader:
            self.default_method = 'easyocr'
        elif self.use_tesseract:
            self.default_method = 'tesseract'
        else:
            raise RuntimeError("No OCR engine available")
    
    def extract_text(self, image_path: str, **kwargs) -> str:
        """
        Extract text from image
        
        Args:
            image_path: Path to the image file
            **kwargs: Additional options
            
        Returns:
            Extracted text
        """
        method = kwargs.get('method', self.default_method)
        
        if method == 'easyocr' and self.use_easyocr:
            return self._extract_with_easyocr(image_path, **kwargs)
        elif method == 'tesseract' and self.use_tesseract:
            return self._extract_with_tesseract(image_path, **kwargs)
        else:
            raise ValueError(f"Unsupported OCR method: {method}")
    
    def extract_text_with_confidence(self, image_path: str, **kwargs) -> Dict[str, Any]:
        """
        Extract text with confidence scores
        
        Args:
            image_path: Path to the image file
            **kwargs: Additional options
            
        Returns:
            Dictionary with text and confidence information
        """
        method = kwargs.get('method', self.default_method)
        
        if method == 'easyocr' and self.use_easyocr:
            return self._extract_with_easyocr_confidence(image_path, **kwargs)
        elif method == 'tesseract' and self.use_tesseract:
            return self._extract_with_tesseract_confidence(image_path, **kwargs)
        else:
            raise ValueError(f"Unsupported OCR method: {method}")
    
    def preprocess_image(self, image_path: str, **kwargs) -> str:
        """
        Preprocess image for better OCR results
        
        Args:
            image_path: Path to the image file
            **kwargs: Preprocessing options
            
        Returns:
            Path to preprocessed image
        """
        if not TESSERACT_AVAILABLE:
            return image_path
        
        try:
            # Load image
            image = Image.open(image_path)
            
            # Apply preprocessing options
            if kwargs.get('enhance_contrast', True):
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(1.5)
            
            if kwargs.get('enhance_sharpness', True):
                enhancer = ImageEnhance.Sharpness(image)
                image = enhancer.enhance(1.5)
            
            if kwargs.get('denoise', True):
                image = image.filter(ImageFilter.MedianFilter(size=3))
            
            if kwargs.get('grayscale', True):
                image = image.convert('L')
            
            # Save preprocessed image
            output_path = kwargs.get('output_path')
            if not output_path:
                temp_dir = tempfile.gettempdir()
                filename = Path(image_path).stem + '_preprocessed.png'
                output_path = os.path.join(temp_dir, filename)
            
            image.save(output_path)
            return output_path
            
        except Exception as e:
            print(f"Error preprocessing image: {e}")
            return image_path
    
    def get_supported_languages(self) -> List[str]:
        """
        Get list of supported languages
        
        Returns:
            List of supported language codes
        """
        languages = []
        
        if self.use_easyocr and EASYOCR_AVAILABLE:
            languages.extend(['en', 'vi', 'zh', 'ja', 'ko', 'th', 'ar', 'hi'])
        
        if self.use_tesseract and TESSERACT_AVAILABLE:
            try:
                # Get Tesseract languages
                tesseract_langs = pytesseract.get_languages()
                languages.extend(tesseract_langs)
            except Exception as e:
                print(f"Error getting Tesseract languages: {e}")
        
        return list(set(languages))  # Remove duplicates
    
    def set_language(self, language: str):
        """
        Set OCR language
        
        Args:
            language: Language code
        """
        self.language = language
        
        # Reinitialize EasyOCR reader if needed
        if self.use_easyocr and EASYOCR_AVAILABLE:
            try:
                self.easyocr_reader = easyocr.Reader([language])
            except Exception as e:
                print(f"Failed to set EasyOCR language: {e}")
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get engine information
        
        Returns:
            Dictionary with engine information
        """
        return {
            'engine': 'Python',
            'easyocr_available': EASYOCR_AVAILABLE,
            'tesseract_available': TESSERACT_AVAILABLE,
            'use_easyocr': self.use_easyocr,
            'use_tesseract': self.use_tesseract,
            'default_method': self.default_method,
            'language': self.language
        }
    
    def _extract_with_easyocr(self, image_path: str, **kwargs) -> str:
        """Extract text using EasyOCR"""
        if not self.easyocr_reader:
            raise RuntimeError("EasyOCR reader not initialized")
        
        try:
            results = self.easyocr_reader.readtext(image_path)
            text = ' '.join([result[1] for result in results])
            return text
        except Exception as e:
            raise RuntimeError(f"EasyOCR extraction failed: {e}")
    
    def _extract_with_easyocr_confidence(self, image_path: str, **kwargs) -> Dict[str, Any]:
        """Extract text with confidence using EasyOCR"""
        if not self.easyocr_reader:
            raise RuntimeError("EasyOCR reader not initialized")
        
        try:
            results = self.easyocr_reader.readtext(image_path)
            
            text_parts = []
            confidences = []
            
            for bbox, text, confidence in results:
                text_parts.append(text)
                confidences.append(confidence)
            
            full_text = ' '.join(text_parts)
            avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
            
            return {
                'text': full_text,
                'confidence': avg_confidence,
                'text_parts': text_parts,
                'confidences': confidences,
                'bboxes': [result[0] for result in results]
            }
        except Exception as e:
            raise RuntimeError(f"EasyOCR extraction failed: {e}")
    
    def _extract_with_tesseract(self, image_path: str, **kwargs) -> str:
        """Extract text using Tesseract"""
        if not TESSERACT_AVAILABLE:
            raise RuntimeError("Tesseract not available")
        
        try:
            # Preprocess image if requested
            if kwargs.get('preprocess', True):
                image_path = self.preprocess_image(image_path, **kwargs)
            
            # Extract text
            text = pytesseract.image_to_string(
                Image.open(image_path),
                lang=self.language,
                config=kwargs.get('tesseract_config', '--psm 6')
            )
            
            return text.strip()
        except Exception as e:
            raise RuntimeError(f"Tesseract extraction failed: {e}")
    
    def _extract_with_tesseract_confidence(self, image_path: str, **kwargs) -> Dict[str, Any]:
        """Extract text with confidence using Tesseract"""
        if not TESSERACT_AVAILABLE:
            raise RuntimeError("Tesseract not available")
        
        try:
            # Preprocess image if requested
            if kwargs.get('preprocess', True):
                image_path = self.preprocess_image(image_path, **kwargs)
            
            # Extract text with confidence
            data = pytesseract.image_to_data(
                Image.open(image_path),
                lang=self.language,
                config=kwargs.get('tesseract_config', '--psm 6'),
                output_type=pytesseract.Output.DICT
            )
            
            # Process results
            text_parts = []
            confidences = []
            
            for i, conf in enumerate(data['conf']):
                if conf > 0:  # Filter out low confidence results
                    text_parts.append(data['text'][i])
                    confidences.append(conf)
            
            full_text = ' '.join(text_parts)
            avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
            
            return {
                'text': full_text,
                'confidence': avg_confidence,
                'text_parts': text_parts,
                'confidences': confidences,
                'raw_data': data
            }
        except Exception as e:
            raise RuntimeError(f"Tesseract extraction failed: {e}") 