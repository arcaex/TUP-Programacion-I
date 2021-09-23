from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("lineEdit.ui", self)
        self.click_button.clicked.connect(self.changeText)
        self.edit_texto.returnPressed.connect(self.changeText)
        self.edit_texto.textChanged.connect(self.changeEdit)
    
    def changeText(self):
        texto = self.edit_texto.text()
        self.label_texto.setText(texto)

    def changeEdit(self):
        if len(self.edit_texto.text())==10:
            print("Logitud superada")
            self.edit_texto.setText("")

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
