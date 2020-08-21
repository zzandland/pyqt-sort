import sys
from typing import List
from PyQt5.QtWidgets import *

from GUI.Histogram import Histogram

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.h = 700
        self.w = 1200
        self.N = 100
        self.setFixedSize(self.w, self.h)

        self.genMenuBar()

        self.data = [i+1 for i in range(self.N)]
        self.diagram = Histogram(self.data, self.h, self.w)

        self.setCentralWidget(self.diagram)

        self.show()

    def genMenuBar(self) -> None:
        menubar = self.menuBar()
        file = menubar.addMenu('File')
        start = QAction('Start', self)
        stop = QAction('Stop', self)
        file.addAction(start)
        file.addAction(stop)
        start.triggered.connect(self.start)
        stop.triggered.connect(self.stop)

        algorithms = menubar.addMenu('Algorithms')

        bubble = QAction('Bubble Sort', self)
        algorithms.addAction(bubble)

    def start(self) -> None:
        self.diagram.stop = False
        self.diagram.randomize()
        self.diagram.sort()

    def stop(self) -> None:
        self.diagram.stop = True
