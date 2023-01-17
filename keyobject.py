class KeyObject:
    def __init__(self, key: int, letter: str):
        self._key = key
        self._letter = letter


    def letter(self):
        return self._letter


    def key(self):
        return self._key


    def __repr__(self) -> str:
        return self.letter()

