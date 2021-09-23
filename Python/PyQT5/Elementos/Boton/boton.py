from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randint


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("boton.ui", self)
        #Definir de que forma el elemento BOTON espera un evento click y que dispara dicho evento.
        self.boton.clicked.connect(self.print_click)
        self.entrar.pressed.connect(self.pressed)
        self.entrar.released.connect(self.on_clicked)

    def print_click(self):
        print("click!")

    def pressed(self):
        print("presionado")

    def released(self):
        print("soltado")

    def on_clicked(self):
        valorDado = randint(1,6)
        print(self.etiqueta.text())
        self.etiqueta.setText(str(valorDado)) 

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
