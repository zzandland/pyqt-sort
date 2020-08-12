from typing import List
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self, data: List[int]):
        super().__init__()

        self.data = data
        self.height = 400
        self.width = 800
        self.padding = 10

        self.resize(self.width, self.height)
        self.setStyleSheet('background-color: black')

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))

        painter.drawRect(y, x, 100, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window([])
    app.exec_()
