#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "ocr_engine.h"

namespace py = pybind11;
using namespace textcapture;

PYBIND11_MODULE(cpp_ocr, m) {
    py::class_<OCREngine>(m, "OCREngine")
        .def(py::init<>())
        .def("initialize", &OCREngine::initialize)
        .def("extract_text", &OCREngine::extract_text)
        .def("extract_text_with_confidence", &OCREngine::extract_text_with_confidence)
        .def("preprocess_image", &OCREngine::preprocess_image,
             py::arg("image_path"),
             py::arg("enhance_contrast") = true,
             py::arg("enhance_sharpness") = true,
             py::arg("denoise") = true,
             py::arg("grayscale") = true)
        .def("set_language", &OCREngine::set_language)
        .def("get_supported_languages", &OCREngine::get_supported_languages)
        .def("get_info", &OCREngine::get_info)
        .def("set_tokenizer_service_url", &OCREngine::set_tokenizer_service_url)
        .def("enable_external_tokenizer", &OCREngine::enable_external_tokenizer)
        .def("is_external_tokenizer_available", &OCREngine::is_external_tokenizer_available);
}
