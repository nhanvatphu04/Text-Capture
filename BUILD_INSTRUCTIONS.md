# TextCapture Build Instructions

This document provides instructions for building and setting up the TextCapture application on different platforms.

## Quick Start (Recommended)

For most users, the simplified Python setup is sufficient:

```bash
python build_simple.py
```

This will install all Python dependencies and check for external tools like Tesseract.

## Full C++ Build (Advanced)

For better performance, you can build the C++ OCR module:

```bash
python build_cpp.py
```

## Platform-Specific Instructions

### Windows

#### Prerequisites

1. **Python 3.8+**: Download from [python.org](https://python.org)
2. **Visual Studio 2019/2022**: Install with "Desktop development with C++" workload
3. **CMake**: Download from [cmake.org](https://cmake.org/download/)
4. **Tesseract**: Download from [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)

#### Setup Steps

1. **Install Visual Studio**:
   - Download Visual Studio Community (free)
   - During installation, select "Desktop development with C++"
   - This includes MSVC compiler and build tools

2. **Install Tesseract**:
   - Download the Windows installer
   - Install to `C:\Program Files\Tesseract-OCR`
   - Add to PATH: `C:\Program Files\Tesseract-OCR`

3. **Run the build script**:
   ```cmd
   # Open Visual Studio Developer Command Prompt
   python build_cpp.py
   ```

#### Alternative: Python-Only Setup

If you don't want to install Visual Studio:

```cmd
python build_simple.py
```

### macOS

#### Prerequisites

1. **Python 3.8+**: Install via Homebrew or python.org
2. **Xcode Command Line Tools**: `xcode-select --install`
3. **Homebrew**: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

#### Setup Steps

1. **Install dependencies**:
   ```bash
   brew install cmake opencv tesseract
   ```

2. **Run the build script**:
   ```bash
   python build_cpp.py
   ```

#### Alternative: Python-Only Setup

```bash
python build_simple.py
```

### Linux (Ubuntu/Debian)

#### Prerequisites

1. **Python 3.8+**: `sudo apt update && sudo apt install python3 python3-pip`
2. **Build tools**: `sudo apt install build-essential cmake`
3. **Libraries**: `sudo apt install libopencv-dev tesseract-ocr libtesseract-dev`

#### Setup Steps

1. **Install dependencies**:
   ```bash
   sudo apt update
   sudo apt install build-essential cmake libopencv-dev tesseract-ocr libtesseract-dev
   ```

2. **Run the build script**:
   ```bash
   python3 build_cpp.py
   ```

#### Alternative: Python-Only Setup

```bash
python3 build_simple.py
```

## Troubleshooting

### Common Issues

#### MSVC Compiler Not Found (Windows)

**Problem**: `✗ MSVC compiler not found`

**Solution**:
1. Install Visual Studio 2019/2022 with C++ workload
2. Run the script from Visual Studio Developer Command Prompt
3. Or use the Python-only setup: `python build_simple.py`

#### OpenCV Not Found

**Problem**: `✗ OpenCV not found`

**Solutions**:
1. Install OpenCV system-wide (see platform instructions above)
2. Use Python OpenCV: `pip install opencv-python`
3. Continue without C++ OpenCV (Python fallback will be used)

#### Tesseract Not Found

**Problem**: `✗ Tesseract not found`

**Solutions**:
1. Install Tesseract system-wide (see platform instructions above)
2. Continue without C++ Tesseract (Python fallback will be used)

#### CMake Configuration Failed

**Problem**: `✗ CMake configuration failed`

**Solutions**:
1. Ensure all dependencies are installed
2. Check that CMake version is 3.16 or higher
3. Try the Python-only setup instead

### Getting Help

If you encounter issues:

1. **Check the error messages** carefully - they often contain specific instructions
2. **Try the Python-only setup** first: `python build_simple.py`
3. **Ensure all prerequisites** are installed for your platform
4. **Check the logs** for specific error details

## Running the Application

After successful setup:

```bash
python main.py
```

The application will automatically use the best available OCR implementation:
- C++ implementation (if built successfully)
- Python fallback (if C++ build failed or not attempted)

## Performance Notes

- **C++ implementation**: Faster OCR processing, better for batch operations
- **Python implementation**: Slower but more portable, works on all platforms
- **EasyOCR**: Good accuracy, works without external dependencies
- **Tesseract**: Industry standard, requires system installation

## Development

For developers who want to modify the C++ code:

1. Edit files in `src/ocr/cpp/`
2. Run `python build_cpp.py` to rebuild
3. The Python bindings are in `cpp_ocr.cpp`

The C++ module provides:
- `OCREngine` class for text recognition
- Image preprocessing functions
- Performance optimizations for large images 