# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_user.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QMessageBox
from modules import utility


class Ui_Dialog_AddUser(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(284, 417)
        Dialog.setStyleSheet(utility.stylesheet.style["background"])
        self.Window = Dialog

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(utility.stylesheet.style["lineEdit"])

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 130, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet(utility.stylesheet.style["lineEdit"])

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 210, 221, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet(utility.stylesheet.style["lineEdit"])

        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 290, 221, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet(utility.stylesheet.style["lineEdit"])

        self.pushButtonAccept = QtWidgets.QPushButton(Dialog)
        self.pushButtonAccept.setGeometry(QtCore.QRect(30, 350, 111, 31))
        self.pushButtonAccept.setObjectName("pushButtonAccept")
        self.pushButtonAccept.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonAccept.clicked.connect(self.pbAccept)

        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(140, 350, 111, 31))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.pushButtonCancel.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonCancel.clicked.connect(self.pbCancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add User"))
        self.label.setText(_translate("Dialog", "*Username"))
        self.label_2.setText(_translate("Dialog", "*Ip"))
        self.label_3.setText(_translate("Dialog", "*Port"))
        self.label_4.setText(_translate("Dialog", "Comment: (optional)"))
        self.pushButtonAccept.setText(_translate("Dialog", "Accept"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))

    def pbAccept(self):
        username = self.lineEdit.text()
        ip = self.lineEdit_2.text()
        port = self.lineEdit_3.text()
        comment = self.lineEdit_4.text()

        if username != "" and ip != "" and port != "":

            if utility.db.checkIfUserExist(username):
                self.messageboxCritical("Error", "Username already exists!")
                return
            if utility.db.checkIfIpExist(ip):
                self.messageboxCritical("Error", "Ip already exists!")
                return
            if utility.db.addUser(username, ip, port, comment):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowModality(0)
                msg.setWindowTitle("Succes")
                msg.setText("          " + "User added!" + "          ")
                msg.exec_()
                self.Window.close()
            else:
                self.messageboxCritical("Error", "Something went wrong, operation aborted!")
                return
        else:
            self.messageboxCritical("Error", "All fields must be filled!")
            return

    def pbCancel(self):
        self.Window.close()

    def messageboxCritical(self, title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowModality(0)
        msg.setWindowTitle(title)
        msg.setText("          " + text + "          ")
        msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
