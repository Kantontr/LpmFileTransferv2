# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QMessageBox
from modules import utility


class Ui_Dialog_Settings(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(252, 624)
        Dialog.setStyleSheet(utility.stylesheet.style["background"])

        self.Window = Dialog

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEditServerIp = QtWidgets.QLineEdit(Dialog)
        self.lineEditServerIp.setGeometry(QtCore.QRect(20, 40, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditServerIp.setFont(font)
        self.lineEditServerIp.setText("")
        self.lineEditServerIp.setObjectName("lineEditServerIp")
        self.lineEditServerIp.setStyleSheet(utility.stylesheet.style["lineEdit"])

        self.lineEditServerPort = QtWidgets.QLineEdit(Dialog)
        self.lineEditServerPort.setGeometry(QtCore.QRect(20, 120, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditServerPort.setFont(font)
        self.lineEditServerPort.setText("")
        self.lineEditServerPort.setObjectName("lineEditServerPort")
        self.lineEditServerPort.setStyleSheet(utility.stylesheet.style["lineEdit"])

        self.lineEditServerTimeout = QtWidgets.QLineEdit(Dialog)
        self.lineEditServerTimeout.setGeometry(QtCore.QRect(20, 200, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditServerTimeout.setFont(font)
        self.lineEditServerTimeout.setText("")
        self.lineEditServerTimeout.setObjectName("lineEditServerTimeout")
        self.lineEditServerTimeout.setStyleSheet(utility.stylesheet.style["lineEdit"])

        self.lineEditDefaultPath = QtWidgets.QLineEdit(Dialog)
        self.lineEditDefaultPath.setGeometry(QtCore.QRect(20, 360, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditDefaultPath.setFont(font)
        self.lineEditDefaultPath.setText("")
        self.lineEditDefaultPath.setObjectName("lineEditDefaultPath")
        self.lineEditDefaultPath.setStyleSheet(utility.stylesheet.style["lineEdit"])

        self.comboBoxColorScheme = QtWidgets.QComboBox(Dialog)
        self.comboBoxColorScheme.setGeometry(QtCore.QRect(20, 280, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBoxColorScheme.setFont(font)
        self.comboBoxColorScheme.setObjectName("comboBoxColorScheme")
        self.comboBoxColorScheme.addItem("")
        self.comboBoxColorScheme.addItem("")
        self.comboBoxColorScheme.setStyleSheet(utility.stylesheet.style["comboBox"])

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 400, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 430, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 460, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 490, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 170, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 520, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 330, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.checkBoxClientAutostart = QtWidgets.QCheckBox(Dialog)
        self.checkBoxClientAutostart.setGeometry(QtCore.QRect(200, 400, 20, 21))
        self.checkBoxClientAutostart.setText("")
        self.checkBoxClientAutostart.setObjectName("checkBoxClientAutostart")

        self.checkBoxServerAutostart = QtWidgets.QCheckBox(Dialog)
        self.checkBoxServerAutostart.setGeometry(QtCore.QRect(200, 430, 20, 21))
        self.checkBoxServerAutostart.setText("")
        self.checkBoxServerAutostart.setObjectName("checkBoxServerAutostart")

        self.checkBoxFileIntegrity = QtWidgets.QCheckBox(Dialog)
        self.checkBoxFileIntegrity.setGeometry(QtCore.QRect(200, 460, 20, 21))
        self.checkBoxFileIntegrity.setText("")
        self.checkBoxFileIntegrity.setObjectName("checkBoxFileIntegrity")

        self.checkBoxAllowCommands = QtWidgets.QCheckBox(Dialog)
        self.checkBoxAllowCommands.setGeometry(QtCore.QRect(200, 490, 20, 21))
        self.checkBoxAllowCommands.setText("")
        self.checkBoxAllowCommands.setObjectName("checkBoxAllowCommands")

        self.checkBoxConnectionEncrypted = QtWidgets.QCheckBox(Dialog)
        self.checkBoxConnectionEncrypted.setGeometry(QtCore.QRect(200, 520, 20, 21))
        self.checkBoxConnectionEncrypted.setText("")
        self.checkBoxConnectionEncrypted.setObjectName("checkBoxConnectionEncrypted")

        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(20, 560, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.pushButtonCancel.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonCancel.clicked.connect(self.pbCancel)

        self.pushButtonSave = QtWidgets.QPushButton(Dialog)
        self.pushButtonSave.setGeometry(QtCore.QRect(130, 560, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonSave.clicked.connect(self.pbsave)
        self.pushButtonSave.setStyleSheet(utility.stylesheet.style["button"])


        self.pushButtonSelectDirectory = QtWidgets.QPushButton(Dialog)
        self.pushButtonSelectDirectory.setGeometry(QtCore.QRect(170, 330, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonSelectDirectory.setFont(font)
        self.pushButtonSelectDirectory.setObjectName("pushButtonSelectDirectory")
        self.pushButtonSelectDirectory.clicked.connect(self.selectDirectory)
        self.pushButtonSelectDirectory.setStyleSheet(utility.stylesheet.style["button"])

        self.retranslateUi(Dialog)
        self.setValues()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Server Ip"))
        self.label_2.setText(_translate("Dialog", "Server Port"))
        self.label_3.setText(_translate("Dialog", "Color Scheme"))
        self.comboBoxColorScheme.setItemText(0, _translate("Dialog", "Dark"))
        self.comboBoxColorScheme.setItemText(1, _translate("Dialog", "Light"))
        self.label_4.setText(_translate("Dialog", "Client Autostart"))
        self.label_5.setText(_translate("Dialog", "Server Autostart"))
        self.label_6.setText(_translate("Dialog", "Check file integrity"))
        self.label_7.setText(_translate("Dialog", "Allow for commands"))
        self.label_8.setText(_translate("Dialog", "Server Timeout (sec)"))
        self.label_9.setText(_translate("Dialog", "Connection Encrypted"))
        self.label_10.setText(_translate("Dialog", "Default save path"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))
        self.pushButtonSave.setText(_translate("Dialog", "Save"))
        self.pushButtonSelectDirectory.setText(_translate("Dialog", "Select"))

    def setValues(self):

        self.lineEditServerPort.setText(utility.settings.settings["serverPort"])
        self.lineEditServerIp.setText(utility.settings.settings["serverIp"])
        self.lineEditServerTimeout.setText(utility.settings.settings["serverRequestTimeout"])
        self.lineEditDefaultPath.setText(utility.settings.settings["defaultSavePath"])

        if utility.settings.settings["clientAutostart"] == "true":
            self.checkBoxClientAutostart.setCheckState(1)
        if utility.settings.settings["serverAutostart"] == "true":
            self.checkBoxServerAutostart.setCheckState(-1)
        if utility.settings.settings["checkFileIntegrity"] == "true":
            self.checkBoxFileIntegrity.setCheckState(-1)
        if utility.settings.settings["connectionEncrypted"] == "true":
            self.checkBoxConnectionEncrypted.setCheckState(-1)
        if utility.settings.settings["allowForCommands"] == "true":
            self.checkBoxAllowCommands.setCheckState(-1)
        if utility.settings.settings["colorScheme"] == "dark":
            print (self.comboBoxColorScheme.setCurrentIndex(0))
        elif utility.settings.settings["colorScheme"] == "light":
            print (self.comboBoxColorScheme.setCurrentIndex(1))

    def pbCancel(self):
        self.Window.close()

    def pbsave(self):

        if self.lineEditServerPort.text() != utility.settings.settings["serverPort"]:
            utility.settings.settings["serverPort"] = self.lineEditServerPort.text()

        if self.lineEditServerIp.text() != utility.settings.settings["serverIp"]:
            utility.settings.settings["serverIp"] = self.lineEditServerIp.text()

        if self.lineEditServerTimeout.text() != utility.settings.settings["serverRequestTimeout"]:
            utility.settings.settings["serverRequestTimeout"] = self.lineEditServerTimeout.text()

        if self.lineEditDefaultPath.text() != utility.settings.settings["defaultSavePath"]:
            utility.settings.settings["defaultSavePath"] = self.lineEditDefaultPath.text()

        if self.checkBoxClientAutostart.isChecked():
            utility.settings.settings["clientAutostart"] = "true"
        else:
            utility.settings.settings["clientAutostart"] = "false"

        if self.checkBoxServerAutostart.isChecked():
            utility.settings.settings["serverAutostart"] = "true"
        else:
            utility.settings.settings["serverAutostart"] = "false"

        if self.checkBoxFileIntegrity.isChecked():
            utility.settings.settings["checkFileIntegrity"] = "true"
        else:
            utility.settings.settings["checkFileIntegrity"] = "false"

        if self.checkBoxConnectionEncrypted.isChecked():
            utility.settings.settings["connectionEncrypted"] = "true"
        else:
            utility.settings.settings["connectionEncrypted"] = "false"

        if self.checkBoxAllowCommands.isChecked():
            utility.settings.settings["allowForCommands"] = "true"
        else:
            utility.settings.settings["allowForCommands"] = "false"

        if self.comboBoxColorScheme.currentIndex() == 0 and utility.settings.settings["colorScheme"] != "dark":
            utility.settings.settings["colorScheme"] = "dark"

        if self.comboBoxColorScheme.currentIndex() == 1 and utility.settings.settings["colorScheme"] != "light":
            utility.settings.settings["colorScheme"] = "light"

        if utility.settings.saveSettingsToFile():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowModality(0)
            msg.setWindowTitle("Succes")
            msg.setText("                Changes Saved!               ")
            msg.exec_()

        self.Window.close()




    def selectDirectory(self):

        title = "Select a folder"
        path = "C:\\"
        folder = QFileDialog.getExistingDirectory(QFileDialog(), title, path)
        if folder:
            self.lineEditDefaultPath.setText(folder)
        print (folder)
