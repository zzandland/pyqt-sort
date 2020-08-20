import sys
from typing import List
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import *

class Histogram(QWidget):

    def __init__(self, data: List[int], height: int, width: int):
        super(Histogram, self).__init__()

        self.height = height
        self.width = width
        self.rectangles = self.data2QRect(data)
        print(data)
        print(self.rectangles)

        self.resize(self.width, self.height)
        self.setStyleSheet('background-color: black')

        self.show()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))

        for rectangle in self.rectangles:
            painter.drawRect(rectangle)

    def data2QRect(self, data: List[int]) -> List[QRect]:
        res = []
        mxHeight = max(data)
        thick = self.width // len(data)
        x = 0
        for val in data:
            tall = round((val / mxHeight) * self.height)
            res.append(QRect(x, self.height - tall, thick, tall))
            x += thick
        return res
