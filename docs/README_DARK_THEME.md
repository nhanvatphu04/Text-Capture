# Qt Dark Theme Stylesheet

Đây là một stylesheet chủ đề tối hoàn chỉnh cho ứng dụng Qt/PySide6 với thiết kế hiện đại và đẹp mắt.

## Tính năng

- **Chủ đề tối hoàn chỉnh**: Nền tối với text sáng, dễ nhìn và không gây mỏi mắt
- **Hỗ trợ đầy đủ các widget**: Button, Input, ComboBox, List, Tree, Menu, Toolbar, v.v.
- **Hiệu ứng hover và focus**: Tương tác mượt mà với người dùng
- **Thiết kế hiện đại**: Bo góc, shadow, và màu sắc theo chuẩn Material Design
- **Responsive**: Tự động điều chỉnh theo kích thước widget
- **Resources support**: Có thể nhúng stylesheet vào ứng dụng

## Cách sử dụng

### 1. Sử dụng từ file (Development)

Thêm code sau vào file `main.py` của bạn:

```python
import os

def load_stylesheet_from_file():
    """Load and return the stylesheet from style.qss file"""
    try:
        style_file = os.path.join(os.path.dirname(__file__), "style.qss")
        with open(style_file, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Warning: style.qss file not found")
        return ""
    except Exception as e:
        print(f"Error loading stylesheet: {e}")
        return ""

# Trong main function
app = QApplication(sys.argv)

# Apply dark theme stylesheet
stylesheet = load_stylesheet_from_file()
if stylesheet:
    app.setStyleSheet(stylesheet)
```

### 2. Sử dụng từ Resources (Production)

#### Bước 1: Compile Resources
```bash
# Sử dụng script tự động
python compile_resources.py

# Hoặc thủ công
pyside6-rcc resources.qrc -o rc_resources.py
```

#### Bước 2: Sử dụng trong code
```python
from PySide6.QtCore import QFile, QIODevice, QTextStream

def load_stylesheet_from_resources():
    """Load and return the stylesheet from resources"""
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

# Trong main function
app = QApplication(sys.argv)

# Apply dark theme stylesheet from resources
stylesheet = load_stylesheet_from_resources()
if stylesheet:
    app.setStyleSheet(stylesheet)
```

### 3. Fallback Strategy (Recommended)

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

# Trong main function
app = QApplication(sys.argv)
stylesheet = load_stylesheet_with_fallback()
if stylesheet:
    app.setStyleSheet(stylesheet)
```

### 4. Chạy demo

Để xem stylesheet hoạt động với nhiều widget khác nhau:

```bash
python demo_widgets.py
```

### 5. Tùy chỉnh màu sắc

Bạn có thể tùy chỉnh màu sắc trong file `style.qss`:

- `#2b2b2b`: Màu nền chính
- `#1e1e1e`: Màu nền phụ (input fields, menus)
- `#0078d4`: Màu accent (primary buttons, focus)
- `#ffffff`: Màu text chính
- `#555555`: Màu border

## Cấu trúc Project

```
project/
├── main.py                 # Main application
├── style.qss              # Stylesheet file
├── resources.qrc          # Resources configuration
├── compile_resources.py   # Resource compilation script
├── rc_resources.py        # Generated resources (after compilation)
├── demo_widgets.py        # Demo application
├── widgets/
│   ├── form.ui
│   └── ui_form.py
└── README files
```

## Các widget được hỗ trợ

### Basic Widgets
- `QWidget` - Widget cơ bản
- `QPushButton` - Nút bấm (có primary style)
- `QLabel` - Nhãn text
- `QGroupBox` - Nhóm widget

### Input Widgets
- `QLineEdit` - Ô nhập text
- `QTextEdit` - Editor text nhiều dòng
- `QPlainTextEdit` - Editor text đơn giản
- `QComboBox` - Dropdown list
- `QSpinBox` - Spin box số
- `QDoubleSpinBox` - Spin box số thập phân

### Selection Widgets
- `QCheckBox` - Checkbox
- `QRadioButton` - Radio button
- `QSlider` - Thanh trượt
- `QProgressBar` - Thanh tiến trình

### List Widgets
- `QListWidget` - Danh sách
- `QTreeWidget` - Cây dữ liệu
- `QTableWidget` - Bảng dữ liệu

### Navigation Widgets
- `QTabWidget` - Tab container
- `QMenuBar` - Thanh menu
- `QToolBar` - Thanh công cụ
- `QStatusBar` - Thanh trạng thái

### Dialog Widgets
- `QDialog` - Dialog window
- `QMessageBox` - Hộp thoại thông báo
- `QToolTip` - Tooltip

## Tùy chỉnh nâng cao

### Thêm class cho button primary

```python
primary_button = QPushButton("Primary Action")
primary_button.setProperty("class", "primary")
```

### Tùy chỉnh màu sắc cho widget cụ thể

```css
/* Trong style.qss */
QPushButton#customButton {
    background-color: #ff6b6b;
    color: white;
}
```

```python
# Trong Python
custom_button = QPushButton("Custom")
custom_button.setObjectName("customButton")
```

### Thêm file vào resources

```xml
<!-- Trong resources.qrc -->
<RCC>
    <qresource prefix="/">
        <file>style.qss</file>
        <file>images/logo.png</file>
        <file>fonts/custom.ttf</file>
    </qresource>
    <qresource prefix="/themes">
        <file>themes/dark.qss</file>
        <file>themes/light.qss</file>
    </qresource>
</RCC>
```

## Build Process

### Development
```bash
# Chạy trực tiếp với file stylesheet
python main.py
```

### Production
```bash
# 1. Compile resources
python compile_resources.py

# 2. Chạy ứng dụng với resources
python main.py
```

## Lưu ý

1. **Encoding**: Đảm bảo file `style.qss` được lưu với encoding UTF-8
2. **Performance**: Stylesheet được load một lần khi khởi động ứng dụng
3. **Compatibility**: Hoạt động với PySide6 và PyQt6
4. **Customization**: Có thể dễ dàng tùy chỉnh màu sắc và style
5. **Resources**: Sử dụng resources cho production để bảo mật và performance tốt hơn

## Troubleshooting

### Stylesheet không load
- Kiểm tra đường dẫn file `style.qss`
- Đảm bảo file tồn tại và có quyền đọc
- Kiểm tra encoding UTF-8

### Resources không load
- Chạy `python compile_resources.py` để compile resources
- Kiểm tra file `rc_resources.py` đã được tạo
- Đảm bảo import `rc_resources` trong code

### Widget không được style
- Kiểm tra tên class widget trong CSS
- Đảm bảo widget được tạo sau khi áp dụng stylesheet
- Thử restart ứng dụng

### Hiệu ứng không hoạt động
- Kiểm tra cú pháp CSS
- Đảm bảo pseudo-class được viết đúng (hover, focus, pressed)
- Kiểm tra thứ tự CSS rules

## Tài liệu tham khảo

- [RESOURCES_GUIDE.md](RESOURCES_GUIDE.md) - Hướng dẫn chi tiết về Qt Resources
- [Qt Stylesheet Reference](https://doc.qt.io/qt-6/stylesheet-reference.html)
- [PySide6 Documentation](https://doc.qt.io/qtforpython/)

## Tác giả

Stylesheet này được thiết kế để cung cấp trải nghiệm người dùng tốt nhất với chủ đề tối hiện đại cho ứng dụng Qt. 