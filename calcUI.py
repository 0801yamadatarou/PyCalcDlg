# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yamada/Desktop/calc/ui/calc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(451, 316)
        self.pushCalc1Button = QtWidgets.QPushButton(Dialog)
        self.pushCalc1Button.setGeometry(QtCore.QRect(50, 220, 80, 26))
        self.pushCalc1Button.setObjectName("pushCalc1Button")
        self.pushCalc2Button = QtWidgets.QPushButton(Dialog)
        self.pushCalc2Button.setGeometry(QtCore.QRect(140, 220, 80, 26))
        self.pushCalc2Button.setObjectName("pushCalc2Button")
        self.pushCalc3Button = QtWidgets.QPushButton(Dialog)
        self.pushCalc3Button.setGeometry(QtCore.QRect(230, 220, 80, 26))
        self.pushCalc3Button.setObjectName("pushCalc3Button")
        self.pushCalc4Button = QtWidgets.QPushButton(Dialog)
        self.pushCalc4Button.setGeometry(QtCore.QRect(50, 180, 80, 26))
        self.pushCalc4Button.setObjectName("pushCalc4Button")
        self.pushCalc5Button = QtWidgets.QPushButton(Dialog)
        self.pushCalc5Button.setGeometry(QtCore.QRect(230, 180, 80, 26))
        self.pushCalc5Button.setObjectName("pushCalc5Button")
        self.pushCalc6Button = QtWidgets.QPushButton(Dialog)
        self.pushCalc6Button.setGeometry(QtCore.QRect(140, 180, 80, 26))
        self.pushCalc6Button.setObjectName("pushCalc6Button")
        self.pushCalc7Button = QtWidgets.QPushButton(Dialog)
        self.pushCalc7Button.setGeometry(QtCore.QRect(50, 140, 80, 26))
        self.pushCalc7Button.setObjectName("pushCalc7Button")
        self.pushCalc8Button = QtWidgets.QPushButton(Dialog)
        self.pushCalc8Button.setGeometry(QtCore.QRect(140, 140, 80, 26))
        self.pushCalc8Button.setObjectName("pushCalc8Button")
        self.pushCalc9Button = QtWidgets.QPushButton(Dialog)
        self.pushCalc9Button.setGeometry(QtCore.QRect(230, 140, 80, 26))
        self.pushCalc9Button.setObjectName("pushCalc9Button")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 100, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushCalcDiviButton = QtWidgets.QPushButton(Dialog)
        self.pushCalcDiviButton.setGeometry(QtCore.QRect(140, 100, 80, 26))
        self.pushCalcDiviButton.setObjectName("pushCalcDiviButton")
        self.pushCalcMultiButton = QtWidgets.QPushButton(Dialog)
        self.pushCalcMultiButton.setGeometry(QtCore.QRect(230, 100, 80, 26))
        self.pushCalcMultiButton.setObjectName("pushCalcMultiButton")
        self.pushCalcSubButton = QtWidgets.QPushButton(Dialog)
        self.pushCalcSubButton.setGeometry(QtCore.QRect(320, 100, 80, 26))
        self.pushCalcSubButton.setObjectName("pushCalcSubButton")
        self.pushCalcAddButton = QtWidgets.QPushButton(Dialog)
        self.pushCalcAddButton.setGeometry(QtCore.QRect(320, 140, 80, 71))
        self.pushCalcAddButton.setObjectName("pushCalcAddButton")
        self.pushCalc0Button = QtWidgets.QPushButton(Dialog)
        self.pushCalc0Button.setGeometry(QtCore.QRect(50, 260, 171, 26))
        self.pushCalc0Button.setObjectName("pushCalc0Button")
        self.pushCalcPointButton = QtWidgets.QPushButton(Dialog)
        self.pushCalcPointButton.setGeometry(QtCore.QRect(230, 260, 80, 26))
        self.pushCalcPointButton.setObjectName("pushCalcPointButton")
        self.pushCalcEqualButton = QtWidgets.QPushButton(Dialog)
        self.pushCalcEqualButton.setGeometry(QtCore.QRect(320, 220, 80, 71))
        self.pushCalcEqualButton.setObjectName("pushCalcEqualButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 20, 351, 70))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushCalc1Button.setText(_translate("Dialog", "1"))
        self.pushCalc2Button.setText(_translate("Dialog", "2"))
        self.pushCalc3Button.setText(_translate("Dialog", "3"))
        self.pushCalc4Button.setText(_translate("Dialog", "4"))
        self.pushCalc5Button.setText(_translate("Dialog", "6"))
        self.pushCalc6Button.setText(_translate("Dialog", "5"))
        self.pushCalc7Button.setText(_translate("Dialog", "7"))
        self.pushCalc8Button.setText(_translate("Dialog", "8"))
        self.pushCalc9Button.setText(_translate("Dialog", "9"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushCalcDiviButton.setText(_translate("Dialog", "/"))
        self.pushCalcMultiButton.setText(_translate("Dialog", "*"))
        self.pushCalcSubButton.setText(_translate("Dialog", "-"))
        self.pushCalcAddButton.setText(_translate("Dialog", "+"))
        self.pushCalc0Button.setText(_translate("Dialog", "0"))
        self.pushCalcPointButton.setText(_translate("Dialog", "."))
        self.pushCalcEqualButton.setText(_translate("Dialog", "="))
