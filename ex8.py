from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

form, widget = uic.loadUiType('ex8.ui')

class MyWindow(widget, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
  

    @pyqtSlot()
    def on_pb_1_clicked(self):
        print('label 1 changed')
        text = self.le_input.text()
        self.label_1.setText(text)
 

    @pyqtSlot()
    def on_pb_2_clicked(self):
        print('label 2 changed')
        text = self.le_input.text()
        self.label_2.setText(text)


    @pyqtSlot()
    def on_pb_3_clicked(self):
        print('Reset')
        text = self.le_input.setText('')




if __name__=='__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()