
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QFocusEvent
from PyQt5.QtTest import QTest
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
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(Qt.ClickFocus)
        self.setCentralWidget(self._grids[self._curr_grid])


    def focusOutEvent(self, ev: QFocusEvent) -> None:
        self.activateWindow()


    def keyPressEvent(self, a0: QKeyEvent) -> None:
        key = a0.key()
        
        widget = self._grids[self._curr_grid].processKeyPressEvent(key)
        if (widget):
            QTest.mouseMove(widget)
        # elif (key == Qt.Key_Return):
            # self.mouseClick(pyautogui.click)
        # elif (key == Qt.Key_Space):
            # self.mouseClick(pyautogui.rightClick)
        # elif (key == Qt.Key_Backspace):
            # self.initialize()
        elif (key == Qt.Key_Tab):
            print("TAB pressed")
        elif (key == Qt.Key_X):
            exit(0)

        return super().keyPressEvent(a0)