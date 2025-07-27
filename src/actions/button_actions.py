"""
Button action handlers
"""

import time
import re
from src.core.async_utils import async_action, safe_ui_update
from PySide6.QtGui import QTextCharFormat, QFont


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

    # Action handlers with @async_action (only for truly async operations)
    @async_action
    def on_refresh_clicked(self):
        """Action for Refresh button"""
        print("Refreshing...")
        # Clear txtEdit content - use thread-safe method
        self._set_text_to_editor_safe("")

        # Clear image in lbImageArea - use thread-safe method
        self._clear_image_safe()

        # Reset all format states
        for format_type in self.format_states:
            self.format_states[format_type] = False
            self._update_button_appearance(format_type)
        print("Refresh completed")

    def _clear_image_safe(self):
        """Thread-safe method to clear the image"""
        safe_ui_update(self.main_window, "_clear_image")

    def _clear_image(self):
        """Clear the image in lbImageArea"""
        try:
            # Clear the image directly
            self.main_window.ui.lbImageArea.clear()
            self.main_window.ui.lbImageArea.setText(
                "Kéo thả ảnh vào đây<br>hoặc click để chọn file"
            )
            self.main_window.ui.lbImageArea.image_path = None
            print("Image cleared successfully")
        except Exception as e:
            print(f"Error clearing image: {e}")

    @async_action
    def on_get_text_clicked(self):
        """Action for Get Text button"""
        print("Getting text...")

        # Get current image path
        image_path = self._get_current_image_path()
        if image_path:
            print(f"Processing image: {image_path}")
            # TODO: Add actual OCR logic here using image_path
            sample_text = f"Đây là văn bản mẫu được lấy từ ảnh: {image_path}. Văn bản này sẽ được xử lý và định dạng."
        else:
            print("No image selected")
            sample_text = "Vui lòng chọn ảnh trước khi thực hiện OCR"

        # Use thread-safe method to update UI
        self._set_text_to_editor_safe(sample_text)
        print("Get text completed")

    @async_action
    def on_capture_clicked(self):
        """Action for Capture button"""
        print("Capturing...")
        time.sleep(1)  # Simulate capture work
        print("Capture completed")

    @async_action
    def on_upload_clicked(self):
        """Action for Upload button"""
        print("Uploading...")
        time.sleep(1)  # Simulate upload work
        print("Upload completed")

    # Action handlers without @async_action (run in main thread)
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
