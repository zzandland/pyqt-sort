import sys
from typing import List
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest

class Histogram(QWidget):

    def __init__(self, data: List[int], height: int, width: int):
        super(Histogram, self).__init__()

        self.height = height
        self.width = width
        self.data = data
        self.i = self.j = -1
        self.rectangles = self.data2QRect(self.data)

        self.resize(self.width, self.height)
        self.setStyleSheet('background-color: black')

        self.show()

        self.sort()

    def sort(self) -> None:
        N = len(self.data)
        for i in range(N):
            for j in range(i):
                self.i, self.j = i, j
                if self.data[i] < self.data[j]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
                self.rectangles = self.data2QRect(self.data)
                self.update()
                QTest.qWait(500)
        self.i = self.j = -1
        self.update()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)

        for i, rectangle in enumerate(self.rectangles):
            if i in (self.i, self.j): painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
            else: painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))
            painter.drawRect(rectangle)

    def data2QRect(self, data: List[int]) -> List[QRect]:
        res = []
        mxHeight = max(data)
        thick = self.width // len(data) - 1
        x = 10
        for val in data:
            tall = round((val / mxHeight) * self.height)
            res.append(QRect(x, self.height - tall, thick, tall))
            x += thick
        return res
