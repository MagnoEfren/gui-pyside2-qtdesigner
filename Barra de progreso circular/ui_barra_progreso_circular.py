# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barra_progreso_circularRVFWEb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(746, 303)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setLayoutDirection(Qt.RightToLeft)
        self.frame_2.setStyleSheet(u"background-color: rgb(79, 79, 79);\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.progressbar_uno = QFrame(self.frame_2)
        self.progressbar_uno.setObjectName(u"progressbar_uno")
        self.progressbar_uno.setMinimumSize(QSize(200, 200))
        self.progressbar_uno.setMaximumSize(QSize(200, 200))
        self.progressbar_uno.setStyleSheet(u"QFrame{\n"
"border-radius: 100px;\n"
"\n"
"border-width: 2px;\n"
"border-color:  red;\n"
"border-style: solid;\n"
"\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{stop1} rgba(255, 0, 0, 0), stop:{stop2} rgba(255, 0, 95, 255));\n"
"\n"
"\n"
"\n"
"}")
        self.progressbar_uno.setFrameShape(QFrame.StyledPanel)
        self.progressbar_uno.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.progressbar_uno)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.progressbar_uno)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(160, 160))
        self.frame_3.setMaximumSize(QSize(160, 160))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius: 80px;\n"
"\n"
"border-width: 2px;\n"
"border-color:  red;\n"
"border-style: solid;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(101, 61, 31, 38))
        self.label.setStyleSheet(u"border-width: 0px;\n"
"font: 85 26pt \"Arial \";\n"
"background-color:None;\n"
"color: rgb(0, 0, 0);")
        self.indicador_uno = QLabel(self.frame_3)
        self.indicador_uno.setObjectName(u"indicador_uno")
        self.indicador_uno.setGeometry(QRect(41, 61, 54, 38))
        self.indicador_uno.setMinimumSize(QSize(53, 0))
        self.indicador_uno.setStyleSheet(u"border-width: 0px;\n"
"font: 85 26pt \"Arial \";\n"
"background-color:None;\n"
"color: rgb(0, 0, 0);")
        self.indicador_uno.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.progressbar_uno)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.slider_uno = QSlider(self.frame_5)
        self.slider_uno.setObjectName(u"slider_uno")
        self.slider_uno.setMinimumSize(QSize(30, 30))
        self.slider_uno.setLayoutDirection(Qt.LeftToRight)
        self.slider_uno.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #ff007f;\n"
"    height: 4px; \n"
"    background: #ff007f;\n"
" \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:  #b700ff;\n"
"    width: 28px;\n"
"	height:28px;\n"
"\n"
"left: 11px;\n"
"right: 11px;\n"
"\n"
"\n"
"    margin: -12px; \n"
"    border-radius:14px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background-color:#00aaff;\n"
"border: 1px solid #00aaff;\n"
"}\n"
"")
        self.slider_uno.setMaximum(100)
        self.slider_uno.setSingleStep(1)
        self.slider_uno.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_uno)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setLayoutDirection(Qt.RightToLeft)
        self.frame_7.setStyleSheet(u"background-color: rgb(84, 71, 91);\n"
"border-radius: 20px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progressbar_dos = QFrame(self.frame_7)
        self.progressbar_dos.setObjectName(u"progressbar_dos")
        self.progressbar_dos.setMinimumSize(QSize(200, 200))
        self.progressbar_dos.setMaximumSize(QSize(200, 200))
        self.progressbar_dos.setStyleSheet(u"QFrame{\n"
"\n"
"border-radius: 100px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{stop1} rgba(255, 0, 0, 0), stop:{stop2} rgba(0,255, 75, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.progressbar_dos.setFrameShape(QFrame.StyledPanel)
        self.progressbar_dos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.progressbar_dos)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_9 = QFrame(self.progressbar_dos)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(160, 160))
        self.frame_9.setMaximumSize(QSize(160, 160))
        self.frame_9.setStyleSheet(u"QFrame{\n"
"background-color: rgb(84, 71, 91);\n"
"border-radius: 80px;\n"
"}\n"
"\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 60, 31, 38))
        self.label_2.setStyleSheet(u"border-width: 0px;\n"
"font: 85 26pt \"Arial \";\n"
"background-color:None;\n"
"color: rgb(255, 255, 255);")
        self.indicador_dos = QLabel(self.frame_9)
        self.indicador_dos.setObjectName(u"indicador_dos")
        self.indicador_dos.setGeometry(QRect(40, 60, 54, 38))
        self.indicador_dos.setMinimumSize(QSize(53, 0))
        self.indicador_dos.setStyleSheet(u"border-width: 0px;\n"
"font: 85 26pt \"Arial \";\n"
"background-color:None;\n"
"color: rgb(255, 255, 255);")
        self.indicador_dos.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.progressbar_dos)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.slider_dos = QSlider(self.frame_6)
        self.slider_dos.setObjectName(u"slider_dos")
        self.slider_dos.setMinimumSize(QSize(30, 30))
        self.slider_dos.setLayoutDirection(Qt.LeftToRight)
        self.slider_dos.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #ff007f;\n"
"    height: 4px; \n"
"    background: #ff007f;\n"
" \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:  #b700ff;\n"
"    width: 28px;\n"
"	height:28px;\n"
"\n"
"left: 11px;\n"
"right: 11px;\n"
"\n"
"\n"
"    margin: -12px; \n"
"    border-radius:14px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background-color:#00aaff;\n"
"border: 1px solid #00aaff;\n"
"}\n"
"")
        self.slider_dos.setMaximum(100)
        self.slider_dos.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.slider_dos)


        self.horizontalLayout_7.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setLayoutDirection(Qt.RightToLeft)
        self.frame_11.setStyleSheet(u"background-color: rgb(79, 79, 79);\n"
"border-radius: 20px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.progressbar_tres = QFrame(self.frame_11)
        self.progressbar_tres.setObjectName(u"progressbar_tres")
        self.progressbar_tres.setMinimumSize(QSize(200, 200))
        self.progressbar_tres.setMaximumSize(QSize(200, 200))
        self.progressbar_tres.setStyleSheet(u"QFrame{\n"
"\n"
"border-radius: 100px;\n"
"background-color: qconicalgradient(cx:0.0, cy:0.0, angle:90, stop:{stop1} rgba(255, 0, 0, 255), stop:{stop2} rgba(255, 255, 0, 255), stop:{stop3} rgba(0, 255, 0,255), stop:{stop4} rgba(0, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"")
        self.progressbar_tres.setFrameShape(QFrame.StyledPanel)
        self.progressbar_tres.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.progressbar_tres)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_13 = QFrame(self.progressbar_tres)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(160, 160))
        self.frame_13.setMaximumSize(QSize(160, 160))
        self.frame_13.setStyleSheet(u"QFrame{\n"
"background-color: rgba(0, 170, 255,0);\n"
"border-radius: 80px;\n"
"\n"
"\n"
"border-width: 15px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style :dotted;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 60, 31, 38))
        self.label_3.setStyleSheet(u"border-width: 0px;\n"
"font: 85 26pt \"Arial \";\n"
"background-color:None;\n"
"color: rgb(0, 0, 0);")
        self.indicador_tres = QLabel(self.frame_13)
        self.indicador_tres.setObjectName(u"indicador_tres")
        self.indicador_tres.setGeometry(QRect(40, 60, 54, 38))
        self.indicador_tres.setMinimumSize(QSize(53, 0))
        self.indicador_tres.setStyleSheet(u"border-width: 0px;\n"
"font: 85 26pt \"Arial \";\n"
"background-color:None;\n"
"color: rgb(0, 0, 0);")
        self.indicador_tres.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.frame_13)


        self.horizontalLayout_5.addWidget(self.progressbar_tres)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.slider_tres = QSlider(self.frame_10)
        self.slider_tres.setObjectName(u"slider_tres")
        self.slider_tres.setMinimumSize(QSize(30, 30))
        self.slider_tres.setLayoutDirection(Qt.LeftToRight)
        self.slider_tres.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #ff007f;\n"
"    height: 4px; \n"
"    background: #ff007f;\n"
" \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:  #b700ff;\n"
"    width: 28px;\n"
"	height:28px;\n"
"\n"
"left: 11px;\n"
"right: 11px;\n"
"\n"
"\n"
"    margin: -12px; \n"
"    border-radius:14px;\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background-color:#00aaff;\n"
"border: 1px solid #00aaff;\n"
"}\n"
"")
        self.slider_tres.setMaximum(100)
        self.slider_tres.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.slider_tres)


        self.horizontalLayout_7.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Barra de progreso circular", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.indicador_uno.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.indicador_dos.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.indicador_tres.setText(QCoreApplication.translate("MainWindow", u"100", None))
    # retranslateUi

