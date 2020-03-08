# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserMessageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from modules import ClassClientConnection
from modules import utility


class Ui_Dialog(object):

    def setupUi(self, Dialog, username):
        self.username = username
        self.style = utility.stylesheet.dark["background"]
        self.connectionStatus = "connecting"

        id = utility.db.getId(username)
        print ("KNUTss {} id",format(id))
        name = utility.db.saved_user[id][0]
        print ("KNUTss")
        ip = utility.db.saved_user[id][1]
        print ("KNUTss")
        port = utility.db.saved_user[id][2]
        print ("KNUTss")
        self.connectionClient = ClassClientConnection.ClientConnection(name, ip, port)
        print ("KNUTss")

        Dialog.setObjectName("Dialog")
        Dialog.resize(745, 430)
        Dialog.setStyleSheet(self.style)

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 561, 331))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.lineEditSendText = QtWidgets.QLineEdit(Dialog)
        self.lineEditSendText.setGeometry(QtCore.QRect(10, 390, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEditSendText.setFont(font)
        self.lineEditSendText.setObjectName("lineEditSendText")

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
        self.pushButtonEnter.setStyleSheet(utility.stylesheet.dark["button"])

        self.pushButtonSendFile = QtWidgets.QPushButton(Dialog)
        self.pushButtonSendFile.setGeometry(QtCore.QRect(590, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonSendFile.setFont(font)
        self.pushButtonSendFile.setObjectName("pushButtonSendFile")
        self.pushButtonSendFile.setStyleSheet(utility.stylesheet.dark["button"])

        self.pushButtonSendFolder = QtWidgets.QPushButton(Dialog)
        self.pushButtonSendFolder.setGeometry(QtCore.QRect(590, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonSendFolder.setFont(font)
        self.pushButtonSendFolder.setObjectName("pushButtonSendFolder")
        self.pushButtonSendFolder.setStyleSheet(utility.stylesheet.dark["button"])

        self.pushButtonDisconnect = QtWidgets.QPushButton(Dialog)
        self.pushButtonDisconnect.setGeometry(QtCore.QRect(590, 340, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButtonDisconnect.setFont(font)
        self.pushButtonDisconnect.setObjectName("pushButtonDisconnect")
        self.pushButtonDisconnect.setStyleSheet(utility.stylesheet.dark["button"])

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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connection with {}".format(self.username)))
        self.labelConnectedTo.setText(_translate("Dialog", "Connected to: {}".format(self.username)))
        self.pushButtonEnter.setText(_translate("Dialog", "Ent"))
        self.pushButtonSendFile.setText(_translate("Dialog", "Send File"))
        self.pushButtonSendFolder.setText(_translate("Dialog", "Send Folder"))
        self.pushButtonDisconnect.setText(_translate("Dialog", "Disconnect"))
        self.labelConnectionStatus.setText(_translate("Dialog", "Connection Status:"))
        self.labelConnectionStatusMod.setText(_translate("Dialog", self.connectionStatus))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
