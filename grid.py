
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel

from keyset import KeySet, KeyObject as KO

class GridWidget(QWidget):
    def __init__(self, row, col, keys):
        super().__init__()

        self._row = row
        self._col = col
        self._keys = keys

        self._empty_list = [QLabel("") for i in range(self._row * self._col)]

        self.initialize()


    def initialize(self):
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resetGrid()


    def resetGrid(self):
        pass


    def setGrid(self, x, y, grid):
        pass