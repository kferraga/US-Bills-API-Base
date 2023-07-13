# itemized_list.py

class ItemizedList:
    """Establishes a basic itemized list."""
    def __init__(self):
        self._items = {}

    def add_kwrd_item(self, key, **kwargs):
        """Adds a new key-value pair to the itemized list, given a list of keyword."""
        self._items[key] = kwargs

    def give_values(self):
        """Returns all items from the values as a list."""
        return list(self._items.values())

    def length(self):
        """Gives length."""
        return len(self._items)