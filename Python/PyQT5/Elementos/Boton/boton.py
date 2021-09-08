from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randint


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("boton.ui", self)
        #Definir de que forma el elemento BOTON espera un evento click y que dispara dicho evento.
        self.boton.clicked.connect(self.on_clicked)
        self.boton.clicked.connect(self.print_click)

    def print_click(self):
        print("click!")

    def on_clicked(self):
        valorDado = randint(1,6)
        self.etiqueta.setText(str(valorDado)) 

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
