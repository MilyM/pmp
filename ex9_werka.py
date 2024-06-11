from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import random 

form, widget = uic.loadUiType('ex9_werka.ui') # tu zmienic

class MyWindow(widget, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    @pyqtSlot()
    def on_random_clicked(self):
        self.size = random.randint(1, 10)
        self.table.setRowCount(self.size)
        for row in range(self.size):
            self.table.setItem(row, 0, QTableWidgetItem(str(random.randint(0,100))))

    @pyqtSlot()
    def on_write_clicked(self):
        file = self.lineEdit.text()
        with open(file, 'w') as file:
            file.write(str(self.size) + '\n')

            for row in range(self.size):
                file.write(self.table.item(row, 0).text() + '\n')
    
    @pyqtSlot()
    def on_read_clicked(self):
        file = self.lineEdit.text()
        with open(file, 'r') as file:
            all = file.readlines()
            all_num = [int(elem.replace('\n', '')) for elem in all]
            print(all_num)

            self.size = all_num[0]
            self.table.setRowCount(self.size)

            for row in range(1, self.size):
                self.table.setItem(row, 0, QTableWidgetItem(str(all_num[row])))


if __name__=='__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()