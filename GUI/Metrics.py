from constants import ALGORITHMS
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

class Metrics(QLabel):

    def __init__(self, algo: str, stop: bool, time: float = 0):
        super().__init__()

        self.algo = algo
        self.stop = stop
        self.time = time

        self.setGeometry(30, 0, 400, 30)
        self.setAlignment(Qt.AlignTop)
        self.setStyleSheet('color: white; background-color: rgba(0,0,0,0%)')
        self.updateText()

        self.show()

    def updateText(self):
        text = ALGORITHMS[self.algo][0]
        if not self.stop: text += ': %f sec' % self.time
        self.setText(text)
