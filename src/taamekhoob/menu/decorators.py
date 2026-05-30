"""Decorators baraye customize kardane item ha"""

from taamekhoob.menu.item import MenuItem


class MenuItemDecorator(MenuItem):
    """class paye decorator: MenuItem hast va MenuItem
    dige ham dar khodesh dare"""

    def __init__(self, wrapped: MenuItem):
        """wrapped menu item ro zakhire mikone"""

        self._wrapped = wrapped


class ExtraCheese(MenuItemDecorator):
    """paneer ezafe (+15.000 T)"""

    def cost(self) -> float:
        """gheymat ro be ezafe paneer bar migardoone"""

        return self._wrapped.cost() + 15000

    def description(self) -> str:
        """tozihate food ro ba paneer ezafe bar
        migardoone"""

        return self._wrapped.description() + " + Extra Cheese"


class ExtraMushroom(MenuItemDecorator):
    """gharch ezafe (+12.000 T)"""

    def cost(self) -> float:
        """gheymat ro be ezafe gharch bar migardoone"""

        return self._wrapped.cost() + 12000

    def description(self) -> str:
        """tozihate food ro ba gharch ezafe bar
        migardoone"""

        return self._wrapped.description() + " + Extra Mushroom"


class Milk(MenuItemDecorator):
    """shir ezafe (+10.000 T)"""

    def cost(self) -> float:
        """gheymat ro be ezafe shir bar migardoone"""

        return self._wrapped.cost() + 10000

    def description(self) -> str:
        """tozihate food ro ba shir ezafe bar
        migardoone"""

        return self._wrapped.description() + " + Milk"


class Sugar(MenuItemDecorator):
    """shekar ezafe (+5.000 T)"""

    def cost(self) -> float:
        """gheymat ro be ezafe shekar bar migardoone"""

        return self._wrapped.cost() + 5000

    def description(self) -> str:
        """tozihate food ro be ezafe shekar bar
        migardoone"""

        return self._wrapped.description() + " + Sugar"


class WithoutOnion(MenuItemDecorator):
    """hazte piaz (gheimat ezafe nemikone)"""

    def cost(self) -> float:
        """gheimat taghir nemikone (hamoon ghabli)"""

        return self._wrapped.cost()

    def description(self) -> str:
        """tozihate food ro ba hazfe piaz bar
        migardoone"""

        return self._wrapped.description() + " (no onion)"
