import sys
from PyQt5.QtWidgets import *
from GUI.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    data = [3,8,2,1,9,0,2,4,6,2,1]
    ui = MainWindow(data)

    app.exec_()
