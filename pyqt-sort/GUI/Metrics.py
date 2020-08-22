from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from constants import ALGORITHMS

class Metrics(QLabel):

    def __init__(self, algo: str, stop: bool, time: float = 0):
        super().__init__()

        self.algo = algo
        self.stop = stop
        self.time = time

        self.setGeometry(50, 10, 400, 30)
        self.setAlignment(Qt.AlignTop)
        self.setStyleSheet('color: white; background-color: rgba(0,0,0,0%)')
        self.updateText()

        self.show()

    def updateText(self):
        text = 'Selected algorithm: %s' % ALGORITHMS[self.algo]
        if not self.stop: text += '\nRunning time: %f sec' % self.time
        self.setText(text)
