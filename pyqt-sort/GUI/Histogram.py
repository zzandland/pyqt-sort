import sys
from typing import List
from random import randint
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget
from PyQt5.QtTest import QTest
from algorithms import insertion_sort, bubble_sort, selection_sort, quick_sort, merge_sort

class Histogram(QWidget):

    def __init__(self, data: List[int], h: int, w: int):
        super(Histogram, self).__init__()

        self.i = self.j = -1
        self.h = h
        self.w = w
        self.data = data
        self.rectangles = self.data2QRect(self.data)

        self.algorithms = {
            'bubble': bubble_sort.BubbleSort,
            'insertion': insertion_sort.InsertionSort,
            'selection': selection_sort.SelectionSort,
            'quick': quick_sort.QuickSort,
            'merge': merge_sort.MergeSort
        }

        self.algorithm = None
        self.changeAlgorithm('bubble')
        self.stop = False

        self.show()

    def changeAlgorithm(self, algo: str) -> None:
        self.stop = True
        self.algorithm = self.algorithms[algo]
        self.iterator = self.algorithm(self.data)

    def randomize(self) -> None:
        self.stop = False
        self.iterator = self.algorithm(self.data)
        for i in range(len(self.data)):
            if self.stop: return
            idx = randint(0, i)
            self.data[i], self.data[idx] = self.data[idx], self.data[i]
            self.rectangles = self.data2QRect(self.data)
            self.update()
            QTest.qWait(1)

    def sort(self) -> None:
        self.i = self.j = -1
        while not self.stop and self.iterator.hasNext():
            self.i, self.j = self.iterator.getPointers()
            self.data = self.iterator.next()
            self.rectangles = self.data2QRect(self.data)
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
        thick = self.w // len(data)
        x = 0
        for val in data:
            tall = round((val / mxHeight) * self.h)
            res.append(QRect(x, self.h - tall, thick, tall))
            x += thick
        return res
