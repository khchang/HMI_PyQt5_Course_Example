# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormHello.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormHello(object):
    def setupUi(self, FormHello):
        FormHello.setObjectName("FormHello")
        FormHello.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(FormHello)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabHello = QtWidgets.QLabel(FormHello)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.LabHello.setFont(font)
        self.LabHello.setObjectName("LabHello")
        self.verticalLayout.addWidget(self.LabHello)
        self.btnClose = QtWidgets.QPushButton(FormHello)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout.addWidget(self.btnClose)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(FormHello)
        QtCore.QMetaObject.connectSlotsByName(FormHello)

    def retranslateUi(self, FormHello):
        _translate = QtCore.QCoreApplication.translate
        FormHello.setWindowTitle(_translate("FormHello", "Demo2_2"))
        self.LabHello.setText(_translate("FormHello", "Hello World! Qt Designer"))
        self.btnClose.setText(_translate("FormHello", "關閉"))
