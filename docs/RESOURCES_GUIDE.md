# Hướng dẫn sử dụng Resources cho Stylesheet Qt

## Tổng quan

Qt Resources cho phép bạn nhúng file stylesheet vào ứng dụng thay vì phải load từ file system. Điều này có những ưu điểm sau:

- **Bảo mật**: File stylesheet được nhúng vào executable
- **Phân phối dễ dàng**: Không cần lo về đường dẫn file
- **Performance**: Load nhanh hơn từ memory
- **Portability**: Hoạt động trên mọi platform

## Cấu trúc Resources

### 1. File `resources.qrc`

```xml
<RCC>
    <qresource prefix="/">
        <file>style.qss</file>
        <file>images/icon.png</file>
        <file>fonts/custom.ttf</file>
    </qresource>
</RCC>
```

### 2. Compile Resources

Để sử dụng resources, bạn cần compile file `.qrc` thành Python module:

```bash
# Sử dụng pyside6-rcc
pyside6-rcc resources.qrc -o rc_resources.py

# Hoặc sử dụng pyrcc6 (PyQt6)
pyrcc6 resources.qrc -o rc_resources.py
```

### 3. Import Resources

```python
import rc_resources
```

## Cách Load Stylesheet từ Resources

### Method 1: Sử dụng QFile

```python
from PySide6.QtCore import QFile, QIODevice, QTextStream

def load_stylesheet_from_resources():
    """Load stylesheet from resources"""
    try:
        file = QFile(":/style.qss")
        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            stream = QTextStream(file)
            stream.setEncoding(QTextStream.Utf8)
            stylesheet = stream.readAll()
            file.close()
            return stylesheet
        else:
            print("Could not open style.qss from resources")
            return ""
    except Exception as e:
        print(f"Error loading stylesheet: {e}")
        return ""
```

### Method 2: Sử dụng QTextStream trực tiếp

```python
from PySide6.QtCore import QTextStream, QIODevice

def load_stylesheet_simple():
    """Simple method to load stylesheet"""
    file = QFile(":/style.qss")
    if file.open(QIODevice.ReadOnly | QIODevice.Text):
        return QTextStream(file).readAll()
    return ""
```

### Method 3: Sử dụng with statement (Python style)

```python
def load_stylesheet_python_style():
    """Python-style resource loading"""
    file = QFile(":/style.qss")
    if file.open(QIODevice.ReadOnly | QIODevice.Text):
        content = QTextStream(file).readAll()
        file.close()
        return content
    return ""
```

## Fallback Strategy

Để đảm bảo ứng dụng hoạt động ngay cả khi resources không có sẵn:

```python
def load_stylesheet_with_fallback():
    """Load stylesheet with fallback to file"""
    # Try resources first
    stylesheet = load_stylesheet_from_resources()
    
    # Fallback to file if resources fail
    if not stylesheet:
        print("Falling back to file-based loading...")
        stylesheet = load_stylesheet_from_file()
    
    return stylesheet
```

## Cấu trúc Project với Resources

```
project/
├── main.py
├── style.qss
├── resources.qrc
├── rc_resources.py (generated)
├── widgets/
│   ├── form.ui
│   └── ui_form.py
└── README.md
```

## Build Process

### 1. Development (không cần compile resources)

```python
# Trong main.py
def load_stylesheet():
    # Try resources first
    stylesheet = load_stylesheet_from_resources()
    if not stylesheet:
        # Fallback to file
        stylesheet = load_stylesheet_from_file()
    return stylesheet
```

### 2. Production (compile resources)

```bash
# Compile resources
pyside6-rcc resources.qrc -o rc_resources.py

# Import trong main.py
import rc_resources
```

## Ví dụ hoàn chỉnh

### `resources.qrc`
```xml
<RCC>
    <qresource prefix="/">
        <file>style.qss</file>
        <file>images/logo.png</file>
    </qresource>
    <qresource prefix="/themes">
        <file>themes/dark.qss</file>
        <file>themes/light.qss</file>
    </qresource>
</RCC>
```

### `main.py`
```python
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile, QIODevice, QTextStream

def load_stylesheet_from_resources():
    """Load stylesheet from resources"""
    try:
        file = QFile(":/style.qss")
        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            stream = QTextStream(file)
            stream.setEncoding(QTextStream.Utf8)
            stylesheet = stream.readAll()
            file.close()
            return stylesheet
        else:
            print("Could not open style.qss from resources")
            return ""
    except Exception as e:
        print(f"Error loading stylesheet: {e}")
        return ""

def load_stylesheet_from_file():
    """Load stylesheet from file (fallback)"""
    try:
        style_file = os.path.join(os.path.dirname(__file__), "style.qss")
        with open(style_file, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error loading file stylesheet: {e}")
        return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Load stylesheet with fallback
    stylesheet = load_stylesheet_from_resources()
    if not stylesheet:
        stylesheet = load_stylesheet_from_file()
    
    if stylesheet:
        app.setStyleSheet(stylesheet)
    
    # Your main window code here
    sys.exit(app.exec())
```

## Lưu ý quan trọng

### 1. Compile Resources
- Luôn compile resources trước khi deploy
- Sử dụng đúng tool cho version Qt (pyside6-rcc vs pyrcc6)

### 2. Path trong Resources
- Sử dụng `:/` prefix để truy cập resources
- Path phải khớp với cấu trúc trong `.qrc` file

### 3. Encoding
- Luôn set encoding UTF-8 cho text files
- Đảm bảo file `.qss` được save với UTF-8

### 4. Performance
- Resources load nhanh hơn file system
- Memory usage tăng nhẹ do file được nhúng

### 5. Debugging
- Kiểm tra console output để debug resource loading
- Sử dụng fallback strategy để development dễ dàng

## Troubleshooting

### Resources không load
```python
# Kiểm tra file có tồn tại trong resources không
file = QFile(":/style.qss")
print(f"File exists: {file.exists()}")
```

### Encoding issues
```python
# Đảm bảo encoding đúng
stream = QTextStream(file)
stream.setEncoding(QTextStream.Utf8)
```

### Path issues
```python
# Kiểm tra path trong .qrc file
# Đảm bảo path khớp với cấu trúc thư mục
```

## Kết luận

Sử dụng Qt Resources cho stylesheet là best practice cho production applications. Nó cung cấp:

- Bảo mật tốt hơn
- Phân phối dễ dàng
- Performance tốt hơn
- Cross-platform compatibility

Luôn implement fallback strategy để development và debugging dễ dàng hơn. 