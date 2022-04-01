from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("menu.ui", self)
        self.boton1.clicked.connect(self.on_Click_Boton1)
        self.boton2.clicked.connect(self.on_Click_Boton2)

    def on_Click_Boton1(self):
        print("Click Boton 1")
    
    def on_Click_Boton2(self):
        print("Click Boton 2")