import sys
from constants import ALGORITHMS
from GUI.Histogram import Histogram
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.h = 500
        self.w = 1000
        self.N = 100
        self.setFixedSize(self.w, self.h)
        self.setStyleSheet('background-color: black')

        self.diagram = Histogram(self.N, self.h, self.w)
        self.setCentralWidget(self.diagram)
        self.genMenuBar()
        self.show()

    def genMenuBar(self) -> None:
        menubar = self.menuBar()

        action = menubar.addMenu('Action')

        start = QAction('Start', self)
        start.triggered.connect(self.diagram.start)
        action.addAction(start)

        stop = QAction('Stop', self)
        stop.triggered.connect(self.diagram.end)
        action.addAction(stop)

        samples = menubar.addMenu('Samples')
        one = QAction('100', self)
        one.triggered.connect(lambda: self.diagram.changeSampleNumber(100))
        samples.addAction(one)
        two = QAction('225', self)
        two.triggered.connect(lambda: self.diagram.changeSampleNumber(225))
        samples.addAction(two)
        five = QAction('500', self)
        five.triggered.connect(lambda: self.diagram.changeSampleNumber(500))
        samples.addAction(five)

        algorithms = menubar.addMenu('Algorithms')

        bubble = QAction(ALGORITHMS['bubble'][0], self)
        bubble.triggered.connect(lambda: self.diagram.changeAlgorithm('bubble'))
        algorithms.addAction(bubble)

        insertion = QAction(ALGORITHMS['insertion'][0], self)
        insertion.triggered.connect(lambda: self.diagram.changeAlgorithm('insertion'))
        algorithms.addAction(insertion)

        selection = QAction(ALGORITHMS['selection'][0], self)
        selection.triggered.connect(lambda: self.diagram.changeAlgorithm('selection'))
        algorithms.addAction(selection)

        quick = QAction(ALGORITHMS['quick'][0], self)
        quick.triggered.connect(lambda: self.diagram.changeAlgorithm('quick'))
        algorithms.addAction(quick)

        merge = QAction(ALGORITHMS['merge'][0], self)
        merge.triggered.connect(lambda: self.diagram.changeAlgorithm('merge'))
        algorithms.addAction(merge)

        heap = QAction(ALGORITHMS['heap'][0], self)
        heap.triggered.connect(lambda: self.diagram.changeAlgorithm('heap'))
        algorithms.addAction(heap)
