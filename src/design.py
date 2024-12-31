# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 500)
        Dialog.setMinimumSize(QSize(900, 500))
        Dialog.setMaximumSize(QSize(900, 500))
        Dialog.setStyleSheet(u"background-color: rgb(25, 26, 26);\n"
"color: rgb(255, 255, 255);")
        self.location1 = QTextBrowser(Dialog)
        self.location1.setObjectName(u"location1")
        self.location1.setGeometry(QRect(30, 100, 661, 51))
        self.location1.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.location1.setStyleSheet(u"border-radius: 8px;\n"
"padding: 8px;\n"
"border: 1px solid rgb(70, 119, 255);\n"
"color: rgd(255, 255, 255);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 10, 111, 51))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Arial\";")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 71, 16))
        self.search_btn1 = QPushButton(Dialog)
        self.search_btn1.setObjectName(u"search_btn1")
        self.search_btn1.setGeometry(QRect(720, 110, 100, 32))
        self.search_btn1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_btn1.setStyleSheet(u"background-color: rgb(70, 119, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.search_btn2 = QPushButton(Dialog)
        self.search_btn2.setObjectName(u"search_btn2")
        self.search_btn2.setGeometry(QRect(720, 210, 100, 32))
        self.search_btn2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_btn2.setStyleSheet(u"background-color: rgb(70, 119, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.location2 = QTextBrowser(Dialog)
        self.location2.setObjectName(u"location2")
        self.location2.setGeometry(QRect(30, 200, 661, 51))
        self.location2.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.location2.setStyleSheet(u"border-radius: 8px;\n"
"padding: 8px;\n"
"border: 1px solid rgb(70, 119, 255);\n"
"color: rgd(255, 255, 255);")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 170, 121, 16))
        self.merge_btn = QPushButton(Dialog)
        self.merge_btn.setObjectName(u"merge_btn")
        self.merge_btn.setGeometry(QRect(380, 410, 111, 41))
        self.merge_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.merge_btn.setStyleSheet(u"background-color: rgb(139, 141, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.result_text = QLabel(Dialog)
        self.result_text.setObjectName(u"result_text")
        self.result_text.setGeometry(QRect(380, 320, 121, 31))
        self.result_text.setStyleSheet(u"color: rgb(148, 255, 129);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Merge PDFs", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Merge PDFs", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"First PDF", None))
        self.search_btn1.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.search_btn2.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Second PDF", None))
        self.merge_btn.setText(QCoreApplication.translate("Dialog", u"Merge", None))
        self.result_text.setText("")
    # retranslateUi

