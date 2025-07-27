# TextCapture

A modern desktop application for extracting text from images using OCR (Optical Character Recognition) technology. Built with PySide6 and featuring a sleek dark theme interface.

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

## Screenshots

*Screenshots will be added here showing the application interface*

## Installation

### Prerequisites

1. **Python 3.8+**: Make sure you have Python 3.8 or higher installed
2. **Tesseract OCR**: Install Tesseract OCR engine
   - **Windows**: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd TextCapture
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Compile resources** (if needed):
   ```bash
   python src/utils/compile_resources.py
   ```

## Usage

### Running the Application

```bash
python main.py
```

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

## Project Structure

```
TextCapture/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── resources.qrc          # Qt resource file
├── src/
│   ├── app.py             # Main application logic
│   ├── ui/
│   │   └── main_window.py # Main window implementation
│   ├── actions/
│   │   └── button_actions.py # Button event handlers
│   ├── core/
│   │   └── button_manager.py # Button state management
│   ├── utils/
│   │   ├── css_manager.py     # CSS property management
│   │   ├── resource_loader.py # Resource loading utilities
│   │   └── compile_resources.py # Resource compilation
│   ├── widgets/
│   │   └── mainwindow/
│   │       ├── form.ui        # Qt Designer UI file
│   │       └── ui_form.py     # Generated UI code
│   └── resources/
│       ├── fonts/             # JetBrains Mono font files
│       ├── icons/             # Application icons
│       ├── images/            # UI images
│       └── styles/
│           └── style.qss      # Dark theme stylesheet
└── docs/                     # Documentation
```

## Development

### Building from Source

1. **Install development dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Compile UI files** (if you modify the .ui file):
   ```bash
   pyside6-uic src/widgets/mainwindow/form.ui -o src/widgets/mainwindow/ui_form.py
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
- **python-docx**: Microsoft Word document support

### System Dependencies
- **Tesseract OCR**: OCR engine (must be installed separately)

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

## Roadmap

- [ ] Camera capture functionality
- [ ] Batch processing for multiple images
- [ ] Export to different formats (PDF, DOCX, TXT)
- [ ] Language detection and multi-language support
- [ ] Advanced text formatting options
- [ ] Plugin system for custom OCR engines
