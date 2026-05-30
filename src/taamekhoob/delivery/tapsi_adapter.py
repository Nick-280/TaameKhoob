"""adapter baraye service Tapsi"""

from typing import Tuple
from taamekhoob.delivery.interface import DeliveryService
import random


class TapsiSDK:
    """shabih sazie Tapsi API
    (third-party - nemishe taghir dad)"""

    def send_order(
        self, origin: str, destination: str, items: list, payment_method: str = "online"
    ) -> dict:
        """ye sefaresh ersal misaze az
        mabda be maghsad ba noe
        pardakht va code rahgiri
        barmigardoone"""

        return {"tracking code": f"TAP_{random.randint(10000, 99999)}", "price": 25000}


class TapsiAdapter(DeliveryService):
    """Adapter baraye Tapsi. Tapsi ro be
    DeliveryService tabdil mikone"""

    def __init__(self, origin_address: str = "restaurant_address"):
        self._sdk = TapsiSDK()
        self._origin_address = origin_address

    def schedule(self, address: str, items: list[Tuple[str, int]]) -> str:
        """ersal ro zamanbandi mikone
        (item haro be halate morede niyaze Tapsi
        tabdil mikone)"""

        items_list = []
        for name, qty in items:
            items_list.append({"name": name, "quantity": qty})

        result = self._sdk.send_order(
            origin=self._origin_address,
            destination=address,
            items=items_list,
            payment_method="online",
        )

        return result["tracking code"]
