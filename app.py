import sys

from keyset import KeySet, KeyObject as KO
from grid import GridWidget

from PyQt5.QtWidgets import QApplication

keys = [
    KO(1, "Q"),
    KO(2, "W"),
    KO(3, "E")
]

ks = KeySet(keys)

print(ks.has_key(1))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = GridWidget(1, 3, keys)
    wnd.show()

    sys.exit(app.exec_())