# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 61, 51))
        self.label_2.setObjectName("label_2")
        self.txt_sayi1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi1.setGeometry(QtCore.QRect(60, 10, 181, 31))
        self.txt_sayi1.setObjectName("txt_sayi1")
        self.txt_sayi2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sayi2.setGeometry(QtCore.QRect(60, 50, 181, 31))
        self.txt_sayi2.setObjectName("txt_sayi2")
        self.btn_toplama = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toplama.setGeometry(QtCore.QRect(10, 90, 91, 41))
        self.btn_toplama.setObjectName("btn_toplama")
        self.btn_cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikarma.setGeometry(QtCore.QRect(110, 90, 91, 41))
        self.btn_cikarma.setObjectName("btn_cikarma")
        self.btn_carpma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carpma.setGeometry(QtCore.QRect(210, 90, 91, 41))
        self.btn_carpma.setObjectName("btn_carpma")
        self.btn_bolme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bolme.setGeometry(QtCore.QRect(310, 90, 91, 41))
        self.btn_bolme.setObjectName("btn_bolme")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(40, 140, 151, 16))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sayı1:"))
        self.label_2.setText(_translate("MainWindow", "Sayı2:"))
        self.btn_toplama.setText(_translate("MainWindow", "Toplama"))
        self.btn_cikarma.setText(_translate("MainWindow", "Çıkarma"))
        self.btn_carpma.setText(_translate("MainWindow", "Çarpma"))
        self.btn_bolme.setText(_translate("MainWindow", "Bölme"))
        self.lbl_sonuc.setText(_translate("MainWindow", "Sonuç :"))
