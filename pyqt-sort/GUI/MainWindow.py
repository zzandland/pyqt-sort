import sys
from typing import List
from PyQt5.QtWidgets import *

from GUI.Histogram import Histogram

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.h = 700
        self.w = 1200
        self.N = 150
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
        start.triggered.connect(self.start)
        file.addAction(start)

        stop = QAction('Stop', self)
        stop.triggered.connect(self.stop)
        file.addAction(stop)

        algorithms = menubar.addMenu('Algorithms')

        bubble = QAction('Bubble Sort', self)
        bubble.triggered.connect(lambda: self.diagram.changeAlgorithm('bubble'))
        algorithms.addAction(bubble)

        insertion = QAction('Insertion Sort', self)
        insertion.triggered.connect(lambda: self.diagram.changeAlgorithm('insertion'))
        algorithms.addAction(insertion)

        selection = QAction('Selection Sort', self)
        selection.triggered.connect(lambda: self.diagram.changeAlgorithm('selection'))
        algorithms.addAction(selection)

        quick = QAction('Quick Sort', self)
        quick.triggered.connect(lambda: self.diagram.changeAlgorithm('quick'))
        algorithms.addAction(quick)

        merge = QAction('Merge Sort', self)
        merge.triggered.connect(lambda: self.diagram.changeAlgorithm('merge'))
        algorithms.addAction(merge)

    def start(self) -> None:
        self.diagram.stop = False
        self.diagram.randomize()
        self.diagram.sort()

    def stop(self) -> None:
        self.diagram.stop = True
