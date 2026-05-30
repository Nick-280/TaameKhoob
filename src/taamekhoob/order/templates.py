"""template sefaresh amade ba pattern prototype"""

import copy


class OrderTemplate:
    """ye ghaleb az sefarsh ke mitoonim
    az roosh copy konim"""

    def __init__(self, name: str, items: list[tuple[str, int]]) -> None:
        """ghaleb sefaresh ro ba name va list food
        ha misaze"""
        self.name = name
        self.items = items

    def clone(self) -> "OrderTemplate":
        """ye deepcopy jadid az ghaleb asli barmigardoone"""

        return copy.deepcopy(self)


BREAKFAST_TEMPLATE = OrderTemplate("sobhane vip", [("espresso", 1), ("cake", 1)])
LUNCH_TEMPLATE = OrderTemplate(
    "nahare kari", [("pizza_maragherita", 1), ("caesar_salad", 1)]
)
