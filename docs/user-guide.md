# TextCapture User Guide

Welcome to TextCapture! This guide will help you get started with extracting text from images using our powerful OCR application.

## 🚀 Getting Started

### First Launch
1. **Run the application**: `python main.py`
2. **Interface overview**: You'll see a dark-themed window with:
   - Image display area (left side)
   - Text editor (right side)
   - Control buttons (bottom)

### Loading Images
You can load images in several ways:

#### Method 1: Drag & Drop
- Simply drag any image file from your file explorer
- Drop it onto the image display area
- The image will appear immediately

#### Method 2: Click to Browse
- Click on the image display area
- Select an image file from the file dialog
- Supported formats: PNG, JPG, JPEG, BMP, GIF, TIFF, WebP

## 📝 Text Extraction

### Basic OCR Process
1. **Load an image** using any method above
2. **Click "Get Text"** button
3. **Wait for processing** (progress indicator will show)
4. **Review extracted text** in the text editor

### Supported Languages
TextCapture supports multiple languages:
- **English** (default)
- **Vietnamese** (Tiếng Việt)
- **Japanese** (日本語)
- **And more** (depending on Tesseract installation)

### OCR Quality Tips
For best results:
- **High resolution images** (300+ DPI)
- **Good contrast** between text and background
- **Clear, readable fonts**
- **Well-lit images** (avoid shadows)

## ✏️ Text Editing & Formatting

### Text Formatting
Use the formatting buttons to modify text:

#### Case Conversion
- **Sentence Case**: Capitalizes first letter of each sentence
- **Lower Case**: Converts all text to lowercase
- **Upper Case**: Converts all text to uppercase

#### Text Decoration
- **Underline**: Adds underline formatting
- **Strikethrough**: Adds strikethrough formatting

### Formatting Tips
- **Toggle states**: Buttons show visual feedback when active
- **Multiple formats**: You can apply multiple formats
- **Reset formatting**: Use "Refresh" button to clear all

## 🔧 Advanced Features

### Image Preprocessing
TextCapture automatically applies preprocessing to improve OCR accuracy:
- **Contrast enhancement**
- **Noise reduction**
- **Sharpening**
- **Grayscale conversion**

### Performance Options
- **C++ Mode**: If available, provides 2-5x faster processing
- **Python Mode**: Fallback mode with good accuracy
- **Auto-detection**: App automatically chooses best available mode

### Error Handling
The application gracefully handles:
- **Invalid image files**
- **Corrupted images**
- **Unsupported formats**
- **OCR processing errors**

## 🆘 Troubleshooting

### Common Issues

#### "No text detected"
- **Check image quality**: Ensure text is clear and readable
- **Try preprocessing**: Use image editing software to enhance contrast
- **Check language**: Ensure correct language is selected
- **Resize image**: Very large images may cause issues

#### "Slow processing"
- **Enable C++ mode**: Build C++ module for faster processing
- **Reduce image size**: Large images take longer to process
- **Close other applications**: Free up system resources

#### "Incorrect text recognition"
- **Improve image quality**: Use higher resolution images
- **Check language setting**: Ensure correct language is selected
- **Try different preprocessing**: Experiment with image editing

### Getting Help
- **Check main README**: For installation and setup issues
- **Review troubleshooting guide**: For detailed solutions
- **Create an issue**: On GitHub for bugs or feature requests

## 📋 Tips & Best Practices

### Image Preparation
- **Use high-resolution images** (300+ DPI for documents)
- **Ensure good lighting** when capturing images
- **Avoid shadows and reflections**
- **Use plain backgrounds** when possible

### Text Processing
- **Review extracted text** carefully
- **Use formatting tools** to clean up text
- **Save important results** to avoid losing work
- **Experiment with different settings** for best results

### Performance
- **Enable C++ mode** for faster processing
- **Close unnecessary applications** during processing
- **Use appropriate image sizes** (not too large or small)

## 🔄 Updates & Maintenance

### Keeping Updated
- **Check for updates** regularly
- **Update Tesseract** for improved language support
- **Rebuild C++ module** after updates if needed

### Data Management
- **Backup important extracted text**
- **Organize images** for easy access
- **Clean up temporary files** periodically

---

*For technical support or feature requests, please visit our [GitHub repository](https://github.com/nhanvatphu04/Text-Capture).* 