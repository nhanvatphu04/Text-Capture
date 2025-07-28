"""
Button action handlers
"""

import re
from src.core.async_utils import async_action, safe_ui_update
from PySide6.QtGui import QTextCharFormat, QFont
from PySide6.QtCore import QCoreApplication
from src.ocr import OCREngine


class ButtonActions:
    """Handles all button actions"""

    def __init__(self, main_window):
        self.main_window = main_window
        self.format_states = {
            "underline": False,
            "strikethrough": False,
            "uppercase": False,
            "lowercase": False,
            "sentence_case": False,
        }
        # Initialize default language
        self.current_language = "eng"

    def _get_text_from_editor(self):
        return self.main_window.ui.txtEdit.toPlainText()

    def _set_text_to_editor(self, text):
        self.main_window.ui.txtEdit.setPlainText(text)

    def _set_text_to_editor_safe(self, text):
        """Thread-safe version of _set_text_to_editor"""
        safe_ui_update(self.main_window, "_set_text_to_editor", text)

    def _get_current_image_path(self):
        """Get the current image path from ImageLabel"""
        return (
            self.main_window.ui.lbImageArea.image_path
            if hasattr(self.main_window.ui.lbImageArea, "image_path")
            else None
        )

    def _apply_format_to_selection(self, format_func, format_type=None):
        cursor = self.main_window.ui.txtEdit.textCursor()

        if cursor.hasSelection():
            # Apply format to selected text
            cursor.mergeCharFormat(format_func())
        else:
            # Apply format to entire document
            cursor.select(cursor.SelectionType.Document)
            cursor.mergeCharFormat(format_func())

        # Update state if format_type is provided
        if format_type:
            self.format_states[format_type] = not self.format_states[format_type]
            self._update_button_appearance(format_type)

    def _update_button_appearance(self, format_type):
        button_map = {
            "underline": self.main_window.ui.btnUnderline,
            "strikethrough": self.main_window.ui.btnStrikethrough,
            "uppercase": self.main_window.ui.btnUpperCase,
            "lowercase": self.main_window.ui.btnLowerCase,
            "sentence_case": self.main_window.ui.btnSentenceCase,
        }

        button = button_map.get(format_type)
        if button:
            is_active = self.format_states[format_type]

            # Set CSS class based on button type
            if format_type in ["uppercase", "lowercase", "sentence_case"]:
                button.setProperty("class", "case-toggle")
            elif format_type in ["underline", "strikethrough"]:
                button.setProperty("class", "decorative-toggle")
            else:
                button.setProperty("class", "toggle")

            # Set active state
            button.setProperty("active", "true" if is_active else "false")

            # Apply styles
            button.style().unpolish(button)
            button.style().polish(button)

    def _create_underline_format(self):
        """Create underline format"""
        format = QTextCharFormat()
        format.setFontUnderline(True)
        return format

    def _create_strikethrough_format(self):
        """Create strikethrough format"""
        format = QTextCharFormat()
        format.setFontStrikeOut(True)
        return format

    def _create_uppercase_format(self):
        """Create uppercase format"""
        format = QTextCharFormat()
        format.setFontCapitalization(QFont.Capitalization.AllUppercase)
        return format

    def _create_lowercase_format(self):
        """Create lowercase format"""
        format = QTextCharFormat()
        format.setFontCapitalization(QFont.Capitalization.AllLowercase)
        return format

    def _create_sentence_case_format(self):
        """Create sentence case format"""
        format = QTextCharFormat()
        format.setFontCapitalization(QFont.Capitalization.Capitalize)
        return format

    def _create_normal_format(self):
        """Create normal format (no special formatting)"""
        format = QTextCharFormat()
        format.setFontUnderline(False)
        format.setFontStrikeOut(False)
        format.setFontCapitalization(QFont.Capitalization.MixedCase)
        return format

    def _create_format_without_underline(self):
        """Create format without underline but keep other formatting"""
        format = QTextCharFormat()
        format.setFontUnderline(False)
        return format

    def _create_format_without_strikethrough(self):
        """Create format without strikethrough but keep other formatting"""
        format = QTextCharFormat()
        format.setFontStrikeOut(False)
        return format

    def _create_format_without_case(self):
        """Create format without case formatting but keep other formatting"""
        format = QTextCharFormat()
        format.setFontCapitalization(QFont.Capitalization.MixedCase)
        return format

    def _toggle_case_format(self, format_type, format_func):
        """Toggle case formatting (uppercase, lowercase, sentence_case) - only one active"""
        cursor = self.main_window.ui.txtEdit.textCursor()

        # Turn off all other case formats first
        case_formats = ["uppercase", "lowercase", "sentence_case"]
        for case_format in case_formats:
            if case_format != format_type and self.format_states[case_format]:
                self.format_states[case_format] = False
                self._update_button_appearance(case_format)

        if cursor.hasSelection():
            # Apply to selected text
            if self.format_states[format_type]:
                # Turn off case formatting
                cursor.mergeCharFormat(self._create_format_without_case())
            else:
                # Turn on case formatting
                cursor.mergeCharFormat(format_func())
        else:
            # Apply to entire document
            cursor.select(cursor.SelectionType.Document)
            if self.format_states[format_type]:
                # Turn off case formatting
                cursor.mergeCharFormat(self._create_format_without_case())
            else:
                # Turn on case formatting
                cursor.mergeCharFormat(format_func())

        # Update state
        self.format_states[format_type] = not self.format_states[format_type]
        self._update_button_appearance(format_type)

    def _toggle_decorative_format(self, format_type, format_func, remove_format_func):
        """Toggle decorative formatting (underline, strikethrough) - independent"""
        cursor = self.main_window.ui.txtEdit.textCursor()

        if cursor.hasSelection():
            # Apply to selected text
            if self.format_states[format_type]:
                # Turn off specific formatting
                cursor.mergeCharFormat(remove_format_func())
            else:
                # Turn on specific formatting
                cursor.mergeCharFormat(format_func())
        else:
            # Apply to entire document
            cursor.select(cursor.SelectionType.Document)
            if self.format_states[format_type]:
                # Turn off specific formatting
                cursor.mergeCharFormat(remove_format_func())
            else:
                # Turn on specific formatting
                cursor.mergeCharFormat(format_func())

        # Update state
        self.format_states[format_type] = not self.format_states[format_type]
        self._update_button_appearance(format_type)

    def on_sentence_case_clicked(self):
        """Action for Sentence Case button - Toggle (mutually exclusive)"""
        self._toggle_case_format("sentence_case", self._create_sentence_case_format)

    def on_lower_case_clicked(self):
        """Action for Lower Case button - Toggle (mutually exclusive)"""
        self._toggle_case_format("lowercase", self._create_lowercase_format)

    def on_upper_case_clicked(self):
        """Action for Upper Case button - Toggle (mutually exclusive)"""
        self._toggle_case_format("uppercase", self._create_uppercase_format)

    def on_underline_clicked(self):
        """Action for Underline button - Toggle (independent)"""
        self._toggle_decorative_format(
            "underline",
            self._create_underline_format,
            self._create_format_without_underline,
        )

    def on_strikethrough_clicked(self):
        """Action for Strikethrough button - Toggle (independent)"""
        self._toggle_decorative_format(
            "strikethrough",
            self._create_strikethrough_format,
            self._create_format_without_strikethrough,
        )

    # Action handlers with @async_action (only for truly async operations)
    @async_action
    def on_refresh_clicked(self):
        """Action for Refresh button"""
        # Clear txtEdit content - use thread-safe method
        self._set_text_to_editor_safe("")

        # Clear image in lbImageArea - use thread-safe method
        self._clear_image_safe()

        # Reset all format states
        for format_type in self.format_states:
            self.format_states[format_type] = False
            self._update_button_appearance(format_type)

    def _clear_image_safe(self):
        """Thread-safe method to clear the image"""
        safe_ui_update(self.main_window, "_clear_image_safe")

    def _clear_image(self):
        """Clear the image in lbImageArea"""
        try:
            # Clear the image directly
            self.main_window.ui.lbImageArea.clear()
            self.main_window.ui.lbImageArea.setText(
                QCoreApplication.translate(
                    "Main",
                    '<div style="text-align: center;">\n'
                    '<img src=":/src/resources/images/add_image.png"/>\n'
                    "<br/>\n"
                    '<span style="font-size: 12pt;">K\u00e9o v\u00e0 th\u1ea3 \u1ea3nh v\u00e0o \u0111\u00e2y</span>\n'
                    "</div>",
                    None,
                )
            )
            self.main_window.ui.lbImageArea.image_path = None
        except Exception as e:
            print(f"Error clearing image: {e}")

    @async_action
    def on_get_text_clicked(self):
        """Action for Get Text button"""
        image_path = self._get_current_image_path()
        if not image_path:
            self.main_window.set_status_message("Vui lòng chọn ảnh trước khi thực hiện OCR", "error")
            return

        current_ui_language = self.main_window.ui.cbLanguage.currentText()
        # Mapping cho Tesseract (C++/Python Tesseract)
        tesseract_mapping = {"En": "eng", "Vi": "vie", "Jp": "jpn"}
        # Mapping cho EasyOCR (chuẩn ISO)
        easyocr_mapping = {"En": "en", "Vi": "vi", "Jp": "ja"}
        selected_language_tesseract = tesseract_mapping.get(current_ui_language, "eng")
        selected_language_easyocr = easyocr_mapping.get(current_ui_language, "en")

        # Nếu là tiếng Nhật, ép dùng EasyOCR (Python)
        if selected_language_tesseract == "jpn":
            try:
                print("Forcing EasyOCR for Japanese...")
                ocr_engine = OCREngine(use_cpp=False, language=selected_language_easyocr)
                extracted_text = ocr_engine.extract_text(image_path)
                if extracted_text and extracted_text.strip():
                    print("EasyOCR (Python) successful for Japanese")
                    self._set_text_to_editor_safe(extracted_text)
                    return
                else:
                    print("EasyOCR (Python) returned empty text for Japanese")
                    self._set_text_to_editor_safe("❌ Không thể nhận dạng văn bản tiếng Nhật từ ảnh này.\n\n💡 Gợi ý:\n- Kiểm tra chất lượng ảnh\n- Đảm bảo ảnh có text rõ ràng\n- Thử với ảnh khác")
                    return
            except Exception as e:
                print(f"EasyOCR (Python) failed for Japanese: {e}")
                self._set_text_to_editor_safe(f"❌ EasyOCR lỗi: {str(e)}")
                return

        # Try C++ implementation first, then fallback to Python
        extracted_text = None
        error_message = None
        
        # First attempt: C++ implementation
        try:
            print(f"Attempting C++ OCR with language: {selected_language_tesseract}")
            ocr_engine = OCREngine(use_cpp=True, language=selected_language_tesseract)
            extracted_text = ocr_engine.extract_text(image_path)
            
            if extracted_text and extracted_text.strip():
                print("C++ OCR successful")
                self._set_text_to_editor_safe(extracted_text)
                return
            else:
                print("C++ OCR returned empty text, trying Python fallback...")
                error_message = "C++ OCR không nhận diện được text, đang thử Python..."
                
        except Exception as e:
            print(f"C++ OCR failed: {e}")
            error_message = f"C++ OCR lỗi: {str(e)}, đang thử Python..."
        
        # Second attempt: Python implementation
        try:
            print(f"Attempting Python OCR with language: {selected_language_easyocr}")
            ocr_engine = OCREngine(use_cpp=False, language=selected_language_easyocr)
            extracted_text = ocr_engine.extract_text(image_path)
            
            if extracted_text and extracted_text.strip():
                print("Python OCR successful")
                self._set_text_to_editor_safe(extracted_text)
                return
            else:
                print("Python OCR also returned empty text")
                self._set_text_to_editor_safe("❌ Không thể nhận dạng văn bản từ ảnh này.\n\n💡 Gợi ý:\n- Kiểm tra chất lượng ảnh\n- Đảm bảo ảnh có text rõ ràng\n- Thử với ngôn ngữ khác")
                
        except Exception as e:
            print(f"Python OCR failed: {e}")
            self._set_text_to_editor_safe(f"❌ Cả C++ và Python OCR đều lỗi:\n\nC++: {error_message}\nPython: {str(e)}\n\n💡 Gợi ý:\n- Kiểm tra ảnh có hợp lệ không\n- Thử ảnh khác\n- Kiểm tra cài đặt Tesseract")

    @async_action
    def on_language_changed(self, text=None):
        """Action for Language button"""
        print(f"Language changed to: {text}")

        # Map UI language codes to Tesseract language codes
        language_mapping = {"En": "eng", "Vi": "vie", "Jp": "jpn"}

        # Get the selected language from combo box
        if text is None:
            text = self.main_window.ui.cbLanguage.currentText()

        # Convert to Tesseract language code
        tesseract_language = language_mapping.get(text, "eng")

        # Store current language for OCR operations
        self.current_language = tesseract_language

    @async_action
    def on_upload_clicked(self):
        """Action for Upload button - Upload from device (camera or file)"""

        # Use thread-safe method to show upload menu
        safe_ui_update(self.main_window, "_show_upload_menu")

    def _capture_from_camera(self):
        """Capture image from camera"""
        try:
            # TODO: Implement camera capture
            # For now, show a message
            self._set_text_to_editor_safe(
                "Chức năng chụp ảnh từ camera đang được phát triển..."
            )
        except Exception as e:
            print(f"Error capturing from camera: {e}")
            self._set_text_to_editor_safe(f"Lỗi khi mở camera: {str(e)}")

    def _select_from_device(self):
        """Select image from device storage"""
        try:
            from PySide6.QtWidgets import QFileDialog

            # Open file dialog for image selection
            file_path, _ = QFileDialog.getOpenFileName(
                self.main_window,
                "Chọn ảnh từ thiết bị",
                "",
                "Image Files (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp);;All Files (*)",
            )

            if file_path:
                # Load the selected image into the image area
                self._load_image_to_area(file_path)
            else:
                print("No file selected")

        except Exception as e:
            print(f"Error selecting from device: {e}")
            self._set_text_to_editor_safe(f"Lỗi khi chọn ảnh: {str(e)}")

    def _load_image_to_area(self, image_path):
        """Load image to the image area"""
        try:
            # Use thread-safe method to load image
            safe_ui_update(self.main_window, "_load_image_to_area", image_path)
        except Exception as e:
            print(f"Error loading image to area: {e}")
            self._set_text_to_editor_safe(f"Lỗi khi tải ảnh: {str(e)}")

    def get_current_language_info(self):
        """Get information about current language and supported languages"""
        current_ui_language = self.main_window.ui.cbLanguage.currentText()
        language_mapping = {"En": "eng", "Vi": "vie", "Jp": "jpn"}
        current_language = language_mapping.get(current_ui_language, "eng")

        language_names = {"eng": "English", "vie": "Vietnamese", "jpn": "Japanese"}

        return {
            "ui_language": current_ui_language,
            "tesseract_language": current_language,
            "language_name": language_names.get(current_language, "Unknown"),
            "supported_languages": [
                "English (eng)",
                "Vietnamese (vie)",
                "Japanese (jpn)",
            ],
        }
