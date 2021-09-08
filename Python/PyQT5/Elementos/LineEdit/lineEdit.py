from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("lineEdit.ui", self)
        self.click_button.clicked.connect(self.changeText)
    
    def changeText(self):
        texto = self.edit_texto.text()
        self.label_texto.setText(texto)

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
