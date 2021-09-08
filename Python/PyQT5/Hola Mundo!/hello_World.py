from PyQt5 import QtWidgets, uic
import sys

template = uic.loadUiType("main.ui")[0]

class Ventana1(QtWidgets.QMainWindow,template):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana1()
    ventana.show()
    sys.exit()
