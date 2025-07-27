"""
Main window implementation
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src")
)

from PySide6.QtWidgets import QWidget
from src.widgets.mainwindow.ui_form import Ui_Main

from src.core.button_manager import ButtonManager
from src.actions.button_actions import ButtonActions


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic src/widgets/mainwindow/form.ui -o src/widgets/mainwindow/ui_form.py
class MainWindow(QWidget):
    """Main application window"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # Initialize components
        self.buttons = self._gather_buttons()
        self.button_manager = ButtonManager(self.buttons)
        self.button_actions = ButtonActions(self)
        self.action_thread = None

        # Setup connections
        self._setup_button_connections()

    def _gather_buttons(self):
        """Gather all buttons from UI"""
        buttons = [
            self.ui.btnRefresh,
            self.ui.btnGetText,
            self.ui.btnCapture,
            self.ui.btnUpload,
            self.ui.btnSentenceCase,
            self.ui.btnLowerCase,
            self.ui.btnUpperCase,
            self.ui.btnUnderline,
            self.ui.btnStrikethrough,
        ]
        return buttons

    def _setup_button_connections(self):
        """Set up connections for all buttons"""
        self.ui.btnRefresh.clicked.connect(self.button_actions.on_refresh_clicked)
        self.ui.btnGetText.clicked.connect(self.button_actions.on_get_text_clicked)
        self.ui.btnCapture.clicked.connect(self.button_actions.on_capture_clicked)
        self.ui.btnUpload.clicked.connect(self.button_actions.on_upload_clicked)
        self.ui.btnSentenceCase.clicked.connect(
            self.button_actions.on_sentence_case_clicked
        )
        self.ui.btnLowerCase.clicked.connect(self.button_actions.on_lower_case_clicked)
        self.ui.btnUpperCase.clicked.connect(self.button_actions.on_upper_case_clicked)
        self.ui.btnUnderline.clicked.connect(self.button_actions.on_underline_clicked)
        self.ui.btnStrikethrough.clicked.connect(
            self.button_actions.on_strikethrough_clicked
        )

    def _set_text_to_editor(self, text):
        """Thread-safe method to set text in the editor"""
        self.ui.txtEdit.setPlainText(text)

    def _clear_image(self):
        """Thread-safe method to clear the image"""
        if hasattr(self.ui.lbImageArea, "clear_image"):
            self.ui.lbImageArea.clear_image()
        else:
            # Fallback: reset to default state
            self.ui.lbImageArea.clear()
            self.ui.lbImageArea.setText(
                "Kéo thả ảnh vào đây<br>hoặc click để chọn file"
            )
            self.ui.lbImageArea.image_path = None

    def disable_other_buttons(self, active_button):
        """Delegate to button manager"""
        self.button_manager.disable_other_buttons(active_button)

    def on_action_finished(self):
        """Delegate to button manager"""
        self.button_manager.on_action_finished()
