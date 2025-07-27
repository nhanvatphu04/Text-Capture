# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile, QIODevice, QTextStream

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic widgets/form.ui -o widgets/ui_form.py
from widgets.ui_form import Ui_Main

# Import resources to register them with Qt
import rc_resources

class Main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)


def load_stylesheet_from_file():
    """Load and return the stylesheet from style.qss file"""
    try:
        # Look for style.qss in the project root (one directory up from this file)
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        style_file = os.path.join(project_root, "style.qss")
        with open(style_file, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Warning: style.qss file not found in project root")
        return ""
    except Exception as e:
        print(f"Error loading stylesheet: {e}")
        return ""


def load_stylesheet_from_resources():
    """Load and return the stylesheet from resources"""
    try:
        # Load from resources
        file = QFile(":/style.qss")
        if file.open(QIODevice.ReadOnly | QIODevice.Text):
            stream = QTextStream(file)
            stylesheet = stream.readAll()
            file.close()
            return stylesheet
        else:
            print("Warning: Could not open style.qss from resources")
            return ""
    except Exception as e:
        print(f"Error loading stylesheet from resources: {e}")
        return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Apply dark theme stylesheet from resources
    # Fallback to file if resources fail
    stylesheet = load_stylesheet_from_resources()
    if not stylesheet:
        print("Falling back to file-based stylesheet loading...")
        stylesheet = load_stylesheet_from_file()
    
    if stylesheet:
        app.setStyleSheet(stylesheet)
    
    widget = Main()
    widget.show()
    sys.exit(app.exec())
