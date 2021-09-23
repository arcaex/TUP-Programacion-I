from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        self.backup.textChanged.connect(self.agregar_digito)
        self.boton1.clicked.connect(self.set_text_backup)

    def set_text_backup(self):
        self.backup.setText("")
        self.backup.setText("1")

    def agregar_digito(self):
        self.Calculo.setText(self.Calculo.text() + self.backup.text())



app = QApplication([])
win = MiVentana()
win.show()
app.exec_()