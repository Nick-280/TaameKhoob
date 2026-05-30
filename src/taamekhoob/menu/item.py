"""MenuItem class base baraye tamame menu item ha"""

from abc import ABC, abstractmethod


class MenuItem(ABC):
    """class base. hame ye foodha az in class
    ers mibarand"""

    @abstractmethod
    def cost(self) -> float:
        """gheimat food ro return mikone"""

        pass

    @abstractmethod
    def description(self) -> str:
        """tozihate food ro return mikone"""

        pass
