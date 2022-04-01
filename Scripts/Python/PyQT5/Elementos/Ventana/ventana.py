from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from ventana2 import MiVentana1

class MiVentana2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana2.ui", self)
        self.ventana_prueba = MiVentana1()
        self.boton_clickAca.clicked.connect(self.on_click)
        self.boton_cerrar.clicked.connect(self.on_cerrar)
    
    def on_click(self):
        self.ventana_prueba.show()

    def on_cerrar(self):
        self.ventana_prueba.hide()
    

app = QApplication([])

win2 = MiVentana2()
win2.show()

app.exec_()

