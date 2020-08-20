import sys
from typing import List
from PyQt5.QtWidgets import *

from GUI.Histogram import Histogram

class MainWindow(QMainWindow):

    def __init__(self, data: List[int]):
        super(MainWindow, self).__init__()

        self.height = 500
        self.width = 1000
        self.data = data

        self.resize(self.width, self.height)
        diagram = Histogram(self.data, self.height, self.width)

        self.setCentralWidget(diagram)

        self.show()
