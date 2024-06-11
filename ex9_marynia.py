from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import random 

form, widget = uic.loadUiType('ex9_marynia.ui') # tu zmienic

class MyWindow(widget, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tb.setRowCount(10)

    
    @pyqtSlot()
    def on_new_num_clicked(self):
        for i in range(10):
            row = QTableWidgetItem(str(random.random()))
            self.tb.setItem(i, 0, row)


    @pyqtSlot()
    def on_save_clicked(self):
        with open('file.txt', 'w') as file:
            for i in range(10):
                number = self.tb.item(i, 0).text()
                file.write(number + ' ')
    
    @pyqtSlot()
    def on_open_clicked(self):

        with open('file.txt', 'r') as file:
            numbers = file.read()
            num_list = numbers.split(' ')
            print(numbers)

            for i in range(10):
                row = QTableWidgetItem(num_list[i])
                self.tb.setItem(i, 0, row)







if __name__=='__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()