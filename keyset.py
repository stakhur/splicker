from keyobject import KeyObject


class KeySet:
    def __init__(self, keys: list[KeyObject]):
        self._list = keys
        self._dict = {k.key(): k for k in self._list}


    def set_widgets(self, widgets: list):
        l = len(widgets)
        if (l != len(self._list)):
            return

        for i in range(l):
            self._list[i].setWidget(widgets[i])


    def set_widget_by_key(self, key: int, widget):
        if (key not in self._dict):
            return
        self._dict[key].setWidget(widget)


    def keys(self):
        return self._dict.keys()


    def has_key(self, key: int):
        return key in self._dict


    def by_index(self, index: int):
        try:
            return self._list[index]
        except IndexError:
            return None


    def by_key(self, key: int):
        try:
            return self._dict[key]
        except KeyError:
            return None
