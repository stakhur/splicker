
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from grid import GridWidget

class GridWindow(QMainWindow):
    def __init__(self, preset):
        super().__init__()
        
        self._setupGrids(preset)
        self._initWidget()
        

    def _setupGrids(self, preset):
        self._grids = []

        for (row, col, keys) in preset:
            self._addGrid(row, col, keys)
        self._curr_grid = 0


    def _addGrid(self, row, col, keys):
        self._grids.append(GridWidget(row, col, keys))

    
    def _initWidget(self):
        self.setCentralWidget(self._grids[self._curr_grid])
        # self.setAttribute(Qt.WA_TranslucentBackground)