
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

from keyset import KeySet, KeyObject as KO

class GridWidget(QWidget):
    def __init__(self, row, col, keys: KeySet):
        super().__init__()

        self._row = row
        self._col = col
        self._keys = keys

        self._setupWidgets()


    def _setupWidgets(self):
        self._setupLabels()
        self._setupGrid()
        self.setLayout(self._grid)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resetGrid(is_initialize = True)


    def _setupLabels(self):
        self._filled_list = [self._createLabel(k.letter()) for k in self._keys.key_list()]
        self._empty_list = [self._createLabel("") for i in range(self._row * self._col)]


    def _createLabel(self, text):
        label = QLabel(text)
        
        label.setStyleSheet("QLabel { color : red; border: 1px dotted red; }")
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label.setFont(QFont("Arial", 18))

        return label


    def _setupGrid(self):
        self._grid = QGridLayout()
        self._grid.setSpacing(0)
        self._grid.setContentsMargins(0, 0, 0, 0)


    def resetGrid(self, is_initialize = False):
        for row in range(self._row):
            for col in range(self._col):
                widget = self._filled_list[row * self._col + col]
                if (is_initialize):
                    self._grid.addWidget(widget, row, col)
                # else:
                    # self._grid.replaceWidget()


    def setGrid(self, x, y, grid):
        pass


    def processKeyPressEvent(self, key):
        if (self._keys.has_key(key)):
            ind = self._keys.get_index_by_key(key)
            return self._filled_list[ind]
        
        return None