from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("message_box.ui", self)
        self.mensaje.clicked.connect(self.on_mensaje)

    def on_mensaje(self):
        msg = QMessageBox()
        msg.setWindowTitle('Titulo de mensaje')
        msg.setText('Este es un mensaje')
        # msg.setIcon(QMessageBox.Critical)
        # msg.setIcon(QMessageBox.Warning)
        # msg.setIcon(QMessageBox.Information)
        msg.setIcon(QMessageBox.Question)
        # msg.setStandardButtons(
        # QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel | QMessageBox.Ok | QMessageBox.Open | QMessageBox.Close | QMessageBox.Save | QMessageBox.SaveAll | QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore)
        msg.setStandardButtons(
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        respuesta = msg.exec_()
        if respuesta == QMessageBox.Yes:
            print('Se eligio si')
        elif respuesta == QMessageBox.No:
            print('Se eligio no')
        else:
            print('Se eligio cancelar')


app = QApplication([])

win = MiVentana()
win.show()

app.exec_()
