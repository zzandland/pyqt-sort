import sys
from GUI.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    app.exec_()
