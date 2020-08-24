from constants import ALGORITHMS
from GUI.Metrics import Metrics
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget
from PyQt5.QtTest import QTest
from random import randint
from timeit import default_timer as timer
from typing import List

class Histogram(QWidget):

    def __init__(self, N: int, h: int, w: int):
        super().__init__()

        self.i = self.j = -1
        self.h = h
        self.w = w
        self.N = N
        self.data = [i+1 for i in range(self.N)]
        self.rectangles = self.data2QRect()

        self.algo = 'bubble'
        self.stop = True

        self.metrics = Metrics(self.algo, self.stop)
        self.metrics.setParent(self)

        self.changeAlgorithm(self.algo)

        self.startTime = self.endTime = timer()

        self.show()

    def changeSampleNumber(self, N: int) -> None:
        self.stop = True
        self.metrics.stop = True
        self.metrics.updateText()
        self.N = N
        self.data = [i+1 for i in range(self.N)]
        self.rectangles = self.data2QRect()
        self.update()

    def changeAlgorithm(self, algo: str) -> None:
        self.end()
        self.algo = algo
        self.metrics.algo = algo
        self.metrics.updateText()

    def start(self) -> None:
        self.stop = False
        self.iterator = ALGORITHMS[self.algo][1](self.data)
        self.randomize()
        self.startTime = timer()
        self.sort()

    def end(self) -> None:
        self.stop = True
        self.metrics.stop = True
        self.metrics.updateText()
        self.changeSampleNumber(self.N)

    def randomize(self) -> None:
        self.stop = False
        for i in range(len(self.data)):
            self.i = i
            if self.stop: return
            idx = randint(0, i)
            self.data[i], self.data[idx] = self.data[idx], self.data[i]
            self.rectangles = self.data2QRect()
            self.update()
            QTest.qWait(1)

    def sort(self) -> None:
        self.i = self.j = -1
        self.metrics.stop = False
        while not self.stop and self.iterator.hasNext():
            self.i, self.j = self.iterator.getPointers()
            self.data = self.iterator.next()
            self.rectangles = self.data2QRect()
            self.update()
            self.metrics.time = timer() - self.startTime
            self.metrics.updateText()
            QTest.qWait(1)

        self.i = self.j = -1
        self.update()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)

        for i, rectangle in enumerate(self.rectangles):
            color = Qt.red if i in (self.i, self.j) else Qt.darkGray
            painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
            painter.drawRect(rectangle)
            painter.fillRect(rectangle, QBrush(color, Qt.SolidPattern))

    def data2QRect(self) -> List[QRect]:
        res = []
        thick = self.w // self.N
        x = 0
        for val in self.data:
            tall = int((val / (self.N+1)) * self.h)
            res.append(QRect(x, self.h - tall, thick, tall))
            x += thick
        return res
