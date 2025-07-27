"""
Button action handlers
"""
import time
from src.core.async_utils import async_action


class ButtonActions:
    """Handles all button actions"""
    
    def __init__(self, main_window):
        self.main_window = main_window

    # Các action handlers với decorator @async_action
    @async_action
    def on_refresh_clicked(self):
        """Action cho button Refresh"""
        print("Refreshing...")
        time.sleep(2)  # Simulate work
        print("Refresh completed")

    @async_action
    def on_get_text_clicked(self):
        """Action cho button Get Text"""
        print("Getting text...")
        time.sleep(1.5)  # Simulate work
        print("Get text completed")

    @async_action
    def on_capture_clicked(self):
        """Action cho button Capture"""
        print("Capturing...")
        time.sleep(2.5)  # Simulate work
        print("Capture completed")

    @async_action
    def on_upload_clicked(self):
        """Action cho button Upload"""
        print("Uploading...")
        time.sleep(3)  # Simulate work
        print("Upload completed")

    @async_action
    def on_sentence_case_clicked(self):
        """Action cho button Sentence Case"""
        print("Converting to sentence case...")
        time.sleep(1)  # Simulate work
        print("Sentence case conversion completed")

    @async_action
    def on_lower_case_clicked(self):
        """Action cho button Lower Case"""
        print("Converting to lower case...")
        time.sleep(1)  # Simulate work
        print("Lower case conversion completed")

    @async_action
    def on_upper_case_clicked(self):
        """Action cho button Upper Case"""
        print("Converting to upper case...")
        time.sleep(1)  # Simulate work
        print("Upper case conversion completed")

    @async_action
    def on_underline_clicked(self):
        """Action cho button Underline"""
        print("Applying underline...")
        time.sleep(1)  # Simulate work
        print("Underline applied")

    @async_action
    def on_strikethrough_clicked(self):
        """Action cho button Strikethrough"""
        print("Applying strikethrough...")
        time.sleep(1)  # Simulate work
        print("Strikethrough applied") 