#ifndef OCR_ENGINE_H
#define OCR_ENGINE_H

#include <string>
#include <vector>
#include <memory>
#include <opencv2/opencv.hpp>
#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>

namespace textcapture {

struct OCRResult {
    std::string text;
    double confidence;
    std::vector<std::string> text_parts;
    std::vector<double> confidences;
    std::vector<cv::Rect> bounding_boxes;
};

class OCREngine {
public:
    OCREngine();
    ~OCREngine();
    
    // Initialize the OCR engine
    bool initialize(const std::string& language = "eng");
    
    // Extract text from image
    std::string extract_text(const std::string& image_path);
    
    // Extract text with confidence scores
    OCRResult extract_text_with_confidence(const std::string& image_path);
    
    // Preprocess image for better OCR results
    std::string preprocess_image(const std::string& image_path, 
                                bool enhance_contrast = true,
                                bool enhance_sharpness = true,
                                bool denoise = true,
                                bool grayscale = true);
    
    // Set OCR language
    bool set_language(const std::string& language);
    
    // Get supported languages
    std::vector<std::string> get_supported_languages();
    
    // Get engine information
    std::string get_info() const;

private:
    std::unique_ptr<tesseract::TessBaseAPI> tess_api_;
    std::string current_language_;
    bool initialized_;
    
    // Image preprocessing methods
    cv::Mat enhance_contrast(const cv::Mat& image);
    cv::Mat enhance_sharpness(const cv::Mat& image);
    cv::Mat denoise_image(const cv::Mat& image);
    cv::Mat convert_to_grayscale(const cv::Mat& image);
    
    // Helper methods
    bool save_image(const cv::Mat& image, const std::string& output_path);
    std::string generate_temp_path(const std::string& original_path);
    std::string post_process_text(const std::string& text);
};

} // namespace textcapture

#endif // OCR_ENGINE_H 