import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication


class ProgressBar(QWidget):
    def __init__(self,title,label):
        super().__init__()
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(10, 10, 340, 25)
        self.setWindowTitle(title)
        self.resize(350, 70)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 35, 330, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setText(label)

    def setValue(self, value):
        self.progressBar.setValue(value)
        QApplication.processEvents()
        self.raise_()

    #def setText(self,title,label):

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     demo = ProgressBar("Knut","Kufa")
#     demo.show()
#
#     sys.exit(app.exec_())
