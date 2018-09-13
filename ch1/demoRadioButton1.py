# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 30, 221, 16))
        self.label.setObjectName("label")
        self.labelFare = QtWidgets.QLabel(Dialog)
        self.labelFare.setGeometry(QtCore.QRect(70, 240, 271, 16))
        self.labelFare.setText("")
        self.labelFare.setObjectName("labelFare")
        self.radioButtonFirstClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonFirstClass.setGeometry(QtCore.QRect(90, 90, 161, 20))
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.radionButtonBusinessClass = QtWidgets.QRadioButton(Dialog)
        self.radionButtonBusinessClass.setGeometry(QtCore.QRect(90, 130, 151, 20))
        self.radionButtonBusinessClass.setObjectName("radionButtonBusinessClass")
        self.radioButtonEconomyClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEconomyClass.setGeometry(QtCore.QRect(90, 170, 161, 20))
        self.radioButtonEconomyClass.setObjectName("radioButtonEconomyClass")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose the flight type"))
        self.radioButtonFirstClass.setText(_translate("Dialog", "First Class $150"))
        self.radionButtonBusinessClass.setText(_translate("Dialog", "Business Class $125"))
        self.radioButtonEconomyClass.setText(_translate("Dialog", "Economy Class $100"))

