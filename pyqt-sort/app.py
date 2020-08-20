import sys
from random import randint
from PyQt5.QtWidgets import *
from GUI.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    N = 200
    data = [i+1 for i in range(N)]
    for i in range(N-1, -1, -1):
        j = randint(0, i)
        data[i], data[j] = data[j], data[i]

    ui = MainWindow(data)

    app.exec_()
