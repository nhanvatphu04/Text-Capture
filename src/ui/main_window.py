"""
Main window implementation
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src")
)

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QCoreApplication
from src.widgets.mainwindow.ui_form import Ui_Main

from src.core.button_manager import ButtonManager
from src.actions.button_actions import ButtonActions
from src.utils.css_manager import CSSManager, WidgetStateManager


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic src/widgets/mainwindow/form.ui -o src/widgets/mainwindow/ui_form.py
class MainWindow(QWidget):
    """Main application window"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # Add image_path attribute to the existing QLabel
        self.ui.lbImageArea.image_path = None

        # Initialize state managers
        self.image_area_state = WidgetStateManager(self.ui.lbImageArea)
        self.text_editor_state = WidgetStateManager(self.ui.txtEdit)

        # Add drag & drop event handlers to the existing QLabel
        self.ui.lbImageArea.dragEnterEvent = self._drag_enter_event
        self.ui.lbImageArea.dragLeaveEvent = self._drag_leave_event
        self.ui.lbImageArea.dropEvent = self._drop_event
        self.ui.lbImageArea.mousePressEvent = self._mouse_press_event

        # Add methods to the QLabel
        self.ui.lbImageArea.load_image = self._load_image
        self.ui.lbImageArea.clear_image = self._clear_image_impl

        # Initialize components
        self.buttons = self._gather_buttons()
        self.button_manager = ButtonManager(self.buttons)
        self.button_actions = ButtonActions(self)
        self.action_thread = None

        # Setup connections
        self._setup_button_connections()

    def _drag_enter_event(self, event):
        """Handle drag enter event"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.image_area_state.set_drag_over_state(True)
        else:
            event.ignore()

    def _drag_leave_event(self, event):
        """Handle drag leave event"""
        self.image_area_state.set_drag_over_state(False)

    def _drop_event(self, event):
        """Handle drop event"""
        self.image_area_state.set_drag_over_state(False)

        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                if self._is_valid_image_file(file_path):
                    self._load_image(file_path)
                    event.acceptProposedAction()
                else:
                    print(f"Invalid image file: {file_path}")
                    self.image_area_state.set_error_state(True)
        else:
            event.ignore()

    def _mouse_press_event(self, event):
        """Handle mouse press event for file selection"""
        if event.button() == Qt.MouseButton.LeftButton:
            file_path, _ = QFileDialog.getOpenFileName(
                self.ui.lbImageArea,
                "Chọn ảnh",
                "",
                "Image Files (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp)",
            )
            if file_path:
                self._load_image(file_path)

    def _is_valid_image_file(self, file_path):
        """Check if the file is a valid image"""
        if not os.path.exists(file_path):
            return False

        # Check file extension
        valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"]
        file_ext = os.path.splitext(file_path)[1].lower()
        return file_ext in valid_extensions

    def _load_image(self, image_path):
        """Load and display an image"""
        try:
            # Set loading state
            self.image_area_state.set_loading_state(True)
            
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                # Scale pixmap to fit the label while maintaining aspect ratio
                scaled_pixmap = pixmap.scaled(
                    self.ui.lbImageArea.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
                self.ui.lbImageArea.setPixmap(scaled_pixmap)
                self.ui.lbImageArea.image_path = image_path
                
                # Set success state briefly
                self.image_area_state.set_loading_state(False)
                self.image_area_state.set_success_state(True)
                
                print(f"Image loaded successfully: {image_path}")
                
                # Clear success state after 2 seconds
                from PySide6.QtCore import QTimer
                QTimer.singleShot(2000, lambda: self.image_area_state.set_success_state(False))
            else:
                print(f"Failed to load image: {image_path}")
                self.image_area_state.set_loading_state(False)
                self.image_area_state.set_error_state(True)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.image_area_state.set_loading_state(False)
            self.image_area_state.set_error_state(True)

    def _clear_image_impl(self):
        """Clear the image and reset to default state"""
        self.ui.lbImageArea.clear()
        self.ui.lbImageArea.setText(
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
        self.ui.lbImageArea.image_path = None
        
        # Reset all states
        self.image_area_state.reset_to_default()

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

    def set_editor_processing(self, processing=True):
        """Set processing state for text editor"""
        self.text_editor_state.set_processing_state(processing)

    def set_editor_readonly(self, readonly=True):
        """Set readonly state for text editor"""
        self.text_editor_state.set_readonly_state(readonly)

    def set_button_processing(self, button, processing=True):
        """Set processing state for a specific button"""
        CSSManager.set_property(button, "processing", processing)

    def set_status_message(self, message, status_type="info"):
        """Set status message with appropriate styling"""
        # You can add a status label to your UI and use this method
        # For now, we'll just print the message
        print(f"[{status_type.upper()}] {message}")

    def get_image_area_state(self):
        """Get current state of image area"""
        return self.image_area_state.get_current_state()

    def get_text_editor_state(self):
        """Get current state of text editor"""
        return self.text_editor_state.get_current_state()

    def _clear_image_safe(self):
        """Thread-safe method to clear the image"""
        if hasattr(self.ui.lbImageArea, "clear_image"):
            self.ui.lbImageArea.clear_image()
        else:
            # Fallback: reset to default state
            self.ui.lbImageArea.clear()
            self.ui.lbImageArea.setText(
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
            self.ui.lbImageArea.image_path = None
            
            # Reset CSS properties
            self.image_area_state.reset_to_default()

    def _load_image_to_area(self, image_path):
        """Thread-safe method to load image to the image area"""
        if hasattr(self.ui.lbImageArea, "load_image"):
            self.ui.lbImageArea.load_image(image_path)
        else:
            # Fallback: load image directly
            try:
                from PySide6.QtGui import QPixmap
                from PySide6.QtCore import Qt

                # Set loading state
                self.image_area_state.set_loading_state(True)
                
                pixmap = QPixmap(image_path)
                if not pixmap.isNull():
                    # Scale pixmap to fit the label while maintaining aspect ratio
                    scaled_pixmap = pixmap.scaled(
                        self.ui.lbImageArea.size(),
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation,
                    )
                    self.ui.lbImageArea.setPixmap(scaled_pixmap)
                    self.ui.lbImageArea.image_path = image_path
                    
                    # Set success state briefly
                    self.image_area_state.set_loading_state(False)
                    self.image_area_state.set_success_state(True)
                    
                    print(f"Image loaded successfully: {image_path}")
                    
                    # Clear success state after 2 seconds
                    from PySide6.QtCore import QTimer
                    QTimer.singleShot(2000, lambda: self.image_area_state.set_success_state(False))
                else:
                    print(f"Failed to load image: {image_path}")
                    self.image_area_state.set_loading_state(False)
                    self.image_area_state.set_error_state(True)
            except Exception as e:
                print(f"Error loading image: {e}")
                self.image_area_state.set_loading_state(False)
                self.image_area_state.set_error_state(True)

    def _show_upload_menu(self):
        """Show upload menu on main thread"""
        try:
            from PySide6.QtWidgets import QMenu
            from PySide6.QtCore import QPoint

            # Create context menu for upload options
            menu = QMenu()
            camera_action = menu.addAction("📷 Chụp ảnh từ camera")
            file_action = menu.addAction("📁 Chọn ảnh từ thiết bị")
            menu.addSeparator()
            cancel_action = menu.addAction("❌ Hủy")

            # Get button reference directly
            button = self.ui.btnUpload
            if button:
                # Show menu at button position
                pos = button.mapToGlobal(QPoint(0, button.height()))
                action = menu.exec(pos)

                if action == camera_action:
                    self._handle_camera_capture()
                elif action == file_action:
                    self._handle_file_selection()
                elif action == cancel_action:
                    print("Upload cancelled")
            else:
                # Fallback: show file dialog directly
                self._handle_file_selection()

        except Exception as e:
            print(f"Error showing upload menu: {e}")
            # Fallback: show file dialog directly
            self._handle_file_selection()

    def _handle_camera_capture(self):
        """Handle camera capture selection"""
        try:
            # TODO: Implement camera capture
            # For now, show a message
            self.ui.txtEdit.setPlainText(
                "Chức năng chụp ảnh từ camera đang được phát triển..."
            )
        except Exception as e:
            print(f"Error capturing from camera: {e}")
            self.ui.txtEdit.setPlainText(f"Lỗi khi mở camera: {str(e)}")

    def _handle_file_selection(self):
        """Handle file selection"""
        try:
            from PySide6.QtWidgets import QFileDialog

            # Open file dialog for image selection
            file_path, _ = QFileDialog.getOpenFileName(
                self,
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
            self.ui.txtEdit.setPlainText(f"Lỗi khi chọn ảnh: {str(e)}")

    def disable_other_buttons(self, active_button):
        """Delegate to button manager"""
        self.button_manager.disable_other_buttons(active_button)

    def on_action_finished(self):
        """Delegate to button manager"""
        self.button_manager.on_action_finished()
