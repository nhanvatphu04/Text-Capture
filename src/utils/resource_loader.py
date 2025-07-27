import os
from PySide6.QtCore import QFile, QIODevice, QTextStream
from PySide6.QtGui import QFontDatabase


class ResourceLoader:
    def __init__(self, project_root: str = None):
        """
        Initialize ResourceLoader with project root path

        Args:
            project_root: Path to project root directory
        """
        if project_root is None:
            # Try to determine project root automatically
            current_dir = os.getcwd()
            if os.path.basename(current_dir) == "app":
                project_root = os.path.dirname(current_dir)
            else:
                project_root = current_dir

        self.project_root = project_root
        self.src_path = os.path.join(project_root, "src")

    def load_stylesheet_from_file(self) -> str:
        """
        Load and return the stylesheet from style.qss file

        Returns:
            str: Stylesheet content or empty string if failed
        """
        try:
            # Look for style.qss in the resources directory
            style_file = os.path.join(self.src_path, "resources", "styles", "style.qss")
            with open(style_file, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print("Warning: style.qss file not found in resources/styles/")
            return ""
        except Exception as e:
            print(f"Error loading stylesheet: {e}")
            return ""

    def load_stylesheet_from_resources(self) -> str:
        """
        Load and return the stylesheet from resources

        Returns:
            str: Stylesheet content or empty string if failed
        """
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

    def load_stylesheet(self) -> str:
        """
        Load stylesheet with fallback mechanism

        Returns:
            str: Stylesheet content or empty string if failed
        """
        # Try resources first, then fallback to file
        stylesheet = self.load_stylesheet_from_resources()
        if not stylesheet:
            print("Falling back to file-based stylesheet loading...")
            stylesheet = self.load_stylesheet_from_file()

        return stylesheet

    def load_fonts_from_resources(self) -> list:
        """
        Load JetBrains Mono fonts from resources

        Returns:
            list: List of loaded font families
        """
        font_files = [
            ":/src/resources/fonts/JetBrainsMono-Regular.ttf",
            ":/src/resources/fonts/JetBrainsMono-Bold.ttf",
            ":/src/resources/fonts/JetBrainsMono-Italic.ttf",
            ":/src/resources/fonts/JetBrainsMono-Light.ttf",
            ":/src/resources/fonts/JetBrainsMono-Medium.ttf",
        ]

        font_db = QFontDatabase()
        loaded_fonts = []

        for font_file in font_files:
            try:
                font_id = font_db.addApplicationFont(font_file)
                if font_id != -1:
                    font_families = font_db.applicationFontFamilies(font_id)
                    loaded_fonts.extend(font_families)
                else:
                    print(f"Failed to load font: {font_file}")
            except Exception as e:
                print(f"Error loading font {font_file}: {e}")

        return loaded_fonts

    def load_fonts_from_file(self) -> list:
        """
        Load JetBrains Mono fonts from file system

        Returns:
            list: List of loaded font families
        """
        font_files = [
            os.path.join(
                self.src_path, "resources", "fonts", "JetBrainsMono-Regular.ttf"
            ),
            os.path.join(self.src_path, "resources", "fonts", "JetBrainsMono-Bold.ttf"),
            os.path.join(
                self.src_path, "resources", "fonts", "JetBrainsMono-Italic.ttf"
            ),
            os.path.join(
                self.src_path, "resources", "fonts", "JetBrainsMono-Light.ttf"
            ),
            os.path.join(
                self.src_path, "resources", "fonts", "JetBrainsMono-Medium.ttf"
            ),
        ]

        font_db = QFontDatabase()
        loaded_fonts = []

        for font_file in font_files:
            try:
                if os.path.exists(font_file):
                    font_id = font_db.addApplicationFont(font_file)
                    if font_id != -1:
                        font_families = font_db.applicationFontFamilies(font_id)
                        loaded_fonts.extend(font_families)
                    else:
                        print(f"Failed to load font from file: {font_file}")
                else:
                    print(f"Font file not found: {font_file}")
            except Exception as e:
                print(f"Error loading font from file {font_file}: {e}")

        return loaded_fonts

    def load_fonts(self) -> list:
        """
        Load fonts with fallback mechanism

        Returns:
            list: List of loaded font families
        """
        # Try resources first, then fallback to file
        loaded_fonts = self.load_fonts_from_resources()
        if not loaded_fonts:
            print("Falling back to file-based font loading...")
            loaded_fonts = self.load_fonts_from_file()

        return loaded_fonts
