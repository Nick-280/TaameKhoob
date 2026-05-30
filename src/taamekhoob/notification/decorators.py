"""decorator ha baraye ezafe kardan kanal haye ersal(SMS, Push, Panel)"""

from taamekhoob.notification.notifier import Notifier


class NotifierDecorator(Notifier):
    """class paye decorator. ham khodesh notifier
    hast, ham dar khodesh notifier dare"""

    def __init__(self, wrapped: Notifier) -> None:
        """notifier dade shode ro zakhire mikone"""

        self._wrapped = wrapped

    def send(self, message: str) -> None:
        """payam ro be notifier ha mifreste"""

        self._wrapped.send(message)


class SMSDecorator(NotifierDecorator):
    """SMS ham be notif ha ezafe mikone"""

    def send(self, message: str) -> None:
        """payam ro be SMS ersal mikone va zanjire
        ro edame mide"""

        super().send(message)
        print(f"SMS: {message}")


class PushDecorator(NotifierDecorator):
    """Push notification ham ezafe mikone"""

    def send(self, message: str) -> None:
        """payam ro ba push ersal mikone va zanjire
        ro edame mide"""

        super().send(message)
        print(f"Push: {message}")


class PanelDecorator(NotifierDecorator):
    """payam ro dar panel karbari zakhire mikone"""

    def send(self, message: str) -> None:
        """payam ro dar panel karbari zakhire
        mikone va zanjire ro edame mide"""

        super().send(message)
        print(f"Panel: {message}")
