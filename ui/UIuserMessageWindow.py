# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserMessageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from modules import ClassConnection
from modules import utility
import threading

class Ui_Dialog_UserMsg(object):

    def setupUi(self, Dialog, username,connection):
        self.username = username

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
        self.pushButtonEnter.setIconSize(QtCore.QSize(25, 25))
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
        self.pushButtonRefreshStatus.clicked.connect(self.updateConnectionStatus)

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

        self.connection = connection
        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #stopPromptThread = True
        #threadPrompt.join()
        threadOutput = threading.Thread(target=self.handleQueue)
        threadOutput.start()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connection with {}".format(self.username)))
        self.labelConnectedTo.setText(_translate("Dialog", "Connected to: {}".format(self.username)))
        # self.pushButtonEnter.setText(_translate("Dialog", "Ent"))
        self.pushButtonSendFile.setText(_translate("Dialog", "Send File"))
        self.pushButtonSendFolder.setText(_translate("Dialog", "Send Folder"))
        self.pushButtonRefreshStatus.setText(_translate("Dialog", "Refresh Status"))
        self.pushButtonDisconnect.setText(_translate("Dialog", "Disconnect"))
        self.labelConnectionStatus.setText(_translate("Dialog", "Connection Status:"))
        self.labelConnectionStatusMod.setText(_translate("Dialog", "Connecting"))

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
                result = self.connection.sendFile(correctedFilePath, "")
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
            self.connection.sendMessage(self.lineEditSendText.text())
            self.lineEditSendText.setText("")


    def pbDisconnect(self):
        if self.pushButtonDisconnect.text() == "Disconnect":
            try:
                self.connection.endConnection()
            except:
                pass
            finally:
                self.pushButtonDisconnect.setText("Reconnect")
                self.labelConnectionStatusMod.setStyleSheet("color:rgb(222,0,0);")
                self.labelConnectionStatusMod.setText("Offline")

        else: #button = reconnect
            try:
                self.createConnection()
                if connection.status == "Connected":
                    self.pushButtonDisconnect.setText("Disconnect")
            except:
                pass

    def updateConnectionStatus(self,status):

        self.labelConnectionStatusMod.setStyleSheet("color:rgb(222,0,0);")
        if status == "":
            status = self.connection.status
        try:
            #status = self.connection.connection_status

            if status == "Connecting...":
                self.labelConnectionStatusMod.setStyleSheet("color:orange;")
            elif status == "Connected":
                self.labelConnectionStatusMod.setStyleSheet("color:rgb(0,222,0);")
            elif status == "Offline":
                self.labelConnectionStatusMod.setStyleSheet("color:rgb(222,0,0);")
                self.pushButtonDisconnect.setText("Reconnect")
            elif status == "error":
                self.labelConnectionStatusMod.setStyleSheet("color:rgb(222,0,0);")
                self.labelConnectionStatusMod.setText("error")
                self.pushButtonDisconnect.setText("Reconnect")
            else:
                self.labelConnectionStatusMod.setStyleSheet("color:orange;")

            self.labelConnectionStatusMod.setText(status)
        except:
            self.labelConnectionStatusMod.setStyleSheet("color:rgb(222,0,0);")
            self.labelConnectionStatusMod.setText("Unknown error")
            self.pushButtonDisconnect.setText("Reconnect")

        finally:
            QApplication.processEvents()

    def handleQueue(self):
        print ("Entering Output Queue loop")
        while True:

            if self.labelConnectionStatusMod.text() != self.connection.status:
                print ("Updateing status")
                self.updateConnectionStatus(self.connection.status)

            if self.connection.OutputQueue and not self.connection.OutputQueue.empty():
                self.textBrowser.append("{}: {}".format(self.username,self.connection.OutputQueue.get()))
                print ("Output Queue wasn't empty!")
            time.sleep(0.5)

    # def promptLoading(self):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Information)
    #     msg.setWindowModality(0)
    #     msg.setWindowTitle("Loading")
    #     msg.setText("         Loading profile...         ")
    #     x = msg.exec_()
    #     while True:
    #         global stopPromptThread
    #         if stop_threads:
    #             break