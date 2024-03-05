# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(242, 301)
        Form.setMaximumSize(QSize(243, 301))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 30))
        self.textEdit.setFont(font1)

        self.verticalLayout.addWidget(self.textEdit)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 25))
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.textEdit_2 = QTextEdit(Form)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 30))
        self.textEdit_2.setFont(font1)

        self.verticalLayout.addWidget(self.textEdit_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButton.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 35))
        self.pushButton_2.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 35))
        self.pushButton_3.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Admin \u0444\u043e\u0440\u043c\u0430</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043c\u0435\u043d\u044f\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c \u043d\u0430 admin", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043c\u0435\u043d\u044f\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c \u043d\u0430 user", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043c\u0435\u043d\u044f\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c \u0434\u043b\u044f \u0441\u0435\u0440\u0432\u0438\u0441\u0430", None))
    # retranslateUi

