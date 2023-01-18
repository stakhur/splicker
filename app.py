import sys

from preset_keyset import preset
from grid_window import GridWindow

from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = GridWindow(preset)    
    wnd.showFullScreen()

    sys.exit(app.exec_())