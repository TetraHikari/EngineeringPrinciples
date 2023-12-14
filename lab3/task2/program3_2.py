# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1792, 1067)
        self.num_label = QLabel(Form)
        self.num_label.setObjectName(u"num_label")
        self.num_label.setGeometry(QRect(640, 410, 151, 201))
        self.num_label.setAlignment(Qt.AlignCenter)
        self.inc_button = QPushButton(Form)
        self.inc_button.setObjectName(u"inc_button")
        self.inc_button.setGeometry(QRect(809, 401, 111, 111))
        self.dec_button = QPushButton(Form)
        self.dec_button.setObjectName(u"dec_button")
        self.dec_button.setGeometry(QRect(810, 510, 111, 111))
        self.reset_btn = QPushButton(Form)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(930, 400, 141, 221))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.num_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.inc_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.dec_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

