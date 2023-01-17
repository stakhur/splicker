from keyobject import KeyObject


class KeySet:
    def __init__(self, keys: list[KeyObject]):
        self._list = keys
        self._keys = (k.key() for k in self._list)


    def key_list(self):
        return self._list


    def keys(self):
        return self._keys


    def has_key(self, key: int):
        return key in self._keys


    def by_index(self, index: int):
        try:
            return self._list[index]
        except IndexError:
            return None


    def by_key(self, key: int):
        if (not self.has_key(key)):
            return None
        return self._list.index(key)
