from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import random 

form, widget = uic.loadUiType('ex9_kacper.ui') # tu zmienic

class MyWindow(widget, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table.setRowCount(25)

    @pyqtSlot()
    def on_gen_clicked(self):
        for i in range(25):
            item = QTableWidgetItem(str(random.randint(0,100)))
            self.table.setItem(i, 0, item)

    @pyqtSlot()
    def on_save_clicked(self):
        filename = self.output.text()
        with open(filename, 'w') as f:
            for i in range(25):
                item = self.table.item(i, 0).text()
                f.write(item + ';')
    
    @pyqtSlot()
    def on_open_clicked(self):
        filename = self.input.text()
        with open(filename, 'r') as f:
            items = f.read().split(';')
            print(items)

            for i in range(25):
                item = QTableWidgetItem(items[i])
                self.table.setItem(i, 0, item)


if __name__=='__main__':
    app = QApplication([])
    wnd = MyWindow()
    wnd.show()
    app.exec()