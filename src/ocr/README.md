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
5. **vcpkg** (quản lý thư viện C++):
   - Clone vcpkg:
     ```bash
     git clone https://github.com/microsoft/vcpkg.git
     cd vcpkg
     .\bootstrap-vcpkg.bat
     ```
   - Thêm vcpkg vào PATH hoặc dùng đường dẫn đầy đủ tới vcpkg.exe
   - Cài pybind11 qua vcpkg:
     ```bash
     .\vcpkg.exe install pybind11:x64-windows
     ```
   - (Khuyến nghị) Cài tesseract qua vcpkg để có đủ file .lib:
     ```bash
     .\vcpkg.exe install tesseract:x64-windows
     ```

#### Build C++ Module thủ công với vcpkg

1. **Xóa thư mục build cũ (nếu có):**
   - Xóa thư mục `src/ocr/cpp/build/` và `src/Release/Release/` nếu muốn build sạch.
2. **Tạo thư mục build và chuyển vào đó:**
   ```bash
   cd src/ocr/cpp
   mkdir build
   cd build
   ```
3. **Cấu hình CMake với toolchain của vcpkg:**
   ```bash
   cmake .. -DCMAKE_TOOLCHAIN_FILE=C:/Users/<user>/vcpkg/scripts/buildsystems/vcpkg.cmake
   ```
   *(Thay đường dẫn cho đúng với máy của bạn)*
4. **Build module:**
   ```bash
   cmake --build . --config Release
   ```
5. **Kết quả:**
   - File `.pyd` (module Python) sẽ nằm trong `src/Release/Release/`
   - Các file `.lib`, `.exp` sẽ nằm trong `src/ocr/cpp/build/Release/`
   - Các file `.dll` phụ thuộc (OpenCV, Tesseract, v.v.) cần copy vào cùng thư mục `.pyd` nếu chạy thử ngoài IDE.

#### Giải thích các thư mục output
- `src/Release/Release/`: Chứa file module Python `.pyd` để import từ Python.
- `src/ocr/cpp/build/Release/`: Chứa file thư viện `.lib`, `.exp` và các file build trung gian.

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

## Troubleshooting

### C++ Module không build được hoặc script báo không tìm thấy file .pyd
1. Kiểm tra dependencies: `python build_cpp.py`
2. Đảm bảo CMake, compiler, pybind11, OpenCV, Tesseract đã cài đặt đúng (ưu tiên cài qua vcpkg).
3. Kiểm tra đường dẫn toolchain vcpkg khi chạy CMake:
   - Đảm bảo lệnh CMake có tham số `-DCMAKE_TOOLCHAIN_FILE=.../vcpkg.cmake`.
4. Kiểm tra vị trí file output `.pyd`:
   - File `.pyd` sẽ nằm trong `src/Release/Release/` (không phải thư mục gốc project).
   - Nếu script báo không tìm thấy file `.pyd`, hãy sửa lại đường dẫn kiểm tra file output trong `build_cpp.py` cho đúng vị trí thực tế.
5. Nếu build thủ công thành công nhưng script vẫn báo lỗi, hãy kiểm tra lại logic kiểm tra file output trong script.

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