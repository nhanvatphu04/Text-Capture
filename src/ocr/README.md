# OCR Module - TextCapture

Module OCR cho ứng dụng TextCapture với hỗ trợ cả Python và C++ implementations.

## Tính năng

### 🔧 Hỗ trợ đa nền tảng
- **Python Implementation**: Sử dụng EasyOCR và Tesseract
- **C++ Implementation**: Hiệu suất cao với OpenCV và Tesseract
- **Tự động fallback**: Tự động chuyển sang Python nếu C++ không khả dụng

### 📝 Xử lý văn bản
- **Đa ngôn ngữ**: Hỗ trợ tiếng Việt, tiếng Anh, tiếng Trung, tiếng Nhật, v.v.
- **Độ chính xác cao**: Preprocessing ảnh nâng cao
- **Confidence scores**: Đánh giá độ tin cậy của kết quả

### 🖼️ Xử lý ảnh
- **Preprocessing**: Tăng độ tương phản, làm sắc nét, khử nhiễu
- **Deskewing**: Tự động căn chỉnh ảnh nghiêng
- **Binarization**: Chuyển đổi ảnh đen trắng
- **Resize**: Thay đổi kích thước ảnh

## Cài đặt

### Python Dependencies

```bash
pip install -r requirements.txt
```

### C++ Dependencies (Tùy chọn - cho hiệu suất cao)

#### Windows
1. **Visual Studio**: Cài đặt Visual Studio 2019 hoặc mới hơn
2. **CMake**: Tải từ https://cmake.org/download/
3. **OpenCV**: Tải từ https://opencv.org/releases/
4. **Tesseract**: Tải từ https://github.com/UB-Mannheim/tesseract/wiki

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install build-essential cmake
sudo apt-get install libopencv-dev
sudo apt-get install tesseract-ocr libtesseract-dev
```

#### macOS
```bash
brew install cmake
brew install opencv
brew install tesseract
```

### Build C++ Module

```bash
python build_cpp.py
```

## Sử dụng

### Cơ bản

```python
from src.ocr import OCREngine

# Khởi tạo OCR engine (tự động chọn C++ hoặc Python)
ocr = OCREngine(use_cpp=True, language='vie')

# Trích xuất văn bản
text = ocr.extract_text('path/to/image.jpg')
print(text)
```

### Nâng cao

```python
from src.ocr import OCREngine, ImageProcessor

# Khởi tạo image processor
processor = ImageProcessor()

# Preprocess ảnh
processed_path = processor.preprocess_image(
    'path/to/image.jpg',
    enhance_contrast=True,
    enhance_sharpness=True,
    denoise=True,
    deskew=True
)

# OCR với confidence scores
ocr = OCREngine(use_cpp=True, language='vie')
result = ocr.extract_text_with_confidence(processed_path)

print(f"Text: {result['text']}")
print(f"Confidence: {result['confidence']:.2f}")
```

### Kiểm tra implementation

```python
from src.ocr import OCREngine

ocr = OCREngine(use_cpp=True)
info = ocr.get_implementation_info()

print(f"Using C++: {info['using_cpp']}")
print(f"C++ Available: {info['cpp_available']}")
print(f"Engine Type: {info['engine_type']}")
```

## Cấu trúc thư mục

```
src/ocr/
├── __init__.py              # Module entry point
├── ocr_engine.py            # Main OCR engine interface
├── python_ocr.py            # Python implementation
├── cpp_ocr.py               # C++ wrapper
├── image_processor.py       # Image preprocessing
├── cpp/                     # C++ source code
│   ├── CMakeLists.txt       # CMake configuration
│   ├── ocr_engine.h         # C++ header
│   ├── ocr_engine.cpp       # C++ implementation
│   └── cpp_ocr.cpp          # Python bindings
└── README.md                # This file
```

## API Reference

### OCREngine

#### Constructor
```python
OCREngine(use_cpp=True, language='eng', **kwargs)
```

#### Methods
- `extract_text(image_path, **kwargs) -> str`
- `extract_text_with_confidence(image_path, **kwargs) -> dict`
- `preprocess_image(image_path, **kwargs) -> str`
- `set_language(language)`
- `get_supported_languages() -> list`
- `get_implementation_info() -> dict`

### ImageProcessor

#### Constructor
```python
ImageProcessor(use_opencv=True, use_pil=True, **kwargs)
```

#### Methods
- `preprocess_image(image_path, **kwargs) -> str`
- `get_available_methods() -> dict`
- `get_default_settings() -> dict`

## Preprocessing Options

### Cơ bản
- `enhance_contrast`: Tăng độ tương phản
- `enhance_sharpness`: Làm sắc nét
- `denoise`: Khử nhiễu
- `grayscale`: Chuyển đen trắng

### Nâng cao
- `deskew`: Tự động căn chỉnh
- `remove_noise`: Loại bỏ nhiễu
- `binarize`: Chuyển nhị phân
- `resize`: Thay đổi kích thước
- `resize_factor`: Hệ số thay đổi kích thước

## Ngôn ngữ hỗ trợ

### Cơ bản
- `eng`: Tiếng Anh
- `vie`: Tiếng Việt
- `chi_sim`: Tiếng Trung giản thể
- `chi_tra`: Tiếng Trung phồn thể

### Mở rộng
- `jpn`: Tiếng Nhật
- `kor`: Tiếng Hàn
- `tha`: Tiếng Thái
- `ara`: Tiếng Ả Rập
- `hin`: Tiếng Hindi

## Troubleshooting

### C++ Module không build được
1. Kiểm tra dependencies: `python build_cpp.py`
2. Đảm bảo CMake và compiler đã cài đặt
3. Kiểm tra đường dẫn OpenCV và Tesseract

### OCR không nhận dạng được
1. Thử preprocessing ảnh trước
2. Kiểm tra chất lượng ảnh
3. Thử ngôn ngữ khác
4. Kiểm tra confidence scores

### Performance
- C++ implementation nhanh hơn 2-5x so với Python
- Sử dụng preprocessing để tăng độ chính xác
- Batch processing cho nhiều ảnh

## Contributing

1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Tạo Pull Request

## License

MIT License - xem file LICENSE để biết thêm chi tiết. 