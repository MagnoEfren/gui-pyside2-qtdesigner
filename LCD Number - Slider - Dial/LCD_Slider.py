# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slider_dial_lcdmGQsXD.ui'
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
        MainWindow.resize(494, 377)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFocusPolicy(Qt.NoFocus)
        self.frame.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMouseTracking(False)
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dial = QDial(self.frame_3)
        self.dial.setObjectName(u"dial")
        self.dial.setMouseTracking(False)
        self.dial.setFocusPolicy(Qt.ClickFocus)
        self.dial.setAcceptDrops(False)
        self.dial.setStyleSheet(u"QDial {\n"
"	background-color: rgb(170, 0, 127);\n"
"\n"
"    }\n"
"\n"
"")
        self.dial.setPageStep(0)
        self.dial.setValue(0)
        self.dial.setSliderPosition(0)
        self.dial.setTracking(True)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(3.700000000000000)
        self.dial.setNotchesVisible(True)

        self.horizontalLayout.addWidget(self.dial)

        self.lcdNumber = QLCDNumber(self.frame_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lcdNumber.setFrameShape(QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.lcdNumber)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.slider = QSlider(self.frame_2)
        self.slider.setObjectName(u"slider")
        self.slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 10px; \n"
"    background: blue;\n"
" \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:  green;\n"
"    border: 1px solid black;\n"
"    width: 20px;\n"
"    margin: -8px 0; \n"
"    border-radius:9px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background-color:red;\n"
"  border: 1px solid black;\n"
"}\n"
"")
        self.slider.setSingleStep(0)
        self.slider.setValue(22)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setInvertedAppearance(False)
        self.slider.setInvertedControls(True)
        self.slider.setTickPosition(QSlider.TicksAbove)

        self.horizontalLayout_2.addWidget(self.slider)

        self.lcdNumber2 = QLCDNumber(self.frame_2)
        self.lcdNumber2.setObjectName(u"lcdNumber2")
        self.lcdNumber2.setStyleSheet(u"")
        self.lcdNumber2.setFrameShape(QFrame.NoFrame)
        self.lcdNumber2.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_2.addWidget(self.lcdNumber2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LCD Number - Slider - Dial", None))
    # retranslateUi

