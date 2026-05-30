"""adapter baraye service SnappBox"""

from typing import Tuple
from taamekhoob.delivery.interface import DeliveryService
import random


class SnappBoxSDK:
    """shabih sazie SnappBox API
    (third-party - nemishe taghir dad)"""

    def create_order(self, origin: str, destination: str, items: list) -> str:
        """ye sefaresh ersal misaze az
        mabda be maghsad va code
        rahgiri barmigardoone"""

        return f"SNAP_{random.randint(10000, 99999)}_{random.randint(10000, 99999)}"


class SnappBoxAdapter(DeliveryService):
    """Adapter baraye SnappBox. SanppBox ro be
    DeliveryService tabdil mikone"""

    def __init__(self, origin_address: str = "restaurant_address"):
        self._sdk = SnappBoxSDK()
        self._origin_address = origin_address

    def schedule(self, address: str, items: list[Tuple[str, int]]) -> str:
        """ersal ro zamanbandi mikone
        (item haro be halate morede niyaze SnappBox
        tabdil mikone)"""

        items_list = []
        for name, qty in items:
            items_list.append({"name": name, "quantity": qty})

        tracking = self._sdk.create_order(
            origin=self._origin_address, destination=address, items=items_list
        )

        return tracking
