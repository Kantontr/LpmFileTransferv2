#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

from modules import database
from modules import settings
from modules import ClassClientConnection
from modules import ClassServerConnection


def main():
    Settings = settings.Settings()
    db = database.Database()
    db.loadDatabaseFromFile()
    db.printDatabase()
    # print(db.AddUser("Knut", "Ipknuta", "PortKnuta", "Knuteusz"))
    # print(db.AddUser("Knut2", "Ipknuta2", "PortKnuta2", ""))
    # print(db.AddUser("Knut3", "Ipknuta3", "PortKnuta3", ""))
    # print(db.AddUser("Knut4", "Ipknuta4", "PortKnuta4", ""))

    # db.LoadDatabaseFromFile()
    # try:
    testClient = ClassClientConnection.ClientConnection("komp2", "192.168.1.3", "50001")
    # try:
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v.mp4", "")
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v2.jpg", "")
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v4.txt", "")
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v5.txt", "")
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v3.jpg", "")
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\LPM_TCP.exe", "")
    # testClient.sendFile("C:\\Users\\kanton\\Desktop\\PythonFrom\\v4.mp4", "")
    # finally:
    # testClient.endConnection()
    print ("Main zyje")
    print ("Main zyje")
    print ("Main zyje")
    print ("Main zyje")
    print ("Main zyje")


# except:
#   print ("Connection error")


if __name__ == '__main__':
    main()
