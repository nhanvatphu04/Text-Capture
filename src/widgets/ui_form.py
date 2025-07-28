# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
import resources_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setWindowModality(Qt.WindowModality.ApplicationModal)
        Main.resize(600, 420)
        Main.setMinimumSize(QSize(600, 420))
        Main.setMaximumSize(QSize(600, 420))
        Main.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/src/resources/icons/app.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Main.setWindowIcon(icon)
        self.lbTitle = QLabel(Main)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setGeometry(QRect(30, 10, 540, 24))
        self.lbTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbImageArea = QLabel(Main)
        self.lbImageArea.setObjectName(u"lbImageArea")
        self.lbImageArea.setGeometry(QRect(30, 50, 200, 200))
        self.lbImageArea.setAcceptDrops(True)
        self.lbImageArea.setFrameShape(QFrame.Shape.Box)
        self.lbImageArea.setFrameShadow(QFrame.Shadow.Plain)
        self.lbImageArea.setTextFormat(Qt.TextFormat.RichText)
        self.lbImageArea.setScaledContents(False)
        self.lbImageArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbImageArea.setWordWrap(True)
        self.lbImageArea.setIndent(-1)
        self.lbImageArea.setOpenExternalLinks(False)
        self.lbImageOption = QLabel(Main)
        self.lbImageOption.setObjectName(u"lbImageOption")
        self.lbImageOption.setGeometry(QRect(100, 250, 60, 24))
        self.lbImageOption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnUpload = QPushButton(Main)
        self.btnUpload.setObjectName(u"btnUpload")
        self.btnUpload.setGeometry(QRect(30, 275, 200, 24))
        self.txtEdit = QTextEdit(Main)
        self.txtEdit.setObjectName(u"txtEdit")
        self.txtEdit.setGeometry(QRect(260, 50, 310, 270))
        self.btnSentenceCase = QPushButton(Main)
        self.btnSentenceCase.setObjectName(u"btnSentenceCase")
        self.btnSentenceCase.setGeometry(QRect(270, 350, 50, 24))
        icon1 = QIcon()
        icon1.addFile(u":/src/resources/images/lettercase.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSentenceCase.setIcon(icon1)
        self.btnLowerCase = QPushButton(Main)
        self.btnLowerCase.setObjectName(u"btnLowerCase")
        self.btnLowerCase.setGeometry(QRect(330, 350, 50, 24))
        icon2 = QIcon()
        icon2.addFile(u":/src/resources/images/lower.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLowerCase.setIcon(icon2)
        self.btnUpperCase = QPushButton(Main)
        self.btnUpperCase.setObjectName(u"btnUpperCase")
        self.btnUpperCase.setGeometry(QRect(390, 350, 50, 24))
        icon3 = QIcon()
        icon3.addFile(u":/src/resources/images/upper.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUpperCase.setIcon(icon3)
        self.btnRefresh = QPushButton(Main)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setGeometry(QRect(30, 310, 90, 24))
        self.btnGetText = QPushButton(Main)
        self.btnGetText.setObjectName(u"btnGetText")
        self.btnGetText.setGeometry(QRect(140, 310, 90, 24))
        self.btnUnderline = QPushButton(Main)
        self.btnUnderline.setObjectName(u"btnUnderline")
        self.btnUnderline.setGeometry(QRect(450, 350, 50, 24))
        icon4 = QIcon()
        icon4.addFile(u":/src/resources/images/underline.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUnderline.setIcon(icon4)
        self.btnStrikethrough = QPushButton(Main)
        self.btnStrikethrough.setObjectName(u"btnStrikethrough")
        self.btnStrikethrough.setGeometry(QRect(510, 350, 50, 24))
        icon5 = QIcon()
        icon5.addFile(u":/src/resources/images/strikethrough.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStrikethrough.setIcon(icon5)
        self.btnStrikethrough.setIconSize(QSize(24, 24))
        self.lbLanguage = QLabel(Main)
        self.lbLanguage.setObjectName(u"lbLanguage")
        self.lbLanguage.setGeometry(QRect(30, 350, 120, 24))
        self.lbLanguage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cbLanguage = QComboBox(Main)
        self.cbLanguage.setObjectName(u"cbLanguage")
        self.cbLanguage.setGeometry(QRect(150, 345, 80, 24))
        self.cbLanguage.setMinimumSize(QSize(80, 24))
        self.lbStatusBar = QLabel(Main)
        self.lbStatusBar.setObjectName(u"lbStatusBar")
        self.lbStatusBar.setGeometry(QRect(0, 390, 600, 32))
        self.lbStatusBar.setFrameShape(QFrame.Shape.Box)
        self.lbStatusBar.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Text Capture", None))
        self.lbTitle.setText(QCoreApplication.translate("Main", u"Text Capture Tool - L\u1ea5y ch\u1eef t\u1eeb \u1ea3nh", None))
        self.lbImageArea.setText(QCoreApplication.translate("Main", u"<div style=\"text-align: center;\">\n"
"<img src=\":/src/resources/images/add_image.png\"/>\n"
"<br/>\n"
"<span style=\"font-size: 12pt;\">K\u00e9o v\u00e0 th\u1ea3 \u1ea3nh v\u00e0o \u0111\u00e2y</span>\n"
"</div>", None))
        self.lbImageOption.setText(QCoreApplication.translate("Main", u"ho\u1eb7c", None))
#if QT_CONFIG(tooltip)
        self.btnUpload.setToolTip(QCoreApplication.translate("Main", u"T\u1ea3i \u1ea3nh t\u1eeb thi\u1ebft b\u1ecb", None))
#endif // QT_CONFIG(tooltip)
        self.btnUpload.setText(QCoreApplication.translate("Main", u"T\u1ea3i \u1ea3nh", None))
#if QT_CONFIG(tooltip)
        self.btnSentenceCase.setToolTip(QCoreApplication.translate("Main", u"Vi\u1ebft hoa \u0111\u1ea7u c\u00e2u", None))
#endif // QT_CONFIG(tooltip)
        self.btnSentenceCase.setText("")
#if QT_CONFIG(tooltip)
        self.btnLowerCase.setToolTip(QCoreApplication.translate("Main", u"Vi\u1ebft th\u01b0\u1eddng to\u00e0n b\u1ed9", None))
#endif // QT_CONFIG(tooltip)
        self.btnLowerCase.setText("")
#if QT_CONFIG(tooltip)
        self.btnUpperCase.setToolTip(QCoreApplication.translate("Main", u"Vi\u1ebft hoa to\u00e0n b\u1ed9", None))
#endif // QT_CONFIG(tooltip)
        self.btnUpperCase.setText("")
#if QT_CONFIG(tooltip)
        self.btnRefresh.setToolTip(QCoreApplication.translate("Main", u"L\u00e0m m\u1edbi \u1ea3nh", None))
#endif // QT_CONFIG(tooltip)
        self.btnRefresh.setText(QCoreApplication.translate("Main", u"L\u00e0m m\u1edbi", None))
#if QT_CONFIG(tooltip)
        self.btnGetText.setToolTip(QCoreApplication.translate("Main", u"L\u1ea5y ch\u1eef t\u1eeb \u1ea3nh", None))
#endif // QT_CONFIG(tooltip)
        self.btnGetText.setText(QCoreApplication.translate("Main", u"L\u1ea5y ch\u1eef", None))
#if QT_CONFIG(tooltip)
        self.btnUnderline.setToolTip(QCoreApplication.translate("Main", u"G\u1ea1ch ch\u00e2n", None))
#endif // QT_CONFIG(tooltip)
        self.btnUnderline.setText("")
#if QT_CONFIG(tooltip)
        self.btnStrikethrough.setToolTip(QCoreApplication.translate("Main", u"G\u1ea1ch ngang", None))
#endif // QT_CONFIG(tooltip)
        self.btnStrikethrough.setText("")
        self.lbLanguage.setText(QCoreApplication.translate("Main", u"Ch\u1ecdn ng\u00f4n ng\u1eef", None))
#if QT_CONFIG(tooltip)
        self.cbLanguage.setToolTip(QCoreApplication.translate("Main", u"Ch\u1ecdn ng\u00f4n ng\u1eef", None))
#endif // QT_CONFIG(tooltip)
        self.cbLanguage.setCurrentText("")
        self.lbStatusBar.setText("")
    # retranslateUi

