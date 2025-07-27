#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include "ocr_engine.h"

namespace py = pybind11;

PYBIND11_MODULE(cpp_ocr, m) {
    m.doc() = "C++ OCR Engine for TextCapture - High performance text extraction using Tesseract and OpenCV";
    
    // OCRResult struct
    py::class_<textcapture::OCRResult>(m, "OCRResult")
        .def_readwrite("text", &textcapture::OCRResult::text)
        .def_readwrite("confidence", &textcapture::OCRResult::confidence)
        .def_readwrite("text_parts", &textcapture::OCRResult::text_parts)
        .def_readwrite("confidences", &textcapture::OCRResult::confidences)
        .def_readwrite("bounding_boxes", &textcapture::OCRResult::bounding_boxes)
        .def("__repr__", [](const textcapture::OCRResult& result) {
            return "OCRResult(text='" + result.text + "', confidence=" + std::to_string(result.confidence) + ")";
        });
    
    // CppOCREngine class
    py::class_<textcapture::OCREngine>(m, "CppOCREngine")
        .def(py::init<>())
        .def("initialize", &textcapture::OCREngine::initialize, 
             py::arg("language") = "eng",
             "Initialize the OCR engine with specified language")
        .def("extract_text", &textcapture::OCREngine::extract_text,
             py::arg("image_path"),
             "Extract text from image file")
        .def("extract_text_with_confidence", &textcapture::OCREngine::extract_text_with_confidence,
             py::arg("image_path"),
             "Extract text with confidence scores from image file")
        .def("preprocess_image", &textcapture::OCREngine::preprocess_image,
             py::arg("image_path"),
             py::arg("enhance_contrast") = true,
             py::arg("enhance_sharpness") = true,
             py::arg("denoise") = true,
             py::arg("grayscale") = true,
             "Preprocess image for better OCR results")
        .def("set_language", &textcapture::OCREngine::set_language,
             py::arg("language"),
             "Set OCR language")
        .def("get_supported_languages", &textcapture::OCREngine::get_supported_languages,
             "Get list of supported languages")
        .def("get_info", &textcapture::OCREngine::get_info,
             "Get engine information")
        .def("__repr__", [](const textcapture::OCREngine& engine) {
            return "CppOCREngine(" + engine.get_info() + ")";
        });
    
    // Module-level functions
    m.def("get_version", []() {
        return "1.0.0";
    }, "Get C++ OCR module version");
    
    m.def("get_dependencies", []() {
        return py::dict(
            py::arg("opencv") = "4.x",
            py::arg("tesseract") = "5.x",
            py::arg("pybind11") = "2.x"
        );
    }, "Get required dependencies");
    
    // Constants
    m.attr("__version__") = "1.0.0";
    m.attr("__author__") = "TextCapture Team";
    m.attr("__description__") = "High-performance C++ OCR engine for text extraction";
} 