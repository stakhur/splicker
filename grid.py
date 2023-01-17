
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class GridWidget(QWidget):
    def __init__(self, row, col, keys):
        super().__init__()

        self._row = row
        self._col = col
        self._keys = keys

        self.initialize()


    def initialize(self):
        self.setAttribute(Qt.WA_TranslucentBackground)