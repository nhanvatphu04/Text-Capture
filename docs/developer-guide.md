# TextCapture Developer Guide

Welcome, developers! This guide will help you set up the development environment and understand the codebase structure.

## 🛠️ Development Setup

### Prerequisites
- **Python 3.8+**
- **Git**
- **C++ Compiler** (for C++ module development)
- **CMake** (for building C++ modules)
- **Tesseract OCR**

### Environment Setup

#### 1. Clone and Setup
```bash
git clone https://github.com/nhanvatphu04/Text-Capture.git
cd TextCapture
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

#### 2. VS Code Configuration
```bash
cp .vscode/c_cpp_properties.json.template .vscode/c_cpp_properties.json
```
Then follow the [VS Code Setup Guide](../.vscode/README.md).

#### 3. Build Resources
```bash
python src/utils/compile_resources.py
```

#### 4. Optional: Build C++ Module
```bash
python build_cpp.py
```

### Module Structure

#### Core Modules
- **`src/app.py`**: Application entry point and initialization
- **`src/ui/main_window.py`**: Main window implementation
- **`src/actions/button_actions.py`**: Event handlers for UI actions

#### OCR System
- **`src/ocr/ocr_engine.py`**: Main OCR interface with fallback logic
- **`src/ocr/python_ocr.py`**: Python-based OCR implementation
- **`src/ocr/cpp_ocr.py`**: C++ OCR wrapper
- **`src/ocr/cpp/`**: C++ source code and bindings

#### Utilities
- **`src/utils/resource_loader.py`**: Resource loading and management
- **`src/utils/compile_resources.py`**: Resource compilation utilities

## 🔧 Development Workflow

### Running the Application
```bash
# Development mode
python main.py

# With debug output
python -u main.py
```

### Code Organization

#### Adding New Features
1. **Create feature branch**: `git checkout -b feature/new-feature`
2. **Implement in appropriate module**
3. **Add tests** (if applicable)
4. **Update documentation**
5. **Create pull request**

#### Code Style Guidelines
- **Follow PEP 8** for Python code
- **Use type hints** where appropriate
- **Document functions** with docstrings
- **Keep functions focused** and small
- **Use meaningful variable names**

### Testing

#### Manual Testing
- **Test OCR accuracy** with various image types
- **Verify UI responsiveness** during processing
- **Check error handling** with invalid inputs
- **Test performance** with large images

## 🚀 Performance Optimization

### C++ Module Development

#### Building C++ Module
```bash
# Windows
python build_cpp.py

# Debug build
python build_cpp.py --debug
```

### Memory Management
- **Use context managers** for file operations
- **Release large objects** after use
- **Monitor memory usage** during development
- **Optimize image processing** for large files

### Troubleshooting Development Issues

#### Import Errors
```bash
# Check Python path
python -c "import sys; print(sys.path)"

# Install missing dependencies
pip install -r requirements.txt
```

#### C++ Build Issues
```bash
# Clean build
rm -rf build/ src/Release/

# Rebuild
python build_cpp.py --clean
```

#### Resource Issues
```bash
# Recompile resources
python src/utils/compile_resources.py

# Check resource files
ls -la src/resources_rc.py
```

## 📚 API Reference

### Core Classes

#### OCREngine
```python
class OCREngine:
    def extract_text(self, image_path: str) -> str
    def extract_text_with_confidence(self, image_path: str) -> Dict
    def preprocess_image(self, image_path: str) -> str
    def set_language(self, language: str) -> None
```

#### MainWindow
```python
class MainWindow(QMainWindow):
    def load_image(self, image_path: str) -> None
    def extract_text(self) -> None
    def clear_all(self) -> None
```

### Configuration

#### Environment Variables
- `TESSDATA_PREFIX`: Tesseract data directory
- `DEBUG`: Enable debug output
- `OCR_LANGUAGE`: Default OCR language

#### Configuration Files
- `resources.qrc`: Qt resource definitions
- `style.qss`: Application styling

## 🔄 Continuous Integration

### Pre-commit Checks
```bash
# Code formatting
black src/

# Linting
flake8 src/

# Type checking
mypy src/
```

### Build Verification
```bash
# Test build process
python build_cpp.py --test

# Verify resources
python src/utils/compile_resources.py --verify
```

## 📖 Additional Resources

### Documentation
- **[Architecture Guide](architecture.md)**: Detailed system design
- **[API Reference](api-reference.md)**: Complete API documentation
- **[C++ Module Guide](cpp-module.md)**: C++ implementation details

### External Resources
- **[PySide6 Documentation](https://doc.qt.io/qtforpython/)**
- **[Tesseract Documentation](https://tesseract-ocr.github.io/)**
- **[OpenCV Documentation](https://docs.opencv.org/)**

### Community
- **[GitHub Issues](https://github.com/nhanvatphu04/Text-Capture/issues)**
- **[Discussions](https://github.com/nhanvatphu04/Text-Capture/discussions)**

---

*Happy coding! For questions or contributions, please see our [Contributing Guide](contributing.md).* 