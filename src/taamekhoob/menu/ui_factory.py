"""UI components ba Abstract factory"""

from abc import ABC, abstractmethod
from taamekhoob.menu.item import MenuItem


class UIFactory(ABC):
    """Base UI factory. khanevade haye UI (web/mobile)
    ro misaze"""

    @abstractmethod
    def create_button(self, label: str):
        """ye dokme ba label dade shode misaze"""
        pass

    @abstractmethod
    def create_item_card(self, item: MenuItem):
        """ye card baraye namayesh ye food misaze"""
        pass

    @abstractmethod
    def create_payment_form(self):
        """ye form baraye pardakht misaze"""
        pass


class WebButton:
    """dokme baraye web"""

    def __init__(self, label: str) -> None:
        """web button ro ba label dada shode misaze"""
        self.label = label

    def render(self) -> str:
        """dokme ro rooye safhe web neshoon mide"""
        return f"Web Button: {self.label}"


class WebItemCard:
    """card baraye namayesh food dar web"""

    def __init__(self, item: MenuItem) -> None:
        """card ro ba food dade shode misaze"""

        self.item = item

    def render(self):
        """card ro roooye safhe web neshoon mide"""

        return f"Web Card: {self.item.description()}"


class WebPaymentForm:
    """form pardakht baraye web"""

    def render(self) -> str:
        """form pardakht ro roooye safhe web
        neshoon mide"""

        return "Web Payment Form"


class MobileButton:
    """dokme baraye mobile"""

    def __init__(self, label: str) -> None:
        """mobile button ro ba label dada shode misaze"""
        self.label = label

    def render(self) -> str:
        """dokme ro rooye safhe mobile neshoon mide"""
        return f"mobile Button: {self.label}"


class MobileItemCard:
    """card baraye namayesh food dar mobile"""

    def __init__(self, item: MenuItem) -> None:
        """card ro ba food dade shode misaze"""

        self.item = item

    def render(self):
        """card ro roooye safhe mobile neshoon mide"""

        return f"Mobile Card: {self.item.description()}"


class MobilePaymentForm:
    """form pardakht baraye mobile"""

    def render(self) -> str:
        """form pardakht ro roooye safhe mobile
        neshoon mide"""

        return "Mobile Payment Form"


class WebUIFactory(UIFactory):
    """Karkhane sakhte component haye web UI"""

    def create_button(self, label: str) -> WebButton:
        """ye dokme web misaze"""

        return WebButton(label)

    def create_item_card(self, item: MenuItem) -> WebItemCard:
        """ye card web baraye food misaze"""

        return WebItemCard(item)

    def create_payment_form(self) -> WebPaymentForm:
        """ye form pardakht web misaze"""

        return WebPaymentForm()


class MobileUIFactory(UIFactory):
    """Karkhane sakhte component haye mobile UI"""

    def create_button(self, label: str) -> MobileButton:
        """ye dokme mobile misaze"""

        return MobileButton(label)

    def create_item_card(self, item: MenuItem) -> MobileItemCard:
        """ye card mobile baraye food misaze"""

        return MobileItemCard(item)

    def create_payment_form(self) -> MobilePaymentForm:
        """ye form pardakht mobile misaze"""

        return MobilePaymentForm()
