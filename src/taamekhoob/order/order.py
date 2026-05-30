"""Order data model"""

from dataclasses import dataclass, field
from typing import Optional
from taamekhoob.menu.item import MenuItem


@dataclass
class Order:
    """etelaate order ro zakhire mikone"""

    order_id: str = ""
    items: list[tuple[MenuItem, int]] = field(default_factory=list)
    coupon: Optional[str] = None
    address: Optional[str] = None
    gateway: Optional[str] = None

    def total_cost(self) -> float:
        """gheimat kol item hara hesab mikone"""

        total = 0.0
        for item, qty in self.items:
            total += item.cost() * qty
        return total

    def __str__(self) -> str:
        """order ro be onvane string neshoon mide"""

        lines = ["ORDERS"]
        for item, qty in self.items:
            lines.append(f" {item.description()} x{qty} = {item.cost()*qty:,} T")
        lines.append(f"Total: {self.total_cost():,} T")
        if self.coupon:
            lines.append(f"Coupon: {self.coupon}")
        if self.address:
            lines.append(f"Address: {self.address}")
        if self.gateway:
            lines.append(f"Payment: {self.gateway}")
        return "\n".join(lines)
