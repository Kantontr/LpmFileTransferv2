# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from modules import utility, ClassConnection
from ui import UIuserMessageWindow, UIsettings, UIaddUser
import sys, threading


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        utility.db.loadDatabaseFromFile()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 581)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)

        # Style sheet
        MainWindow.setStyleSheet(utility.stylesheet.style["background"])

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 411, 550))
        self.treeWidget.setMaximumSize(QtCore.QSize(411, 550))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")

        self.labelServerStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelServerStatus.setGeometry(QtCore.QRect(10, 550, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelServerStatus.setFont(font)
        self.labelServerStatus.setObjectName("labelServerStatus")

        self.pushButtonAddUser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddUser.setGeometry(QtCore.QRect(430, 40, 51, 51))
        self.pushButtonAddUser.setObjectName("pushButtonAddUser")
        self.pushButtonAddUser.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonAddUser.setIcon(QtGui.QIcon("icons\\addUser.svg"))
        self.pushButtonAddUser.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonAddUser.clicked.connect(self.pbAddUser)

        self.pushButtonRemUser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemUser.setGeometry(QtCore.QRect(430, 100, 51, 51))
        self.pushButtonRemUser.setObjectName("pushButtonRemUser")
        self.pushButtonRemUser.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonRemUser.setIcon(QtGui.QIcon("icons\\removeUser.svg"))
        self.pushButtonRemUser.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonRemUser.setEnabled(0)
        self.pushButtonRemUser.clicked.connect(self.pbRemUser)

        self.pushButtonSettings = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSettings.setGeometry(QtCore.QRect(430, 220, 51, 51))
        self.pushButtonSettings.setObjectName("pushButtonSettings")
        self.pushButtonSettings.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonSettings.setIcon(QtGui.QIcon("icons\\settings.svg"))
        self.pushButtonSettings.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonSettings.clicked.connect(self.pbsettings)

        self.pushButtonEnter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEnter.setGeometry(QtCore.QRect(430, 160, 51, 51))
        self.pushButtonEnter.setObjectName("pushButtonEnter")
        self.pushButtonEnter.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonEnter.setIcon(QtGui.QIcon("icons\\selectUser.svg"))
        self.pushButtonEnter.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonEnter.setEnabled(0)

        self.pushButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(430, 480, 51, 51))
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.pushButtonExit.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonExit.setIcon(QtGui.QIcon("icons\\exit.svg"))
        self.pushButtonExit.setIconSize(QtCore.QSize(40, 40))

        self.treeWidget.clicked.connect(self.treeSelection)
        self.treeWidget.itemDoubleClicked.connect(self.doubleClickHandler)
        self.pushButtonExit.clicked.connect(self.quit)
        self.pushButtonEnter.clicked.connect(self.openUserWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.serverThread = threading.Thread(target=self.serverWaitForConnection)
        self.serverThread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LPM Transfer v2"))
        self.labelServerStatus.setText(_translate("Dialog", "Server Offline"))

        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Online Users"))
        self.treeWidget.setStyleSheet(utility.stylesheet.style["tree"])
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setAlternatingRowColors(True)
        # self.treeWidget.setIcon(QtGui.QIcon("icons\\exit.svg"))
        # self.treeWidget.setIconSize(QtCore.QSize(40, 40))
        self.fillTree()

    def fillTree(self):
        self.treeWidget.clear()
        font = QtGui.QFont()
        font.setPointSize(13)

        for i in utility.db.saved_user:
            ntw = QtWidgets.QTreeWidgetItem(self.treeWidget, [utility.db.saved_user[i][0]])
            QtWidgets.QTreeWidgetItem(ntw, [utility.db.saved_user[i][1]]).setFont(0, font)
            QtWidgets.QTreeWidgetItem(ntw, [utility.db.saved_user[i][2]]).setFont(0, font)
            QtWidgets.QTreeWidgetItem(ntw, [utility.db.saved_user[i][3]]).setFont(0, font)

    def quit(self):
        sys.exit()

    def pbNewConnection(self):
        if self.treeWidget.selectedItems():  # if an item is selected
            if self.treeWidget.currentItem().parent():  # parent exist
                username = self.treeWidget.currentItem().parent().text(0)
            else:
                username = self.treeWidget.currentItem().text(0)
            connection = self.createConnection("client", username)
            self.openUserWindow(username, connection)

    def pbAddUser(self):
        Dialog = QtWidgets.QDialog()
        ui = UIaddUser.Ui_Dialog_AddUser()
        ui.setupUi(Dialog)
        Dialog.exec_()
        self.fillTree()

    def pbRemUser(self):
        if self.treeWidget.selectedItems():  # if an item is selected
            if self.treeWidget.currentItem().parent():  # parent exist
                username = self.treeWidget.currentItem().parent().text(0)
            else:
                username = self.treeWidget.currentItem().text(0)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setWindowModality(0)
            msg.setWindowTitle("Delete user?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            msg.setText("          Delete user " + username + "?          ")
            ret = msg.exec_()

            if ret == QMessageBox.Yes:
                utility.db.removeUser(username)
                self.fillTree()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Question)
                msg.setWindowModality(0)
                msg.setWindowTitle("Succes")
                msg.setText("          User deleted!          ")
                msg.exec_()

    def openUserWindow(self, username, connection):
        #self.serverWaitingConnection.shutdown()
        Dialog = QtWidgets.QDialog()
        ui = UIuserMessageWindow.Ui_Dialog_UserMsg()
        ui.setupUi(Dialog, username, connection)
        Dialog.exec_()
        #self.serverThread.start()


    def doubleClickHandler(self):
        if not self.treeWidget.currentItem().parent():  # parent exist
            username = self.treeWidget.currentItem().text(0)
            print ("Username: {}".format(username))
            connection = self.createConnection("client", username)
            self.openUserWindow(username, connection)

    def treeSelection(self):
        self.pushButtonEnter.setEnabled(True)
        self.pushButtonRemUser.setEnabled(True)
        getSelected = self.treeWidget.selectedItems()
        if self.treeWidget.currentItem().parent():  # parent exist
            print (getSelected[0].text(0))
        else:
            self.treeWidget.collapseAll()
            self.treeWidget.expandItem(self.treeWidget.currentItem())
            print ("Knut bezrodzica")

    def pbsettings(self):
        Dialog = QtWidgets.QDialog()
        ui = UIsettings.Ui_Dialog_Settings()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def createConnection(self, connectionSide, username):

        if connectionSide == "server":
            serverIp = utility.settings.settings["serverIp"]
            serverPort = utility.settings.settings["serverPort"]
            connection = ClassConnection.Connection("server", serverIp, int(serverPort))
            return connection
        else:  # else if we want a client connection
            id = utility.db.getId(username)
            ip = utility.db.saved_user[id][1]
            port = utility.db.saved_user[id][2]
            connection = ClassConnection.Connection("client", ip, int(port))
            return connection

    def serverWaitForConnection(self):
        ip = utility.settings.settings["serverIp"]
        port = utility.settings.settings["serverPort"]
        self.labelServerStatus.setText("Server Online on {}:{}".format(ip,port))
        self.serverWaitingConnection = self.createConnection("server", "")
        self.labelServerStatus.setText("Server Busy")
        self.openUserWindow(connection.connection_ip, connection)
