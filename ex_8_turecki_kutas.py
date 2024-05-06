from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

form, widget = uic.loadUiType('ex_8_turek.ui') #tu zmień plik ui i usun komentarz

class MyWindow(widget, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_off.setEnabled(False)
        self.pb_write.setEnabled(False)
        
    @pyqtSlot()
    def on_pb_on_clicked(self):
        self.pb_off.setEnabled(True)
        self.pb_write.setEnabled(True)
        self.pb_on.setEnabled(False)
        self.label_button.setText('LAST BUTTON: ON')
    
    @pyqtSlot()
    def on_pb_off_clicked(self):
        self.pb_off.setEnabled(False)
        self.pb_write.setEnabled(False)
        self.pb_on.setEnabled(True)
        self.label_button.setText('LAST BUTTON: OFF')
    
    @pyqtSlot()
    def on_pb_write_clicked(self):
        text = self.le_text.text()
        self.label_text.setText(f'TEXT WROTE: {text}')
        self.le_text.setText('')
        self.label_button.setText('LAST BUTTON: Write')



  


if __name__=='__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()