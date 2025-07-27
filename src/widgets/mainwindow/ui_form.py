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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)
import sys
import os
# Add src directory to path to import resources_rc
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
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

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Text Capture", None))
    # retranslateUi

