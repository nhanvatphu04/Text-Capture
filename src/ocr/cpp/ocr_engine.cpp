#include "ocr_engine.h"
#include <iostream>
#include <fstream>
#include <filesystem>
#include <algorithm>
#include <sstream>

namespace textcapture {

OCREngine::OCREngine() : initialized_(false) {
    tess_api_ = std::make_unique<tesseract::TessBaseAPI>();
}

OCREngine::~OCREngine() {
    if (tess_api_) {
        tess_api_->End();
    }
}

bool OCREngine::initialize(const std::string& language) {
    try {
        // Initialize Tesseract
        if (tess_api_->Init(nullptr, language.c_str())) {
            std::cerr << "Failed to initialize Tesseract with language: " << language << std::endl;
            return false;
        }
        
        // Set OCR parameters for better accuracy and word separation
        tess_api_->SetPageSegMode(tesseract::PSM_AUTO);
        tess_api_->SetVariable("tessedit_char_whitelist", "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵýỷỹ.,!?;:()[]{}\"'`~@#$%^&*+-=_|\\/<>");
        
        // Improve word separation
        tess_api_->SetVariable("preserve_interword_spaces", "1");
        tess_api_->SetVariable("tessedit_do_invert", "0");
        tess_api_->SetVariable("textord_heavy_nr", "1");
        tess_api_->SetVariable("textord_min_linesize", "2.0");
        
        current_language_ = language;
        initialized_ = true;
        
        std::cout << "Tesseract initialized successfully with language: " << language << std::endl;
        return true;
        
    } catch (const std::exception& e) {
        std::cerr << "Exception during Tesseract initialization: " << e.what() << std::endl;
        return false;
    }
}

std::string OCREngine::extract_text(const std::string& image_path) {
    if (!initialized_) {
        throw std::runtime_error("OCR engine not initialized");
    }
    
    try {
        // Load image using OpenCV
        cv::Mat image = cv::imread(image_path);
        if (image.empty()) {
            throw std::runtime_error("Failed to load image: " + image_path);
        }
        
        std::cout << "Image loaded successfully: " << image.cols << "x" << image.rows << " channels: " << image.channels() << std::endl;
        
        // Preprocess image with improved approach for better word separation
        cv::Mat preprocessed = image.clone();
        preprocessed = convert_to_grayscale(preprocessed);
        
        if (current_language_ == "jpn") {
            // Simplify pipeline for Japanese: only grayscale + Otsu threshold
            cv::threshold(preprocessed, preprocessed, 0, 255, cv::THRESH_BINARY + cv::THRESH_OTSU);
            std::cout << "[JPN] Simple grayscale + Otsu threshold pipeline applied" << std::endl;
        } else {
            // Old pipeline for other languages
            cv::Mat enhanced = enhance_contrast(preprocessed);
            cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(1, 1));
            cv::Mat eroded;
            cv::erode(enhanced, eroded, kernel, cv::Point(-1, -1), 1);
            cv::Mat binary;
            cv::threshold(eroded, binary, 0, 255, cv::THRESH_BINARY + cv::THRESH_OTSU);
            cv::Mat kernel2 = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(2, 1));
            cv::Mat dilated;
            cv::dilate(binary, dilated, kernel2, cv::Point(-1, -1), 1);
            preprocessed = dilated;
        }
        
        std::cout << "Image preprocessed successfully with adaptive thresholding" << std::endl;
        
        // Set image for Tesseract
        tess_api_->SetImage(preprocessed.data, preprocessed.cols, preprocessed.rows, 
                           preprocessed.channels(), preprocessed.step);
        
        // Check if image was set correctly (no need to check GetImage as it's not available)
        std::cout << "Image dimensions: " << preprocessed.cols << "x" << preprocessed.rows << std::endl;
        
        std::cout << "Image set for Tesseract successfully" << std::endl;
        
        // Extract text
        char* text = tess_api_->GetUTF8Text();
        if (!text) {
            throw std::runtime_error("Tesseract returned null text");
        }
        
        std::string result(text);
        delete[] text;
        
        // Check if text is empty or contains only whitespace
        if (result.empty() || result.find_first_not_of(" \t\n\r") == std::string::npos) {
            std::cout << "Empty page!!" << std::endl;
            return "";
        }
        
        // Post-process text to improve word separation
        result = post_process_text(result);
        
        std::cout << "Text extracted successfully, length: " << result.length() << std::endl;
        return result;
        
    } catch (const std::exception& e) {
        throw std::runtime_error("Text extraction failed: " + std::string(e.what()));
    }
}

OCRResult OCREngine::extract_text_with_confidence(const std::string& image_path) {
    if (!initialized_) {
        throw std::runtime_error("OCR engine not initialized");
    }
    
    OCRResult result;
    
    try {
        // Load image using OpenCV
        cv::Mat image = cv::imread(image_path);
        if (image.empty()) {
            throw std::runtime_error("Failed to load image: " + image_path);
        }
        
        // Preprocess image
        cv::Mat preprocessed = image.clone();
        preprocessed = convert_to_grayscale(preprocessed);
        preprocessed = enhance_contrast(preprocessed);
        preprocessed = enhance_sharpness(preprocessed);
        preprocessed = denoise_image(preprocessed);
        
        // Set image for Tesseract
        tess_api_->SetImage(preprocessed.data, preprocessed.cols, preprocessed.rows, 
                           preprocessed.channels(), preprocessed.step);
        
        // Get text with confidence
        char* text = tess_api_->GetUTF8Text();
        result.text = std::string(text);
        delete[] text;
        
        // Get confidence scores
        int* word_count = tess_api_->AllWordConfidences();
        
        if (word_count) {
            for (int i = 0; i < *word_count; ++i) {
                result.confidences.push_back(static_cast<double>(word_count[i]));
            }
            delete[] word_count;
        }
        
        // Calculate average confidence
        if (!result.confidences.empty()) {
            double sum = 0.0;
            for (double conf : result.confidences) {
                sum += conf;
            }
            result.confidence = sum / result.confidences.size();
        } else {
            result.confidence = 0.0;
        }
        
        // Split text into parts
        std::istringstream iss(result.text);
        std::string word;
        while (iss >> word) {
            result.text_parts.push_back(word);
        }
        
    } catch (const std::exception& e) {
        throw std::runtime_error("Text extraction with confidence failed: " + std::string(e.what()));
    }
    
         return result;
 }

std::string OCREngine::preprocess_image(const std::string& image_path, 
                                       bool enhance_contrast,
                                       bool enhance_sharpness,
                                       bool denoise,
                                       bool grayscale) {
    try {
        // Load image
        cv::Mat image = cv::imread(image_path);
        if (image.empty()) {
            throw std::runtime_error("Failed to load image: " + image_path);
        }
        
        // Apply preprocessing
        cv::Mat processed = image.clone();
        
        if (grayscale) {
            processed = convert_to_grayscale(processed);
        }
        
        if (enhance_contrast) {
            processed = this->enhance_contrast(processed);
        }
        
        if (enhance_sharpness) {
            processed = this->enhance_sharpness(processed);
        }
        
        if (denoise) {
            processed = this->denoise_image(processed);
        }
        
        // Save preprocessed image
        std::string output_path = generate_temp_path(image_path);
        if (!save_image(processed, output_path)) {
            throw std::runtime_error("Failed to save preprocessed image");
        }
        
        return output_path;
        
    } catch (const std::exception& e) {
        throw std::runtime_error("Image preprocessing failed: " + std::string(e.what()));
    }
}

bool OCREngine::set_language(const std::string& language) {
    try {
        // End current API
        if (tess_api_) {
            tess_api_->End();
        }
        
        // Reinitialize with new language
        return initialize(language);
        
    } catch (const std::exception& e) {
        std::cerr << "Failed to set language: " << e.what() << std::endl;
        return false;
    }
}

std::vector<std::string> OCREngine::get_supported_languages() {
    std::vector<std::string> languages = {
        "eng", "vie", "chi_sim", "chi_tra", "jpn", "kor", "tha", "ara", "hin"
    };
    return languages;
}

std::string OCREngine::get_info() const {
    std::ostringstream oss;
    oss << "C++ OCR Engine (Tesseract + OpenCV)\n";
    oss << "Initialized: " << (initialized_ ? "Yes" : "No") << "\n";
    oss << "Language: " << current_language_ << "\n";
    oss << "Tesseract Version: " << (tess_api_ ? tess_api_->Version() : "Unknown") << "\n";
    return oss.str();
}

// Private methods

cv::Mat OCREngine::enhance_contrast(const cv::Mat& image) {
    cv::Mat enhanced;
    double alpha = 1.5; // Contrast control
    int beta = 10;      // Brightness control
    
    image.convertTo(enhanced, -1, alpha, beta);
    return enhanced;
}

cv::Mat OCREngine::enhance_sharpness(const cv::Mat& image) {
    cv::Mat kernel = (cv::Mat_<float>(3, 3) << 
        0, -1, 0,
        -1, 5, -1,
        0, -1, 0);
    
    cv::Mat sharpened;
    cv::filter2D(image, sharpened, -1, kernel);
    return sharpened;
}

cv::Mat OCREngine::denoise_image(const cv::Mat& image) {
    cv::Mat denoised;
    cv::medianBlur(image, denoised, 3);
    return denoised;
}

cv::Mat OCREngine::convert_to_grayscale(const cv::Mat& image) {
    if (image.channels() == 1) {
        return image.clone();
    }
    
    cv::Mat grayscale;
    cv::cvtColor(image, grayscale, cv::COLOR_BGR2GRAY);
    return grayscale;
}

bool OCREngine::save_image(const cv::Mat& image, const std::string& output_path) {
    try {
        return cv::imwrite(output_path, image);
    } catch (const std::exception& e) {
        std::cerr << "Failed to save image: " << e.what() << std::endl;
        return false;
    }
}

std::string OCREngine::generate_temp_path(const std::string& original_path) {
    std::filesystem::path path(original_path);
    std::string stem = path.stem().string();
    std::string extension = path.extension().string();
    
    // Create temp directory if it doesn't exist
    std::filesystem::path temp_dir = std::filesystem::temp_directory_path() / "textcapture";
    std::filesystem::create_directories(temp_dir);
    
    // Generate unique filename
    std::string temp_filename = stem + "_preprocessed" + extension;
    return (temp_dir / temp_filename).string();
}

std::string OCREngine::post_process_text(const std::string& text) {
    std::string result = text;
    
    // Add spaces between consecutive uppercase letters followed by lowercase
    for (size_t i = 1; i < result.length() - 1; ++i) {
        if (std::isupper(result[i-1]) && std::isupper(result[i]) && std::islower(result[i+1])) {
            result.insert(i, " ");
            i++; // Skip the inserted space
        }
    }
    
    // Clean up multiple spaces
    std::string::iterator new_end = std::unique(result.begin(), result.end(),
        [](char a, char b) { return a == ' ' && b == ' '; });
    result.erase(new_end, result.end());
    
    return result;
}

} // namespace textcapture 