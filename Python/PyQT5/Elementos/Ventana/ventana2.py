from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana.ui", self)