# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginxFCvOH.ui'
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
        MainWindow.resize(448, 523)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"border: 1px solid rgb(0, 0, 127);\n"
"	background-color: qlineargradient(spread:reflect, x1:0.516, y1:0, x2:0.513846, y2:1, stop:0 rgba(11, 192, 255, 255), stop:1 rgba(68, 0, 127, 255));\n"
"border-radius:20px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.bt_ingresar = QPushButton(self.frame)
        self.bt_ingresar.setObjectName(u"bt_ingresar")
        self.bt_ingresar.setGeometry(QRect(140, 330, 171, 41))
        self.bt_ingresar.setStyleSheet(u"QPushButton{\n"
"border:4px solid #ffffff;\n"
"border-radius:20px;\n"
"background-color: rgb(0, 255, 0);\n"
"	font: 87 12pt \"Segoe UI Black\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:4px solid #000000;\n"
"border-radius:20px;\n"
"	background-color: rgb(255, 255, 0);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"\n"
"}\n"
"")
        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(100, 270, 241, 31))
        self.password.setStyleSheet(u"QLineEdit {\n"
"border-radius:10px;\n"
"	font: 75 12pt \"Arial\";\n"
"font: 75 12pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignCenter)
        self.users = QLineEdit(self.frame)
        self.users.setObjectName(u"users")
        self.users.setGeometry(QRect(100, 180, 241, 31))
        self.users.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.users.setStyleSheet(u"QLineEdit {\n"
"	font: 75 12pt \"Arial\";\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.users.setInputMethodHints(Qt.ImhNone)
        self.users.setMaxLength(60)
        self.users.setAlignment(Qt.AlignCenter)
        self.users.setDragEnabled(False)
        self.users.setReadOnly(False)
        self.users.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.users.setClearButtonEnabled(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 240, 131, 20))
        self.label.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color:rgba(0,0,0,0%);\n"
"border:0px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 150, 131, 20))
        self.label_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(0,0,0,0%);\n"
"border:0px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 390, 371, 16))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgba(0,0,0,0%);\n"
"     border-radius:25px;\n"
"border: 1px solid #00007f;\n"
"\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(spread:reflect, x1:0.995263, y1:0.563, x2:0, y2:0.574, stop:0.301843 rgba(11, 255, 240, 255), stop:1 rgba(68, 0, 127, 255));\n"
"\n"
"     border-radius:25px;\n"
"\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QProgressBar.BottomToTop)
        self.cargando = QLabel(self.frame)
        self.cargando.setObjectName(u"cargando")
        self.cargando.setGeometry(QRect(150, 410, 151, 31))
        self.cargando.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.cargando.setStyleSheet(u"QLabel{\n"
"background-color: rgba(0,0,0,0%);\n"
"font: 12pt \"Segoe Print\";\n"
"border:0px;\n"
"}")
        self.cargando.setFrameShape(QFrame.NoFrame)
        self.cargando.setFrameShadow(QFrame.Plain)
        self.cargando.setLineWidth(1)
        self.cargando.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, -30, 221, 211))
        self.label_4.setStyleSheet(u"border:0px;\n"
"background-color: rgba(0,0,0,0%);")
        self.label_4.setPixmap(QPixmap(u"logo.png"))
        self.label_4.setScaledContents(True)
        self.contrasena_incorrecta = QLabel(self.frame)
        self.contrasena_incorrecta.setObjectName(u"contrasena_incorrecta")
        self.contrasena_incorrecta.setGeometry(QRect(170, 300, 121, 16))
        self.contrasena_incorrecta.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 0, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"border:0px;\n"
"")
        self.usuario_incorrecto = QLabel(self.frame)
        self.usuario_incorrecto.setObjectName(u"usuario_incorrecto")
        self.usuario_incorrecto.setGeometry(QRect(180, 210, 91, 16))
        self.usuario_incorrecto.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: rgb(255, 0, 0);\n"
"border:0px;\n"
"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 490, 75, 23))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"	font: 75 12pt \"MS Sans Serif\";\n"
"background-color: rgba(0, 0, 0,0%);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:0px;\n"
"	background-color: qlineargradient(spread:reflect, x1:0.540925, y1:1, x2:0.540922, y2:0.006, stop:0.175799 rgba(11, 255, 240, 255), stop:1 rgba(68, 0, 127, 255));\n"
"	font: 75 12pt \"MS Sans Serif\";\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_ingresar.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su contrase\u00f1a", None))
        self.users.setText("")
        self.users.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su correo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.cargando.setText("")
        self.label_4.setText("")
        self.contrasena_incorrecta.setText("")
        self.usuario_incorrecto.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

