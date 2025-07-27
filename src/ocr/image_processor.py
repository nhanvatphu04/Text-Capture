"""
Image Processor - Advanced image preprocessing for OCR
"""

import os
import cv2
import numpy as np
from typing import Dict, Any, Optional, Tuple
from pathlib import Path
import tempfile

try:
    from PIL import Image, ImageEnhance, ImageFilter, ImageOps
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


class ImageProcessor:
    """
    Advanced image processor for OCR preprocessing
    """
    
    def __init__(self, **kwargs):
        """
        Initialize image processor
        
        Args:
            **kwargs: Configuration options
        """
        self.use_opencv = kwargs.get('use_opencv', True)
        self.use_pil = kwargs.get('use_pil', True) and PIL_AVAILABLE
        
        # Default preprocessing settings
        self.default_settings = {
            'enhance_contrast': True,
            'enhance_sharpness': True,
            'denoise': True,
            'grayscale': True,
            'deskew': True,
            'remove_noise': True,
            'binarize': False,
            'resize': False,
            'resize_factor': 2.0
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
        
        # Merge settings
        settings = {**self.default_settings, **kwargs}
        
        try:
            if self.use_opencv:
                return self._preprocess_with_opencv(image_path, settings)
            elif self.use_pil:
                return self._preprocess_with_pil(image_path, settings)
            else:
                raise RuntimeError("No image processing library available")
                
        except Exception as e:
            print(f"Error preprocessing image: {e}")
            return image_path
    
    def _preprocess_with_opencv(self, image_path: str, settings: Dict[str, Any]) -> str:
        """Preprocess image using OpenCV"""
        # Load image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Failed to load image: {image_path}")
        
        # Apply preprocessing
        processed = image.copy()
        
        # Convert to grayscale
        if settings['grayscale']:
            processed = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
        
        # Enhance contrast
        if settings['enhance_contrast']:
            processed = self._enhance_contrast_opencv(processed)
        
        # Enhance sharpness
        if settings['enhance_sharpness']:
            processed = self._enhance_sharpness_opencv(processed)
        
        # Denoise
        if settings['denoise']:
            processed = self._denoise_opencv(processed)
        
        # Remove noise
        if settings['remove_noise']:
            processed = self._remove_noise_opencv(processed)
        
        # Deskew
        if settings['deskew']:
            processed = self._deskew_opencv(processed)
        
        # Binarize
        if settings['binarize']:
            processed = self._binarize_opencv(processed)
        
        # Resize
        if settings['resize']:
            processed = self._resize_opencv(processed, settings['resize_factor'])
        
        # Save processed image
        output_path = self._generate_output_path(image_path, "_opencv_processed")
        cv2.imwrite(output_path, processed)
        
        return output_path
    
    def _preprocess_with_pil(self, image_path: str, settings: Dict[str, Any]) -> str:
        """Preprocess image using PIL"""
        # Load image
        image = Image.open(image_path)
        
        # Apply preprocessing
        processed = image.copy()
        
        # Convert to grayscale
        if settings['grayscale']:
            processed = processed.convert('L')
        
        # Enhance contrast
        if settings['enhance_contrast']:
            enhancer = ImageEnhance.Contrast(processed)
            processed = enhancer.enhance(1.5)
        
        # Enhance sharpness
        if settings['enhance_sharpness']:
            enhancer = ImageEnhance.Sharpness(processed)
            processed = enhancer.enhance(1.5)
        
        # Denoise
        if settings['denoise']:
            processed = processed.filter(ImageFilter.MedianFilter(size=3))
        
        # Remove noise
        if settings['remove_noise']:
            processed = self._remove_noise_pil(processed)
        
        # Deskew
        if settings['deskew']:
            processed = self._deskew_pil(processed)
        
        # Binarize
        if settings['binarize']:
            processed = self._binarize_pil(processed)
        
        # Resize
        if settings['resize']:
            processed = self._resize_pil(processed, settings['resize_factor'])
        
        # Save processed image
        output_path = self._generate_output_path(image_path, "_pil_processed")
        processed.save(output_path)
        
        return output_path
    
    # OpenCV preprocessing methods
    
    def _enhance_contrast_opencv(self, image: np.ndarray) -> np.ndarray:
        """Enhance contrast using OpenCV"""
        # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        return clahe.apply(image)
    
    def _enhance_sharpness_opencv(self, image: np.ndarray) -> np.ndarray:
        """Enhance sharpness using OpenCV"""
        kernel = np.array([[-1, -1, -1],
                          [-1,  9, -1],
                          [-1, -1, -1]])
        return cv2.filter2D(image, -1, kernel)
    
    def _denoise_opencv(self, image: np.ndarray) -> np.ndarray:
        """Denoise image using OpenCV"""
        return cv2.fastNlMeansDenoising(image)
    
    def _remove_noise_opencv(self, image: np.ndarray) -> np.ndarray:
        """Remove noise using OpenCV"""
        # Apply morphological operations
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        return image
    
    def _deskew_opencv(self, image: np.ndarray) -> np.ndarray:
        """Deskew image using OpenCV"""
        # Find contours
        coords = np.column_stack(np.where(image > 0))
        if len(coords) == 0:
            return image
        
        # Find minimum area rectangle
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = 90 + angle
        
        # Rotate image
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        
        return rotated
    
    def _binarize_opencv(self, image: np.ndarray) -> np.ndarray:
        """Binarize image using OpenCV"""
        # Apply Otsu's thresholding
        _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return binary
    
    def _resize_opencv(self, image: np.ndarray, factor: float) -> np.ndarray:
        """Resize image using OpenCV"""
        height, width = image.shape[:2]
        new_height, new_width = int(height * factor), int(width * factor)
        return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    
    # PIL preprocessing methods
    
    def _remove_noise_pil(self, image: Image.Image) -> Image.Image:
        """Remove noise using PIL"""
        # Apply unsharp mask
        return image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    
    def _deskew_pil(self, image: Image.Image) -> Image.Image:
        """Deskew image using PIL"""
        # Convert to numpy for processing
        img_array = np.array(image)
        
        # Find contours
        coords = np.column_stack(np.where(img_array > 0))
        if len(coords) == 0:
            return image
        
        # Find minimum area rectangle
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = 90 + angle
        
        # Rotate image
        return image.rotate(angle, expand=True, fillcolor=255)
    
    def _binarize_pil(self, image: Image.Image) -> Image.Image:
        """Binarize image using PIL"""
        # Convert to grayscale if not already
        if image.mode != 'L':
            image = image.convert('L')
        
        # Apply threshold
        threshold = 128
        return image.point(lambda x: 0 if x < threshold else 255, '1')
    
    def _resize_pil(self, image: Image.Image, factor: float) -> Image.Image:
        """Resize image using PIL"""
        width, height = image.size
        new_width, new_height = int(width * factor), int(height * factor)
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Utility methods
    
    def _generate_output_path(self, original_path: str, suffix: str) -> str:
        """Generate output path for processed image"""
        path = Path(original_path)
        temp_dir = Path(tempfile.gettempdir()) / "textcapture"
        temp_dir.mkdir(exist_ok=True)
        
        filename = f"{path.stem}{suffix}{path.suffix}"
        return str(temp_dir / filename)
    
    def get_available_methods(self) -> Dict[str, bool]:
        """Get available processing methods"""
        return {
            'opencv': self.use_opencv,
            'pil': self.use_pil
        }
    
    def get_default_settings(self) -> Dict[str, Any]:
        """Get default preprocessing settings"""
        return self.default_settings.copy() 