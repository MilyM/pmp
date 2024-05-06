from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

form, widget = uic.loadUiType('ex_8_werka.ui') #tu zmień plik ui i usun komentarz

class MyWindow(widget, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.result = 0
        self.label_result.setText(f'RESULT: {self.result}')

    @pyqtSlot()
    def on_pb_plus_clicked(self):
        value = int(self.le_in.text())
        self.result += value
        self.label_result.setText(f'RESULT: {self.result}')
        self.le_in.setText('')

    @pyqtSlot()
    def on_pb_minus_clicked(self):
        value = int(self.le_in.text())
        self.result -= value
        self.label_result.setText(f'RESULT: {self.result}')
        self.le_in.setText('')

    @pyqtSlot()
    def on_pb_reset_clicked(self):
        self.result = 0
        self.label_result.setText(f'RESULT: {self.result}')
  


if __name__=='__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()