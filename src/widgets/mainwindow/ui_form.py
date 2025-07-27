# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
    QDragEnterEvent,
    QDropEvent,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QWidget,
)
import resources_rc
import os


class ImageLabel(QLabel):
    """Custom QLabel that supports drag & drop for images"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Plain)
        self.setTextFormat(Qt.TextFormat.RichText)
        self.setScaledContents(False)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setWordWrap(True)
        self.setIndent(-1)
        self.setOpenExternalLinks(False)

        # Set default text
        self.setText(
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

        # Store the current image path
        self.image_path = None

    def dragEnterEvent(self, event: QDragEnterEvent):
        """Handle drag enter event"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.setStyleSheet(
                "border: 2px dashed #4CAF50; background-color: rgba(76, 175, 80, 0.1);"
            )
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        """Handle drag leave event"""
        self.setStyleSheet("")
        super().dragLeaveEvent(event)

    def dropEvent(self, event: QDropEvent):
        """Handle drop event"""
        self.setStyleSheet("")

        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                if self._is_valid_image_file(file_path):
                    self.load_image(file_path)
                    event.acceptProposedAction()
                else:
                    print(f"Invalid image file: {file_path}")
        else:
            event.ignore()

    def _is_valid_image_file(self, file_path):
        """Check if the file is a valid image"""
        if not os.path.exists(file_path):
            return False

        # Check file extension
        valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"]
        file_ext = os.path.splitext(file_path)[1].lower()
        return file_ext in valid_extensions

    def load_image(self, image_path):
        """Load and display an image"""
        try:
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                # Scale pixmap to fit the label while maintaining aspect ratio
                scaled_pixmap = pixmap.scaled(
                    self.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
                self.setPixmap(scaled_pixmap)
                self.image_path = image_path
                print(f"Image loaded successfully: {image_path}")
            else:
                print(f"Failed to load image: {image_path}")
        except Exception as e:
            print(f"Error loading image: {e}")

    def mousePressEvent(self, event):
        """Handle mouse press event for file selection"""
        if event.button() == Qt.MouseButton.LeftButton:
            from PySide6.QtWidgets import QFileDialog

            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Chọn ảnh",
                "",
                "Image Files (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp)",
            )
            if file_path:
                self.load_image(file_path)
        super().mousePressEvent(event)

    def clear_image(self):
        """Clear the image and reset to default state"""
        self.clear()
        self.setText(
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
        self.image_path = None
        self.setStyleSheet("")  # Reset any custom styling


class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName("Main")
        Main.setWindowModality(Qt.WindowModality.ApplicationModal)
        Main.resize(600, 400)
        Main.setMinimumSize(QSize(600, 400))
        Main.setMaximumSize(QSize(600, 400))
        Main.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(
            ":/src/resources/icons/app.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        Main.setWindowIcon(icon)
        self.lbTitle = QLabel(Main)
        self.lbTitle.setObjectName("lbTitle")
        self.lbTitle.setGeometry(QRect(30, 10, 540, 24))
        self.lbTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbImageArea = ImageLabel(Main)
        self.lbImageArea.setObjectName("lbImageArea")
        self.lbImageArea.setGeometry(QRect(30, 50, 200, 200))
        self.btnCapture = QPushButton(Main)
        self.btnCapture.setObjectName("btnCapture")
        self.btnCapture.setGeometry(QRect(30, 350, 90, 24))
        self.lbImageOption = QLabel(Main)
        self.lbImageOption.setObjectName("lbImageOption")
        self.lbImageOption.setGeometry(QRect(100, 320, 60, 24))
        self.lbImageOption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnUpload = QPushButton(Main)
        self.btnUpload.setObjectName("btnUpload")
        self.btnUpload.setGeometry(QRect(140, 350, 90, 24))
        self.txtEdit = QTextEdit(Main)
        self.txtEdit.setObjectName("txtEdit")
        self.txtEdit.setGeometry(QRect(260, 50, 310, 270))
        self.btnSentenceCase = QPushButton(Main)
        self.btnSentenceCase.setObjectName("btnSentenceCase")
        self.btnSentenceCase.setGeometry(QRect(270, 350, 50, 24))
        icon1 = QIcon()
        icon1.addFile(
            ":/src/resources/images/lettercase.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.btnSentenceCase.setIcon(icon1)
        self.btnLowerCase = QPushButton(Main)
        self.btnLowerCase.setObjectName("btnLowerCase")
        self.btnLowerCase.setGeometry(QRect(330, 350, 50, 24))
        icon2 = QIcon()
        icon2.addFile(
            ":/src/resources/images/lower.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.btnLowerCase.setIcon(icon2)
        self.btnUpperCase = QPushButton(Main)
        self.btnUpperCase.setObjectName("btnUpperCase")
        self.btnUpperCase.setGeometry(QRect(390, 350, 50, 24))
        icon3 = QIcon()
        icon3.addFile(
            ":/src/resources/images/upper.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.btnUpperCase.setIcon(icon3)
        self.btnRefresh = QPushButton(Main)
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnRefresh.setGeometry(QRect(30, 280, 90, 24))
        self.btnGetText = QPushButton(Main)
        self.btnGetText.setObjectName("btnGetText")
        self.btnGetText.setGeometry(QRect(140, 280, 90, 24))
        self.btnUnderline = QPushButton(Main)
        self.btnUnderline.setObjectName("btnUnderline")
        self.btnUnderline.setGeometry(QRect(450, 350, 50, 24))
        icon4 = QIcon()
        icon4.addFile(
            ":/src/resources/images/underline.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.btnUnderline.setIcon(icon4)
        self.btnStrikethrough = QPushButton(Main)
        self.btnStrikethrough.setObjectName("btnStrikethrough")
        self.btnStrikethrough.setGeometry(QRect(510, 350, 50, 24))
        icon5 = QIcon()
        icon5.addFile(
            ":/src/resources/images/strikethrough.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.btnStrikethrough.setIcon(icon5)
        self.btnStrikethrough.setIconSize(QSize(24, 24))

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)

    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", "Text Capture", None))
        self.lbTitle.setText(
            QCoreApplication.translate(
                "Main", "Text Capture Tool - L\u1ea5y ch\u1eef t\u1eeb \u1ea3nh", None
            )
        )
        self.lbImageArea.setText(
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
        # if QT_CONFIG(tooltip)
        self.btnCapture.setToolTip(
            QCoreApplication.translate(
                "Main", "Ch\u1ee5p \u1ea3nh t\u1eeb m\u00e0n h\u00ecnh", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btnCapture.setText(
            QCoreApplication.translate("Main", "Ch\u1ee5p \u1ea3nh", None)
        )
        self.lbImageOption.setText(
            QCoreApplication.translate("Main", "ho\u1eb7c", None)
        )
        # if QT_CONFIG(tooltip)
        self.btnUpload.setToolTip(
            QCoreApplication.translate(
                "Main", "T\u1ea3i \u1ea3nh t\u1eeb thi\u1ebft b\u1ecb", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btnUpload.setText(
            QCoreApplication.translate("Main", "T\u1ea3i \u1ea3nh", None)
        )
        # if QT_CONFIG(tooltip)
        self.btnSentenceCase.setToolTip(
            QCoreApplication.translate(
                "Main", "Vi\u1ebft hoa \u0111\u1ea7u c\u00e2u", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btnSentenceCase.setText("")
        # if QT_CONFIG(tooltip)
        self.btnLowerCase.setToolTip(
            QCoreApplication.translate(
                "Main", "Vi\u1ebft th\u01b0\u1eddng to\u00e0n b\u1ed9", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btnLowerCase.setText("")
        # if QT_CONFIG(tooltip)
        self.btnUpperCase.setToolTip(
            QCoreApplication.translate("Main", "Vi\u1ebft hoa to\u00e0n b\u1ed9", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.btnUpperCase.setText("")
        # if QT_CONFIG(tooltip)
        self.btnRefresh.setToolTip(
            QCoreApplication.translate("Main", "L\u00e0m m\u1edbi \u1ea3nh", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.btnRefresh.setText(
            QCoreApplication.translate("Main", "L\u00e0m m\u1edbi", None)
        )
        # if QT_CONFIG(tooltip)
        self.btnGetText.setToolTip(
            QCoreApplication.translate(
                "Main", "L\u1ea5y ch\u1eef t\u1eeb \u1ea3nh", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.btnGetText.setText(
            QCoreApplication.translate("Main", "L\u1ea5y ch\u1eef", None)
        )
        # if QT_CONFIG(tooltip)
        self.btnUnderline.setToolTip(
            QCoreApplication.translate("Main", "G\u1ea1ch ch\u00e2n", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.btnUnderline.setText("")
        # if QT_CONFIG(tooltip)
        self.btnStrikethrough.setToolTip(
            QCoreApplication.translate("Main", "G\u1ea1ch ngang", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.btnStrikethrough.setText("")

    # retranslateUi
