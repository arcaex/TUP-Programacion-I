from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("lista.ui", self)
        self.agregar.clicked.connect(self.on_agregar)
        self.quitar.clicked.connect(self.on_quitar)
        self.lista.clicked.connect(self.on_click)
        self.quitar_todos.clicked.connect(self.remove_all)

    def on_click(self):
        print(self.lista.currentItem().text())

    def on_agregar(self):
        self.lista.addItem(self.nombre.text())
        self.nombre.setText('')

    def on_quitar(self):
        self.lista.takeItem(self.lista.currentRow())

    def remove_all(self):
        self.lista.clear()

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
