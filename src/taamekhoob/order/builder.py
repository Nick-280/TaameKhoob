"""Builder baraye sakht sefaresh"""

from taamekhoob.order.order import Order
from taamekhoob.menu.item import MenuItem


class OrderBuilder:
    """sefaresh ro gam be gam misaze"""

    def __init__(self) -> None:
        """ye builder jadid ba sefaresh khali
        misaze"""

        self._order = Order()

    def add_item(self, item: MenuItem, qty: int = 1) -> "OrderBuilder":
        """ye food be sefaresh ezafe mikone"""

        self._order.items.append((item, qty))
        return self

    def with_coupon(self, code: str) -> "OrderBuilder":
        """code takhfif ro ezafe mikone"""

        self._order.coupon = code
        return self

    def deliver_to(self, address: str) -> "OrderBuilder":
        """address tahvili ro ezafe mikone"""

        self._order.address = address
        return self

    def pay_with(self, gateway: str) -> "OrderBuilder":
        """dargahe pardakht ro entekhab mikone"""

        self._order.gateway = gateway
        return self

    def build(self) -> Order:
        """sefaresh nahaei ro ba etebarsanji bar
        migardoone"""

        if not self._order.items:
            raise ValueError("Order must have at least one item")
        return self._order
