"""Inventory service. shabih sazi anbari baraye check va reserve"""

from taamekhoob.menu.item import MenuItem


class InventoryService:
    """service baraye modiriate anbari (check va reserve)"""

    def __init__(self):
        self._stock = {
            "pizza": 20,
            "pizza_margherita": 10,
            "espresso": 20,
            "latte": 15,
            "cake": 5,
            "caesar_salad": 8,
        }
        self._reserved = {}

    def check(self, item: MenuItem, qty: int) -> bool:
        """barresi mojodi anbari"""

        name = item.description().split()[0].lower()

        if name not in self._stock:
            return False

        available = self._stock[name] - self._reserved.get(name, 0)
        return available >= qty

    def reserve(self, item: MenuItem, qty: int) -> None:
        """reserve mojodi anbari"""

        name = item.description().split()[0].lower()

        if name in self._stock:
            self._reserved[name] = self._reserved.get(name, 0) + qty
