from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("input_dialog.ui", self)
        self.ingresar.clicked.connect(self.on_ingresar)

    def on_ingresar(self):
        
        items = ['Rojo', 'Verde', 'Azul']
        item, ok = QInputDialog.getItem(
            self, 'Ingresar', 'Eliga un item', items, 1, False)
        if ok:
            self.entrada.setText(item)


app = QApplication([])

win = MiVentana()
win.show()

app.exec_()
