# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from modules import utility
from ui import UIuserMessageWindow, UIsettings
import sys


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
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 411, 581))
        self.treeWidget.setMaximumSize(QtCore.QSize(411, 581))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")

        self.pushButtonAddUser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddUser.setGeometry(QtCore.QRect(430, 40, 51, 51))
        self.pushButtonAddUser.setObjectName("pushButtonAddUser")
        self.pushButtonAddUser.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonAddUser.setIcon(QtGui.QIcon("icons\\addUser.svg"))
        self.pushButtonAddUser.setIconSize(QtCore.QSize(40, 40))

        self.pushButtonRemUser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemUser.setGeometry(QtCore.QRect(430, 100, 51, 51))
        self.pushButtonRemUser.setObjectName("pushButtonRemUser")
        self.pushButtonRemUser.setStyleSheet(utility.stylesheet.style["button"])
        self.pushButtonRemUser.setIcon(QtGui.QIcon("icons\\removeUser.svg"))
        self.pushButtonRemUser.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonRemUser.setEnabled(0)

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LPM Transfer v2"))

        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Online Users"))
        self.treeWidget.setStyleSheet(utility.stylesheet.style["tree"])
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setAlternatingRowColors(True)
        # self.treeWidget.setIcon(QtGui.QIcon("icons\\exit.svg"))
        # self.treeWidget.setIconSize(QtCore.QSize(40, 40))

        font = QtGui.QFont()
        font.setPointSize(13)

        for i in utility.db.saved_user:
            ntw = QtWidgets.QTreeWidgetItem(self.treeWidget, [utility.db.saved_user[i][0]])
            QtWidgets.QTreeWidgetItem(ntw, [utility.db.saved_user[i][1]]).setFont(0, font)
            QtWidgets.QTreeWidgetItem(ntw, [utility.db.saved_user[i][2]]).setFont(0, font)
            QtWidgets.QTreeWidgetItem(ntw, [utility.db.saved_user[i][3]]).setFont(0, font)

    def quit(self):
        sys.exit()

    def openUserWindow(self):
        if self.treeWidget.selectedItems():  # if an item is selected

            if self.treeWidget.currentItem().parent():  # parent exist
                username = self.treeWidget.currentItem().parent().text(0)
            else:
                username = self.treeWidget.currentItem().text(0)
            Dialog = QtWidgets.QDialog()
            ui = UIuserMessageWindow.Ui_Dialog_UserMsg()
            ui.setupUi(Dialog, username)
            Dialog.exec_()

        else:
            return

    def doubleClickHandler(self):
        if not self.treeWidget.currentItem().parent():  # parent exist
            username = self.treeWidget.currentItem().text(0)
            print ("Username: {}".format(username))
            self.openUserWindow()

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
