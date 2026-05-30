"""item haye concrete menu"""

from taamekhoob.menu.item import MenuItem


class Espresso(MenuItem):
    """Espresso coffee"""

    def cost(self) -> float:
        return 80000

    def description(self) -> str:
        return "Espresso"


class Latte(MenuItem):
    """Latte coffee"""

    def cost(self) -> float:
        return 120000

    def description(self) -> str:
        return "Latte"


class PizzaMargherita(MenuItem):
    """pizza margherita ba size haye motefavet"""

    def __init__(self, size: str = "M") -> None:
        self.size = size

    def cost(self) -> float:
        if self.size == "S":
            return 180000

        if self.size == "L":
            return 300000

        return 240000

    def description(self) -> str:
        return f"Pizza ({self.size})"


class CaesarSalad(MenuItem):
    """Caesar salad"""

    def cost(self) -> float:
        return 160000

    def description(self) -> str:
        return "Caesar Salad"


class Cheesecake(MenuItem):
    """Cheesecake dessert"""

    def cost(self) -> float:
        return 110000

    def description(self) -> str:
        return "Cheesecake"
