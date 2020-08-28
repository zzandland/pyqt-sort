import sys
from constants import ALGORITHMS
from GUI.Histogram import Histogram
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.h = 512
        self.w = 1024
        self.N = 128
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
        self.addMenuItem(samples, '128', 'sample_size')
        self.addMenuItem(samples, '256', 'sample_size')
        self.addMenuItem(samples, '512', 'sample_size')

        algorithms = menubar.addMenu('Algorithms')
        self.addMenuItem(algorithms, 'bubble', 'algorithm')
        self.addMenuItem(algorithms, 'insertion', 'algorithm')
        self.addMenuItem(algorithms, 'binary_insertion', 'algorithm')
        self.addMenuItem(algorithms, 'selection', 'algorithm')
        self.addMenuItem(algorithms, 'quick', 'algorithm')
        self.addMenuItem(algorithms, 'merge', 'algorithm')
        self.addMenuItem(algorithms, 'heap', 'algorithm')
        self.addMenuItem(algorithms, 'cycle', 'algorithm')
        self.addMenuItem(algorithms, 'optimized_cycle', 'algorithm')

    def addMenuItem(self, menu: object, item: str, category: str) -> None:
        if category == 'algorithm':
            new = QAction(ALGORITHMS[item][0], self)
            new.triggered.connect(lambda: self.diagram.changeAlgorithm(item))
            menu.addAction(new)
        elif category == 'sample_size':
            new = QAction(item, self)
            new.triggered.connect(lambda: self.diagram.changeSampleNumber(int(item)))
            menu.addAction(new)
