# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from modules import utility
from gui import userMessageWindow
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        utility.db.loadDatabaseFromFile()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 581)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)

        #Style sheet
        self.style = utility.stylesheet.dark["background"]
        MainWindow.setStyleSheet(self.style)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")


        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 411, 581))
        self.treeWidget.setMaximumSize(QtCore.QSize(411, 581))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")

        self.pushButtonAddUser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddUser.setGeometry(QtCore.QRect(430, 40, 51, 51))
        self.pushButtonAddUser.setObjectName("pushButtonAddUser")
        self.pushButtonAddUser.setStyleSheet(utility.stylesheet.dark["button"])

        self.pushButtonRemUser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemUser.setGeometry(QtCore.QRect(430, 100, 51, 51))
        self.pushButtonRemUser.setObjectName("pushButtonRemUser")
        self.pushButtonRemUser.setStyleSheet(utility.stylesheet.dark["button"])

        self.pushButtonSettings = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSettings.setGeometry(QtCore.QRect(430, 220, 51, 51))
        self.pushButtonSettings.setObjectName("pushButtonSettings")
        self.pushButtonSettings.setStyleSheet(utility.stylesheet.dark["button"])

        self.pushButtonEnter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEnter.setGeometry(QtCore.QRect(430, 160, 51, 51))
        self.pushButtonEnter.setObjectName("pushButtonEnter")
        self.pushButtonEnter.setStyleSheet(utility.stylesheet.dark["button"])

        self.pushButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(430, 480, 51, 51))
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.pushButtonExit.setStyleSheet(utility.stylesheet.dark["button"])

        self.treeWidget.clicked.connect(self.pt)
        self.treeWidget.itemDoubleClicked.connect(self.doubleClickHandler)
        self.pushButtonExit.clicked.connect(self.test)
        self.pushButtonEnter.clicked.connect(self.openUserWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LPM Transfer v2"))

        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Online Users"))
        self.treeWidget.setStyleSheet(utility.stylesheet.dark["tree"])
        self.treeWidget.setSortingEnabled(False)

        for i in utility.db.saved_user:
            ntw = QtWidgets.QTreeWidgetItem(self.treeWidget,[utility.db.saved_user[i][0]])
            QtWidgets.QTreeWidgetItem(ntw, [utility.db.saved_user[i][1]])
            QtWidgets.QTreeWidgetItem(ntw, [utility.db.saved_user[i][2]])
            QtWidgets.QTreeWidgetItem(ntw, [utility.db.saved_user[i][3]])


        self.pushButtonAddUser.setText(_translate("MainWindow", "+"))
        self.pushButtonRemUser.setText(_translate("MainWindow", "-"))
        self.pushButtonSettings.setText(_translate("MainWindow", "Set"))
        self.pushButtonEnter.setText(_translate("MainWindow", "Ent"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))

    def test(self):
        sys.exit()

    def openUserWindow(self):
        if self.treeWidget.selectedItems(): #if an item is selected

            username = self.treeWidget.currentItem().text(0)
            app = QtWidgets.QApplication(sys.argv)
            Dialog = QtWidgets.QDialog()
            ui = userMessageWindow.Ui_Dialog()
            ui.setupUi(Dialog,username)
            Dialog.exec()
            sys.exit(app.exec_())


            print("OPEN")
        else:
            return

    def doubleClickHandler(self):
        if not self.treeWidget.currentItem().parent():  # parent exist
            username = self.treeWidget.currentItem().text(0)
            print ("Username: {}".format(username))
            self.openUserWindow()

    def pt(self):

        getSelected = self.treeWidget.selectedItems()
        #parents =  self.treeWidget.currentItem().parent()
        if self.treeWidget.currentItem().parent(): #parent exist
            print (getSelected[0].text(0))
        else:
            print ("Knut bezrodzica")

            #self.treeWidget.collapseAll()
            #self.treeWidget.expandItem(self.treeWidget.currentItem())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
