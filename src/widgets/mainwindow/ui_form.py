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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import resources_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setWindowModality(Qt.WindowModality.ApplicationModal)
        Main.resize(400, 300)
        Main.setMinimumSize(QSize(400, 300))
        Main.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/src/resources/icons/app.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Main.setWindowIcon(icon)
        self.lbTitle = QLabel(Main)
        self.lbTitle.setObjectName(u"lbTitle")
        self.lbTitle.setGeometry(QRect(30, 10, 340, 24))
        self.lbTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbImageArea = QLabel(Main)
        self.lbImageArea.setObjectName(u"lbImageArea")
        self.lbImageArea.setGeometry(QRect(30, 50, 150, 150))
        self.lbImageArea.setFrameShape(QFrame.Shape.Box)
        self.lbImageArea.setFrameShadow(QFrame.Shadow.Plain)
        self.lbImageArea.setTextFormat(Qt.TextFormat.RichText)
        self.lbImageArea.setScaledContents(False)
        self.lbImageArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbImageArea.setWordWrap(True)
        self.lbImageArea.setIndent(-1)
        self.lbImageArea.setOpenExternalLinks(False)
        self.btnCapture = QPushButton(Main)
        self.btnCapture.setObjectName(u"btnCapture")
        self.btnCapture.setGeometry(QRect(30, 250, 70, 24))
        self.lbImageOption = QLabel(Main)
        self.lbImageOption.setObjectName(u"lbImageOption")
        self.lbImageOption.setGeometry(QRect(80, 210, 60, 24))
        self.lbImageOption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnUpload = QPushButton(Main)
        self.btnUpload.setObjectName(u"btnUpload")
        self.btnUpload.setGeometry(QRect(110, 250, 70, 24))
        self.txtEdit = QTextEdit(Main)
        self.txtEdit.setObjectName(u"txtEdit")
        self.txtEdit.setGeometry(QRect(200, 50, 170, 170))
        self.btnSentenceCase = QPushButton(Main)
        self.btnSentenceCase.setObjectName(u"btnSentenceCase")
        self.btnSentenceCase.setGeometry(QRect(200, 250, 50, 24))
        icon1 = QIcon()
        icon1.addFile(u":/src/resources/images/lettercase.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSentenceCase.setIcon(icon1)
        self.btnLowerCase = QPushButton(Main)
        self.btnLowerCase.setObjectName(u"btnLowerCase")
        self.btnLowerCase.setGeometry(QRect(260, 250, 50, 24))
        icon2 = QIcon()
        icon2.addFile(u":/src/resources/images/lower.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLowerCase.setIcon(icon2)
        self.btnUpperCase = QPushButton(Main)
        self.btnUpperCase.setObjectName(u"btnUpperCase")
        self.btnUpperCase.setGeometry(QRect(320, 250, 50, 24))
        icon3 = QIcon()
        icon3.addFile(u":/src/resources/images/upper.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnUpperCase.setIcon(icon3)

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
        self.btnCapture.setText(QCoreApplication.translate("Main", u"Ch\u1ee5p \u1ea3nh", None))
        self.lbImageOption.setText(QCoreApplication.translate("Main", u"ho\u1eb7c", None))
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
    # retranslateUi

