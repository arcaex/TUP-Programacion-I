from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana.ui", self)

class MiVentana2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana2.ui", self)
        self.boton_clickAca.clicked.connect(self.on_click)
        self.opcion1.toggled.connect(self.change_button)
        self.opcion2.toggled.connect(self.change_button)
        self.opcion3.toggled.connect(self.change_button)
    
    def on_click(self):
        numero1 = int(self.numero1.text())
        numero2 = int(self.numero2.text())
        if(self.opcion1.isChecked()):
            self.resultado.setText(str(numero1+numero2))
        elif (self.opcion2.isChecked()):
            self.resultado.setText(str(numero1*numero2))
        elif (self.opcion3.isChecked()):
            self.resultado.setText(str(numero1/numero2))

    def change_button(self):
        if(self.opcion1.isChecked()):
            self.boton_clickAca.setText("Sumar")
        elif (self.opcion2.isChecked()):
            self.boton_clickAca.setText("Multiplicar")
        elif (self.opcion3.isChecked()):
            self.boton_clickAca.setText("Dividir")
    

app = QApplication([])

win2 = MiVentana2()
win2.show()

app.exec_()

