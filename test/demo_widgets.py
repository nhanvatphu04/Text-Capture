# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QPushButton, QLineEdit, QTextEdit, 
                               QComboBox, QCheckBox, QRadioButton, QSlider, 
                               QProgressBar, QLabel, QGroupBox, QTabWidget,
                               QListWidget, QSpinBox, QMenuBar, QStatusBar,
                               QToolBar, QMessageBox)
from PySide6.QtCore import Qt, QTimer, QFile, QIODevice, QTextStream
from PySide6.QtGui import QAction, QFontDatabase

# Import resources to register them with Qt
# Add parent directory to path to import rc_resources
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import src.resources_rc

def load_stylesheet_from_file():
    """Load and return the stylesheet from style.qss file"""
    try:
        # Look for style.qss in the project root (one directory up from this file)
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        style_file = os.path.join(project_root, "src", "resources", "styles", "style.qss")
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
        file = QFile(":/src/resources/styles/style.qss")
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


def load_fonts_from_resources():
    """Load JetBrains Mono fonts from resources"""
    font_files = [
        ":/src/resources/fonts/JetBrainsMono-Regular.ttf",
        ":/src/resources/fonts/JetBrainsMono-Bold.ttf",
        ":/src/resources/fonts/JetBrainsMono-Italic.ttf",
        ":/src/resources/fonts/JetBrainsMono-Light.ttf",
        ":/src/resources/fonts/JetBrainsMono-Medium.ttf"
    ]
    
    font_db = QFontDatabase()
    loaded_fonts = []
    
    for font_file in font_files:
        try:
            font_id = font_db.addApplicationFont(font_file)
            if font_id != -1:
                font_families = font_db.applicationFontFamilies(font_id)
                loaded_fonts.extend(font_families)
                print(f"Loaded font: {font_families}")
            else:
                print(f"Failed to load font: {font_file}")
        except Exception as e:
            print(f"Error loading font {font_file}: {e}")
    
    # Verify fonts are available
    available_fonts = font_db.families()
    jetbrains_fonts = [f for f in available_fonts if "JetBrains" in f]
    print(f"Available JetBrains fonts: {jetbrains_fonts}")
    
    return loaded_fonts


class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Dark Theme Demo")
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QVBoxLayout(central_widget)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create tab widget
        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)
        
        # Create tabs
        tab_widget.addTab(self.create_basic_widgets_tab(), "Basic Widgets")
        tab_widget.addTab(self.create_input_widgets_tab(), "Input Widgets")
        tab_widget.addTab(self.create_list_widgets_tab(), "List Widgets")
        
        # Create status bar
        self.statusBar().showMessage("Ready")
        
        # Setup progress bar demo
        self.setup_progress_demo()
    
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        new_action = QAction("New", self)
        new_action.setShortcut("Ctrl+N")
        file_menu.addAction(new_action)
        
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        toolbar.addAction("New")
        toolbar.addAction("Open")
        toolbar.addSeparator()
        toolbar.addAction("Cut")
        toolbar.addAction("Copy")
        toolbar.addAction("Paste")
    
    def create_basic_widgets_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Buttons group
        button_group = QGroupBox("Buttons")
        button_layout = QHBoxLayout(button_group)
        
        normal_btn = QPushButton("Normal Button")
        primary_btn = QPushButton("Primary Button")
        primary_btn.setProperty("class", "primary")
        disabled_btn = QPushButton("Disabled Button")
        disabled_btn.setEnabled(False)
        
        button_layout.addWidget(normal_btn)
        button_layout.addWidget(primary_btn)
        button_layout.addWidget(disabled_btn)
        button_layout.addStretch()
        
        layout.addWidget(button_group)
        
        # Labels and text
        text_group = QGroupBox("Text Elements")
        text_layout = QVBoxLayout(text_group)
        
        label = QLabel("This is a sample label with dark theme styling")
        text_edit = QTextEdit()
        text_edit.setPlainText("The quick brown fox jumps over the lazy dog. This is a text editor with dark theme.\nYou can type here to see the styling.")
        text_edit.setMaximumHeight(100)
        
        # Add code editor example with JetBrains Mono
        code_edit = QTextEdit()
        code_edit.setProperty("class", "code")
        code_edit.setPlainText("""# Python code example with JetBrains Mono
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test the function
for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")""")
        code_edit.setMaximumHeight(120)
        
        # Force apply font to code editor
        from PySide6.QtGui import QFont
        jetbrains_font = QFont("JetBrains Mono", 10)
        code_edit.setFont(jetbrains_font)
        
        # Also set font for regular text editor
        text_edit.setFont(jetbrains_font)
        
        text_layout.addWidget(label)
        text_layout.addWidget(text_edit)
        text_layout.addWidget(code_edit)
        
        layout.addWidget(text_group)
        
        # Progress and slider
        control_group = QGroupBox("Controls")
        control_layout = QVBoxLayout(control_group)
        
        progress_bar = QProgressBar()
        progress_bar.setValue(65)
        control_layout.addWidget(progress_bar)
        
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(50)
        control_layout.addWidget(slider)
        
        layout.addWidget(control_group)
        
        layout.addStretch()
        return widget
    
    def create_input_widgets_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Input fields
        input_group = QGroupBox("Input Fields")
        input_layout = QVBoxLayout(input_group)
        
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Enter text here...")
        input_layout.addWidget(line_edit)
        
        combo_box = QComboBox()
        combo_box.addItems(["Option 1", "Option 2", "Option 3", "Option 4"])
        input_layout.addWidget(combo_box)
        
        spin_box = QSpinBox()
        spin_box.setRange(0, 100)
        spin_box.setValue(25)
        input_layout.addWidget(spin_box)
        
        layout.addWidget(input_group)
        
        # Checkboxes and radio buttons
        selection_group = QGroupBox("Selection Controls")
        selection_layout = QVBoxLayout(selection_group)
        
        checkbox1 = QCheckBox("Checkbox 1")
        checkbox2 = QCheckBox("Checkbox 2 (Checked)")
        checkbox2.setChecked(True)
        checkbox3 = QCheckBox("Checkbox 3 (Disabled)")
        checkbox3.setEnabled(False)
        
        selection_layout.addWidget(checkbox1)
        selection_layout.addWidget(checkbox2)
        selection_layout.addWidget(checkbox3)
        
        radio1 = QRadioButton("Radio Button 1")
        radio2 = QRadioButton("Radio Button 2 (Selected)")
        radio2.setChecked(True)
        radio3 = QRadioButton("Radio Button 3")
        
        selection_layout.addWidget(radio1)
        selection_layout.addWidget(radio2)
        selection_layout.addWidget(radio3)
        
        layout.addWidget(selection_group)
        
        layout.addStretch()
        return widget
    
    def create_list_widgets_tab(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        
        # List widget
        list_group = QGroupBox("List Widget")
        list_layout = QVBoxLayout(list_group)
        
        list_widget = QListWidget()
        list_widget.addItems([
            "Item 1", "Item 2", "Item 3", "Item 4", "Item 5",
            "Item 6", "Item 7", "Item 8", "Item 9", "Item 10"
        ])
        list_layout.addWidget(list_widget)
        
        layout.addWidget(list_group)
        
        # Tree widget (simulated with list)
        tree_group = QGroupBox("Tree-like Structure")
        tree_layout = QVBoxLayout(tree_group)
        
        tree_list = QListWidget()
        tree_list.addItems([
            "📁 Documents",
            "  📄 report.pdf",
            "  📄 presentation.pptx",
            "📁 Pictures",
            "  📄 photo1.jpg",
            "  📄 photo2.png",
            "📁 Music",
            "  📄 song1.mp3",
            "  📄 song2.wav"
        ])
        tree_layout.addWidget(tree_list)
        
        layout.addWidget(tree_group)
        
        return widget
    
    def setup_progress_demo(self):
        """Setup a demo progress bar that updates automatically"""
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)
        self.progress_timer.start(100)  # Update every 100ms
        self.progress_value = 0
    
    def update_progress(self):
        """Update progress bar value for demo"""
        self.progress_value = (self.progress_value + 1) % 101
        # Find progress bar in the widget tree and update it
        for widget in self.findChildren(QProgressBar):
            if widget.parent().title() == "Controls":
                widget.setValue(self.progress_value)
                break
    
    def show_about(self):
        QMessageBox.about(self, "About", 
                         "Qt Dark Theme Demo\n\n"
                         "This application demonstrates the dark theme "
                         "stylesheet for Qt widgets.\n\n"
                         "Created with PySide6")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Load JetBrains Mono fonts from resources
    print("Loading JetBrains Mono fonts...")
    loaded_fonts = load_fonts_from_resources()
    
    # Apply dark theme stylesheet from resources
    # Fallback to file if resources fail
    stylesheet = load_stylesheet_from_resources()
    if not stylesheet:
        print("Falling back to file-based stylesheet loading...")
        stylesheet = load_stylesheet_from_file()
    
    if stylesheet:
        app.setStyleSheet(stylesheet)
        print("Stylesheet applied successfully")
    else:
        print("Warning: No stylesheet applied")
    
    # Set default font for entire application
    from PySide6.QtGui import QFont
    default_font = QFont("JetBrains Mono", 9)
    app.setFont(default_font)
    print(f"Default app font set to: {default_font.family()}")
    
    window = DemoWindow()
    window.show()
    sys.exit(app.exec()) 