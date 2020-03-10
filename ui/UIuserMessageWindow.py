# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserMessageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from modules import ClassClientConnection
from modules import utility


class Ui_Dialog_UserMsg(object):

    def setupUi(self, Dialog, username):
        self.username = username
        #self.style = utility.stylesheet.style["background"]
        self.connectionStatus = "connecting"

        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        # msg.setWindowModality(0)
        # msg.setWindowTitle("Loading")
        # msg.setText("         Loading profile...         ")
        # x = msg.exec_()

        Dialog.setObjectName("Dialog")
        Dialog.resize(745, 430)
        Dialog.setStyleSheet(utility.stylesheet.style["background"])

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 561, 331))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet(utility.stylesheet.style["textBrowser"])

        self.lineEditSendText = QtWidgets.QLineEdit(Dialog)
        self.lineEditSendText.setGeometry(QtCore.QRect(10, 390, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditSendText.setFont(font)
        self.lineEditSendText.setObjectName("lineEditSendText")
        self.lineEditSendText.setStyleSheet(utility.stylesheet.style["lineEdit"])

        self.labelConnectedTo = QtWidgets.QLabel(Dialog)
        self.labelConnectedTo.setGeometry(QtCore.QRect(10, 10, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelConnectedTo.setFont(font)
        self.labelConnectedTo.setObjectName("labelConnectedTo")

        self.pushButtonEnter = QtWidgets.QPushButton(Dialog)
        self.pushButtonEnter.setGeometry(QtCore.QRect(530, 390, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEnter.setFont(font)
        self.pushButtonEnter.setObjectName("pushButtonEnter")
        self.pushButtonEnter.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonEnter.setIcon(QtGui.QIcon("icons\\send.svg"))
        self.pushButtonEnter.setIconSize(QtCore.QSize(25,25))
        self.pushButtonEnter.clicked.connect(self.pbEnter)


        self.pushButtonSendFile = QtWidgets.QPushButton(Dialog)
        self.pushButtonSendFile.setGeometry(QtCore.QRect(590, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonSendFile.setFont(font)
        self.pushButtonSendFile.setObjectName("pushButtonSendFile")
        self.pushButtonSendFile.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonSendFile.clicked.connect(self.getFilePath)

        self.pushButtonSendFolder = QtWidgets.QPushButton(Dialog)
        self.pushButtonSendFolder.setGeometry(QtCore.QRect(590, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonSendFolder.setFont(font)
        self.pushButtonSendFolder.setObjectName("pushButtonSendFolder")
        self.pushButtonSendFolder.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonSendFolder.clicked.connect(self.getFolderPath)

        self.pushButtonRefreshStatus = QtWidgets.QPushButton(Dialog)
        self.pushButtonRefreshStatus.setGeometry(QtCore.QRect(590, 220, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonRefreshStatus.setFont(font)
        self.pushButtonRefreshStatus.setObjectName("pushButtonRefreshStatus")
        self.pushButtonRefreshStatus.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonRefreshStatus.clicked.connect(self.checkConnectionStatus)

        self.pushButtonDisconnect = QtWidgets.QPushButton(Dialog)
        self.pushButtonDisconnect.setGeometry(QtCore.QRect(590, 340, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonDisconnect.setFont(font)
        self.pushButtonDisconnect.setObjectName("pushButtonDisconnect")
        self.pushButtonDisconnect.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonDisconnect.clicked.connect(self.pbDisconnect)

        self.labelConnectionStatus = QtWidgets.QLabel(Dialog)
        self.labelConnectionStatus.setGeometry(QtCore.QRect(590, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelConnectionStatus.setFont(font)
        self.labelConnectionStatus.setObjectName("labelConnectionStatus")

        self.labelConnectionStatusMod = QtWidgets.QLabel(Dialog)
        self.labelConnectionStatusMod.setGeometry(QtCore.QRect(600, 80, 201, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelConnectionStatusMod.setFont(font)
        self.labelConnectionStatusMod.setObjectName("labelConnectionStatusMod")

        self.createConnection()
        self.checkConnectionStatus()
        self.retranslateUi(Dialog)

        self.checkConnectionStatus()

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.checkConnectionStatus()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connection with {}".format(self.username)))
        self.labelConnectedTo.setText(_translate("Dialog", "Connected to: {}".format(self.username)))
        #self.pushButtonEnter.setText(_translate("Dialog", "Ent"))
        self.pushButtonSendFile.setText(_translate("Dialog", "Send File"))
        self.pushButtonSendFolder.setText(_translate("Dialog", "Send Folder"))
        self.pushButtonRefreshStatus.setText(_translate("Dialog", "Refresh Status"))
        self.pushButtonDisconnect.setText(_translate("Dialog", "Disconnect"))
        self.labelConnectionStatus.setText(_translate("Dialog", "Connection Status:"))
        self.labelConnectionStatusMod.setText(_translate("Dialog", self.connectionStatus))

    def correctFilePath(self, filepath):

        list = filepath.split("/")
        correctedPath = ""
        for i in range(len(list) - 1):
            correctedPath += list[i]
            correctedPath += "\\"
        correctedPath += list[len(list) - 1]
        return correctedPath

    def getFilePath(self):
        title = "Select a file"
        path = "C:\\"
        file, _ = QFileDialog.getOpenFileName(QFileDialog(), title, path, "")
        correctedFilePath = self.correctFilePath(file)

        if file:
            try:
                print ("Sending: {}".format(correctedFilePath))
                result = self.connectionClient.sendFile(correctedFilePath, "")
                if result:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowModality(0)
                    msg.setWindowTitle("Succes")
                    msg.setText("                File Sent Successfully!               ")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowModality(0)
                    msg.setWindowTitle("Fail")
                    msg.setText("                Error sending file!               ")
                    msg.exec_()
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowModality(0)
                msg.setWindowTitle("Fail")
                msg.setText("                Error sending file!               ")
                msg.exec_()
                print ("error")

    def getFolderPath(self):
        title = "Select a folder"
        path = "C:\\"
        folder = QFileDialog.getExistingDirectory(QFileDialog(), title, path)
        print (folder)

    def pbEnter(self):
        if self.lineEditSendText:
            self.textBrowser.append("You: {}".format(self.lineEditSendText.text()))
            self.lineEditSendText.setText("")

    def pbDisconnect(self):
        if self.pushButtonDisconnect.text() == "Disconnect":
            try:
                self.connectionClient.endConnection()
            except:
                pass
            finally:
                self.pushButtonDisconnect.setText("Reconnect")
                self.labelConnectionStatusMod.setStyleSheet("color:rgb(222,0,0);")
                self.labelConnectionStatusMod.setText("Offline")

        else:
            try:
                self.createConnection()
                result = self.checheckConnectionStatus
                if result == "Online":
                    self.pushButtonDisconnect.setText("Disconnect")
            except:
                pass
            finally:
                self.checkConnectionStatus()

    def createConnection(self):
        id = utility.db.getId(self.username)
        name = utility.db.saved_user[id][0]
        ip = utility.db.saved_user[id][1]
        port = utility.db.saved_user[id][2]
        self.connectionClient = ClassClientConnection.ClientConnection(name, ip, port)
        if self.connectionClient:
            if self.connectionClient.connection_status == "Online":
                self.textBrowser.append("Connected to {}:{}".format(ip, port))
            return True
        else:
            return False

    def checkConnectionStatus(self):

        self.labelConnectionStatusMod.setStyleSheet("color:rgb(222,0,0);")
        try:
            status = self.connectionClient.connection_status

            if status == "connecting":
                self.labelConnectionStatusMod.setStyleSheet("color:orange;")
            elif status == "Online":
                self.labelConnectionStatusMod.setStyleSheet("color:rgb(0,222,0);")
            elif status == "Offline":
                self.labelConnectionStatusMod.setStyleSheet("color:rgb(222,0,0);")
                self.pushButtonDisconnect.setText("Reconnect")
            else:
                self.labelConnectionStatusMod.setStyleSheet("color:rgb(222,0,0);")
                self.labelConnectionStatusMod.setText("error")
                self.pushButtonDisconnect.setText("Reconnect")

            self.labelConnectionStatusMod.setText(status)
        except:
            self.labelConnectionStatusMod.setStyleSheet("color:rgb(222,0,0);")
            self.labelConnectionStatusMod.setText("error")
            self.pushButtonDisconnect.setText("Reconnect")

        finally:
            QApplication.processEvents()
