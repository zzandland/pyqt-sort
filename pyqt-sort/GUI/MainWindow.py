import sys
from constants import ALGORITHMS, BLACKLIST
from GUI.Histogram import Histogram
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.h = 512
        self.w = 1024
        self.N = 128
        self.blackList = []
        self.dup = False
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
        dup = QAction('Allow Duplicate Values', self, checkable=True)
        dup.triggered.connect(lambda: self.toggleDuplicate())
        samples.addAction(dup)
        self.addMenuItem(samples, '128', 'sample_size')
        self.addMenuItem(samples, '256', 'sample_size')
        self.addMenuItem(samples, '512', 'sample_size')

        algorithms = menubar.addMenu('Algorithms')
        for algo in ALGORITHMS:
            self.addMenuItem(algorithms, algo, 'algorithm')

    def toggleDuplicate(self) -> None:
        self.dup = not self.dup
        self.diagram.dup = self.dup
        self.diagram.end()
        for action in self.blackList:
            action.setEnabled(not self.dup)

    def addMenuItem(self, menu: object, item: str, category: str) -> None:
        if category == 'algorithm':
            new = QAction(ALGORITHMS[item][0], self)
            new.triggered.connect(lambda: self.diagram.changeAlgorithm(item))
            menu.addAction(new)
            if item in BLACKLIST: self.blackList.append(new)
        elif category == 'sample_size':
            new = QAction(item, self)
            new.triggered.connect(lambda: self.diagram.changeSampleNumber(int(item)))
            menu.addAction(new)
