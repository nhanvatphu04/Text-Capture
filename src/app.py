"""
Main entry point for the TextCapture application
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))

from PySide6.QtWidgets import QApplication

# Import resources to register them with Qt
import src.resources_rc

# Import ResourceLoader
from src.utils import ResourceLoader

# Import our modular components
from src.ui.main_window import MainWindow


def run_app():
    """Main function to run the application"""
    app = QApplication(sys.argv)

    # Initialize ResourceLoader
    resource_loader = ResourceLoader()

    # Load JetBrains Mono fonts
    loaded_fonts = resource_loader.load_fonts()

    # Apply stylesheet
    stylesheet = resource_loader.load_stylesheet()
    if stylesheet:
        app.setStyleSheet(stylesheet)

    # Create and show main window
    widget = MainWindow()
    widget.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(run_app())
