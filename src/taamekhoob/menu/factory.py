"""MenuItemFactory: Factory method pattern"""

from taamekhoob.menu.item import MenuItem
from taamekhoob.menu.concrete_items import (
    Espresso,
    Latte,
    PizzaMargherita,
    CaesarSalad,
    Cheesecake,
)


class MenuItemFactory:
    """factory baraye sakhte hame item haye menu"""

    @staticmethod
    def create(item_type: str, **kwargs) -> MenuItem:
        """ye food jadid ba type dade shode misazad.

        Args: item_type: "espresso", "latte", "pizza",
        "salad", "cake"
        **kwargs: size(S, M, L) baraye pizza"""

        size = kwargs.get("size", "M")
        if item_type == "espresso":
            return Espresso()
        elif item_type == "latte":
            return Latte()
        elif (item_type == "pizza") or (item_type == "pizza_margherita"):
            return PizzaMargherita(size)
        elif (item_type == "salad") or (item_type == "caesar_salad"):
            return CaesarSalad()
        elif (item_type == "cake") or (item_type == "cheesecake"):
            return Cheesecake()
        else:
            raise ValueError(f"Unknown item type: {item_type}")
