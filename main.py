#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
from ui import UImainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

def main():

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    MainWindow = QtWidgets.QMainWindow()
    ui = UImainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
