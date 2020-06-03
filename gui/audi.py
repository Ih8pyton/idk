from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sys
import os

class DevilMayCry(QMainWindow):

    def __init__(self):
        super(DevilMayCry, self).__init__()
        uic.loadUi('au.ui', self)

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(15)
        self.tableWidget.setHorizontalHeaderLabels(('Character','EDGEmeter','Weapon'))

        self.pushButton_2.clicked.connect(self.clear)
        self.tableWidget.setSortingEnabled(True)

        row = 0
        for item in range(0, 15):
            window = QTableWidgetItem(item)

            boxin = QtWidgets.QComboBox()
            boxin.addItem("SSS")
            boxin.addItem("SS")
            boxin.addItem("S")
            boxin.addItem("A")
            boxin.addItem("NOT STYLISH AT ALL")

            self.tableWidget.setItem(row, 0, window)
            self.tableWidget.setCellWidget(row, 1, boxin)
            row += 1

    def clear(self):
        self.tableWidget.clear()

def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = DevilMayCry()
    window.show() 
    app.exec_()
    
if __name__ == '__main__': 
    main()
