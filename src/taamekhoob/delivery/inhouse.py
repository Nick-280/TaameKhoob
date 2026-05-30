"""adapter baraye service dakheli"""

import random
from typing import Tuple


class InHouseDelivery:
    """shabih sazie ersal dakheli resturan
    (third-party - nemishe taghir dad)"""

    def assign_driver(self, customer_address: str, items_count: int) -> int:
        """motori ro ersal mikone va ID driver ro barmigardoone"""

        driver_id = random.randint(1, 99)
        return driver_id


class InHouseAdapter:
    """Adapter baraye ersal dakheli. InHouse ro be
    DeliveryService tabdil mikone"""

    def __init__(self):
        self._delivery = InHouseDelivery()

    def schedule(self, address: str, items: list[Tuple[str, int]]) -> str:
        """ersal ro zamanbandi mikone
        (item haro be halate morede niyaze InHouse
        tabdil mikone)"""

        items_count = len(items)
        driver_id = self._delivery.assign_driver(address, items_count)
        return f"INHOUSE_{driver_id}"
