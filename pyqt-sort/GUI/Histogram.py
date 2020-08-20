import sys
from typing import List
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest
from algorithms import insertion_sort, bubble_sort, selection_sort, quick_sort

class Histogram(QWidget):

    def __init__(self, data: List[int], height: int, width: int):
        super(Histogram, self).__init__()

        self.height = height
        self.width = width
        self.iterator = insertion_sort.InsertionSort(data)
        self.i = self.j = -1
        self.rectangles = self.data2QRect(data)

        self.resize(self.width, self.height)
        self.setStyleSheet('background-color: black')

        self.show()
        self.sort()

    def sort(self) -> None:
        while self.iterator.hasNext():
            self.i, self.j = self.iterator.getPointers()
            self.rectangles = self.data2QRect(self.iterator.next())
            self.update()
            QTest.qWait(1)

        self.i = self.j = -1
        self.update()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)

        for i, rectangle in enumerate(self.rectangles):
            color = Qt.red if i in (self.i, self.j) else Qt.white
            painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
            painter.drawRect(rectangle)
            painter.fillRect(rectangle, QBrush(color, Qt.SolidPattern))

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
