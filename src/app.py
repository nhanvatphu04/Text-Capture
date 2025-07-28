"""
Main entry point for the TextCapture application
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))

from PySide6.QtWidgets import QApplication
from src.utils import ResourceLoader
from src.ui.main_window import MainWindow


def run_app():
    """Main function to run the application"""
    app = QApplication(sys.argv)
    
    resource_loader = ResourceLoader()

    stylesheet = resource_loader.load_stylesheet()
    if stylesheet:
        app.setStyleSheet(stylesheet)

    # Create and show main window
    widget = MainWindow()
    widget.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(run_app())
