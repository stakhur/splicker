from keyset import KeySet, KeyObject as KO
from PyQt5.QtCore import Qt

_ks1 = KeySet([
    KO(Qt.Key_Q, "Q"),
    KO(Qt.Key_W, "W"),
    KO(Qt.Key_A, "A"),
    KO(Qt.Key_S, "S")
])

_ks2 = KeySet([
    KO(Qt.Key_Q, "Q"),
    KO(Qt.Key_W, "W"),
    KO(Qt.Key_E, "E"),
    KO(Qt.Key_A, "A"),
    KO(Qt.Key_S, "S"),
    KO(Qt.Key_D, "D"),
    KO(Qt.Key_Z, "Z"),
    KO(Qt.Key_X, "X"),
    KO(Qt.Key_C, "C")
])

_ks3 = KeySet([
    KO(Qt.Key_7, "7"),
    KO(Qt.Key_8, "8"),
    KO(Qt.Key_9, "9"),
    KO(Qt.Key_4, "4"),
    KO(Qt.Key_5, "5"),
    KO(Qt.Key_6, "6"),
    KO(Qt.Key_1, "1"),
    KO(Qt.Key_2, "2"),
    KO(Qt.Key_3, "3")
])

preset = [
    (2, 2, _ks1),
    (3, 3, _ks2),
    (3, 3, _ks3)
]
