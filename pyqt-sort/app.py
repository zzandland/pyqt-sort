import sys
from PyQt5.QtWidgets import QApplication
from GUI.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    app.exec_()
