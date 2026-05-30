"""class Logger ba Singleton pattern.
tanha yek nemone az Logger vojud dare"""

from typing import Optional


class Logger:
    """yek Logger sade baraye zakhire messages. Singleton pattern"""

    _instance: Optional["Logger"] = None

    def __new__(cls) -> "Logger":
        """__new__ ro override mikonim ta hamoon sample ghabli
        return beshe"""

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """logger ro faghat yek bar meghdar dehi mikone"""

        if not hasattr(self, "_initialized"):
            self._initialized = True
            self._messages: list[str] = []

    def log(self, message: str) -> None:
        """ye message be list ezafe mikone"""

        self._messages.append(message)

    def info(self, message: str) -> None:
        """ye message be name INFO ezafe mione"""

        self._messages.append(f"[INFO] {message}")

    def warning(self, message: str) -> None:
        """ye message ba name WARNING ezafe mikone"""

        self._messages.append(f"[WARNING] {message}")

    def error(self, message: str) -> None:
        """ye message ba name ERROR ezafe mikone"""

        self._messages.append(f"[ERROR] {message}")

    def get_messages(self) -> list[str]:
        """tamame messages list ro barmigardone"""

        return self._messages.copy()
