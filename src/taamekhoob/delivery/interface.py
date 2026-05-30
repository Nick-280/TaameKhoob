"""yekparche kardane service tahvil kala"""

from abc import ABC, abstractmethod
from typing import List, Tuple


class DeliveryService(ABC):
    """rabet yekparche baraye hame service ha"""

    @abstractmethod
    def schedule(self, address: str, items: List[Tuple[str, int]]) -> str:
        """ersal ro zamanbandi mikone va code rahgiri
        barmigardoone yani ye reshte.
        (address: address moshtari)
        (items: list az esm food va tedad)"""

        pass
