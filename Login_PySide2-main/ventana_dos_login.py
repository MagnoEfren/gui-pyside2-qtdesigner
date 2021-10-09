# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_dos_loginbdfdKW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaDos(object):
    def setupUi(self, VentanaDos):
        if not VentanaDos.objectName():
            VentanaDos.setObjectName(u"VentanaDos")
        VentanaDos.resize(742, 520)
        self.centralwidget = QWidget(VentanaDos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0.547, y1:1, x2:0.534, y2:0, stop:0.253012 rgba(87, 252, 255, 255), stop:0.776248 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0,0%);\n"
"font: 75 38pt \"MS Sans Serif\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        VentanaDos.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaDos)

        QMetaObject.connectSlotsByName(VentanaDos)
    # setupUi

    def retranslateUi(self, VentanaDos):
        VentanaDos.setWindowTitle(QCoreApplication.translate("VentanaDos", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("VentanaDos", u"VENTANA DOS", None))
    # retranslateUi

