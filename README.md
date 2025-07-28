# TextCapture

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PySide6](https://img.shields.io/badge/PySide6-6.0+-green.svg)](https://doc.qt.io/qtforpython/)
[![Tesseract](https://img.shields.io/badge/Tesseract-5.0+-orange.svg)](https://github.com/tesseract-ocr/tesseract)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern desktop application for extracting text from images using OCR (Optical Character Recognition) technology. Built with PySide6 and featuring a sleek dark theme interface.

**🚀 Key Features:**
- **⚡ High Performance**: C++ implementation for 2-5x faster processing
- **🌍 Multi-language**: English, Vietnamese, Japanese, and more
- **🎨 Modern UI**: Dark theme with drag & drop support
- **🔍 Advanced OCR**: Tesseract + EasyOCR for accurate text recognition

## Features

### 🖼️ Image Processing
- **Drag & Drop Support**: Simply drag and drop images into the application
- **Multiple Image Formats**: Supports PNG, JPG, JPEG, BMP, GIF, TIFF, and WebP
- **Click to Select**: Click on the image area to browse and select images from your device
- **Real-time Preview**: See your selected image before processing

### 📝 Text Extraction & Editing
- **OCR Technology**: Powered by EasyOCR and Tesseract for accurate text recognition
- **Rich Text Editor**: Edit extracted text with formatting options
- **Text Formatting**: Apply various text transformations:
  - **Case Conversion**: Sentence case, lowercase, uppercase
  - **Text Decoration**: Underline, strikethrough
  - **Toggle States**: Visual feedback for active formatting options

### 🎨 Modern UI
- **Dark Theme**: Easy on the eyes with a professional dark interface
- **JetBrains Mono Font**: Clean, readable monospace font for text editing
- **Responsive Design**: Adapts to different window sizes
- **Visual Feedback**: Loading states, success/error indicators, and drag-over effects

### 🔧 User Experience
- **Button States**: Visual feedback during processing operations
- **Error Handling**: Graceful handling of invalid files and processing errors
- **Thread-Safe Operations**: Non-blocking UI during image processing
- **C++ Performance**: Optional C++ implementation for 2-5x faster processing


## Quick Start for New Developers

### 🚀 First Time Setup

If you just pulled this project from git, follow these steps:

1. **Clone and navigate to project**:
   ```bash
   git clone https://github.com/nhanvatphu04/Text-Capture.git
   cd TextCapture
   ```

2. **Setup Python environment**:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate (Windows)
   venv\Scripts\activate
   
   # Activate (macOS/Linux)
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR** (required):
   - **Windows**: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

4. **Setup VS Code** (optional, for development):
   ```bash
   # Copy VS Code configuration template
   cp .vscode/c_cpp_properties.json.template .vscode/c_cpp_properties.json
   ```
   
   Then follow the [VS Code Setup Guide](.vscode/README.md) to configure your environment.

5. **Compile resources**:
   ```bash
   python src/utils/compile_resources.py
   ```

6. **Run the application**:
   ```bash
   python main.py
   ```

### 🔧 Optional: C++ Setup (for high performance)

For 2-5x faster processing, build the C++ module:

1. **Install C++ dependencies**:
   - **Windows**: Visual Studio 2022 with C++ tools
   - **macOS**: Xcode Command Line Tools
   - **Linux**: GCC/Clang, CMake

2. **Install OpenCV and vcpkg**:
   ```bash
   # Windows (using vcpkg)
   git clone https://github.com/Microsoft/vcpkg.git
   cd vcpkg
   .\bootstrap-vcpkg.bat
   .\vcpkg install opencv:x64-windows
   ```

3. **Build C++ module**:
   ```bash
   python build_cpp.py
   ```

See [OCR Module README](src/ocr/README.md) for detailed C++ setup instructions.

## Installation

### Prerequisites

1. **Python 3.8+**: Make sure you have Python 3.8 or higher installed
2. **Tesseract OCR**: Install Tesseract OCR engine
   - **Windows**: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

### Optional: C++ Dependencies (for high performance)

For 2-5x faster processing, you can build the C++ module:

1. **C++ Compiler**: Visual Studio (Windows), GCC/Clang (Linux/macOS)
2. **CMake**: Build system
3. **OpenCV**: Computer vision library
4. **Tesseract**: OCR engine (C++ version)

See [OCR Module README](src/ocr/README.md) for detailed installation instructions.

## Usage

### Running the Application

```bash
python main.py
```

### 🆘 Common Issues & Solutions

#### "Module not found" errors
```bash
# Make sure you're in the virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

#### "Tesseract not found" error
- **Windows**: Add Tesseract to PATH or set `TESSDATA_PREFIX` environment variable
- **macOS/Linux**: Install Tesseract using package manager

#### "C++ module not available" warning
- This is normal if you haven't built the C++ module
- The app will fall back to Python implementation
- Follow the C++ setup guide above for better performance

#### VS Code IntelliSense issues
- Copy the template: `cp .vscode/c_cpp_properties.json.template .vscode/c_cpp_properties.json`
- Update paths in the file with your local paths
- See [VS Code Setup Guide](.vscode/README.md) for details

### Basic Workflow

1. **Load an Image**:
   - Drag and drop an image file into the application
   - Or click on the image area to browse and select a file

2. **Extract Text**:
   - Click the "Get Text" button to perform OCR
   - The extracted text will appear in the text editor

3. **Edit and Format**:
   - Use the formatting buttons to modify the text:
     - **Sentence Case**: Capitalize first letter of each sentence
     - **Lower Case**: Convert all text to lowercase
     - **Upper Case**: Convert all text to uppercase
     - **Underline**: Add underline formatting
     - **Strikethrough**: Add strikethrough formatting

4. **Clear and Reset**:
   - Use the "Refresh" button to clear both image and text
   - Reset all formatting states

### Advanced Features

- **Processing States**: Buttons show visual feedback during operations
- **Error Handling**: Invalid images or processing errors are clearly indicated
- **Thread Safety**: UI remains responsive during background operations

## Development

### Building from Source

1. **Install development dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Compile UI files** (if you modify the .ui file):
   ```bash
   pyside6-uic src/widgets/form.ui -o src/widgets/ui_form.py
   ```

3. **Compile resources** (if you add new resources):
   ```bash
   pyside6-rcc resources.qrc -o src/resources_rc.py
   ```

### Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Document functions and classes
- Keep CSS classes and properties minimal and focused

## Dependencies

### Core Dependencies
- **PySide6**: Qt framework for Python
- **Pillow**: Image processing library
- **EasyOCR**: OCR engine for text recognition
- **pytesseract**: Python wrapper for Tesseract OCR
- **OpenCV**: Computer vision library
- **pybind11**: C++ Python bindings

### System Dependencies
- **Tesseract OCR**: OCR engine (must be installed separately)
- **OpenCV**: Computer vision library (for C++ implementation)
- **C++ Compiler**: For building high-performance module

### Development Dependencies
- **CMake**: Build system for C++ modules
- **Visual Studio**: C++ compiler (Windows)
- **vcpkg**: Package manager for C++ libraries

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **JetBrains Mono**: Font used in the application
- **EasyOCR**: OCR engine for text recognition
- **Tesseract**: OCR engine backend
- **PySide6**: Qt framework for Python

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/nhanvatphu04/Text-Capture/issues) page
2. Create a new issue with detailed information
3. Include system information and error messages

## Performance

### C++ vs Python Implementation

| Feature | Python | C++ | Improvement |
|---------|--------|-----|-------------|
| Text Extraction | ~2-3s | ~0.5-1s | **2-5x faster** |
| Image Preprocessing | ~1-2s | ~0.2-0.5s | **3-4x faster** |
| Memory Usage | Higher | Lower | **30-50% less** |

*Performance may vary based on image size and complexity*

## Roadmap

- [x] C++ implementation for high performance
- [x] Advanced image preprocessing
- [x] Multi-language OCR support
- [ ] Camera capture functionality
- [ ] Batch processing for multiple images
- [ ] Export to different formats (PDF, DOCX, TXT)
- [ ] Language detection and multi-language support
- [ ] Advanced text formatting options
- [ ] Plugin system for custom OCR engines
