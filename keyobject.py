class KeyObject:
    def __init__(self, key: int, letter: str):
        self._key = key
        self._letter = letter
        self._widget = None


    def setWidget(self, widget):
        self._widget = widget


    def letter(self):
        return self._letter


    def key(self):
        return self._key


    def widget(self):
        return self._widget


    def __repr__(self) -> str:
        return self.letter()

