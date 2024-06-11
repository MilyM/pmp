from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import random 

form, widget = uic.loadUiType('ex09.ui') 

class MyWindow(widget, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.rows_number = None

    
    @pyqtSlot()
    def on_pb_generate_clicked(self):
        # print('clicked')
        self.rows_number = random.randint(1, 100)
        self.table.setRowCount(self.rows_number)

        for i in range(self.rows_number):
            row = QTableWidgetItem(str(random.randint(0, 10000)))
            self.table.setItem(i, 0, row)


    @pyqtSlot()
    def on_pb_save_clicked(self):
        filename = self.le_file.text()
        lines = [self.table.item(i, 0).text() + '\n' for i in range(self.rows_number)]
        with open(filename, 'w') as file:
            file.writelines(lines)

    
    @pyqtSlot()
    def on_pb_open_clicked(self):
        filename = self.le_open.text()

        with open(filename, 'r') as file:
            lines = file.readlines()
            self.numbers = [line.replace('\n', '') for line in lines]
        
        self.rows_number = len(self.numbers)
        self.table.setRowCount(self.rows_number)
        
        for i, number in enumerate(self.numbers):
            row = QTableWidgetItem(number)
            self.table.setItem(i, 0, row)







if __name__=='__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()