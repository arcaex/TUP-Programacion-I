from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("radio.ui", self)
        self.opcion1.toggled.connect(self.on_toggled)
        self.opcion2.toggled.connect(self.on_toggled)
        self.opcion3.toggled.connect(self.on_toggled)

    def on_toggled(self):
        print("Cambio de estado")
        if self.opcion1.isChecked():
            self.etiqueta.setText("Se elige la opcion 1")
        elif self.opcion2.isChecked():
            self.etiqueta.setText("Se elige la opcion 2")
        elif self.opcion3.isChecked():
            self.etiqueta.setText("Se elige la opcion 3")

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
