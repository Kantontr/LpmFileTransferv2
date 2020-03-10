#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

from modules import utility
# from modules import settings
#from modules import ClassClientConnection
# from modules import ClassServerConnection
# from modules import LPMRsaEncrypt
from ui import UImainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

def main():

    utility.stylesheet.setStyle("dark")

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    MainWindow = QtWidgets.QMainWindow()
    ui = UImainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




    # settings = settings.Settings()
    # db = database.Database()
    # db.printDatabase()

    # test = LPMRsaEncrypt.LPMRsaEncrypt()
    # enc = test.encryptLine("WikiKnut")
    # print ("Enc: {}".format(enc))
    # dec = test.decryptLine(enc)
    # print ("Dec: {}".format(dec))
    # print(db.AddUser("Knut", "Ipknuta", "PortKnuta", "Knuteusz"))
    # print(db.AddUser("Knut2", "Ipknuta2", "PortKnuta2", ""))
    # print(db.AddUser("Knut3", "Ipknuta3", "PortKnuta3", ""))
    # print(db.AddUser("Knut4", "Ipknuta4", "PortKnuta4", ""))

    # db.LoadDatabaseFromFile()
    # try:
    #testClient = ClassClientConnection.ClientConnection("komp2", "192.168.1.3", "50001")
    # try:
    #testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v.mp4", "")
    #testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v2.jpg", "")
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v4.txt", "")
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v5.txt", "")
    #testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v3.jpg", "")
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\LPM_TCP.exe", "")
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v4.mp4", "")
    # finally:
    # testClient.endConnection()
    #print ("Main.py: I'm Alive!")


# except:
#   print ("Connection error")


if __name__ == '__main__':
    main()
