"""base notifier. Email asli ke payam ro mifreste"""

from abc import ABC, abstractmethod


class Notifier(ABC):
    """class paye baraye hame notifier ha
    (che asli che decorator ha)"""

    @abstractmethod
    def send(self, message: str) -> None:
        """payam ro be karbar ersal mikone"""

        pass


class EmailNotifier(Notifier):
    """ba Email notif mifreste"""

    def send(self, message: str) -> None:
        print(f"Email: {message}")
