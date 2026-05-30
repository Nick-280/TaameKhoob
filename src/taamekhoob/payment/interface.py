"""yekparche kardane dargahe pardakht"""

from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    """rabet yekparche baraye hame dargah ha"""

    @abstractmethod
    def pay(self, amount_toman: int, order_id: str) -> str:
        """pardakht ro shoru mikone va URL vase
        hedayat user ro barmigardoone"""

        pass

    @abstractmethod
    def verify(self, payment_ref: str) -> bool:
        """vaziat pardakht ro check mikone,
        agar success: True"""

        pass
