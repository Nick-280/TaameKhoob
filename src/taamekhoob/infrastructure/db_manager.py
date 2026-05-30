"""Class database manager ba Singleton pattern.
ertebatat va zakhire sazi database ro modiriat mikone"""

from typing import Optional, Any


class DBManager:
    """faghat ye nemone misaze"""

    _instance: Optional["DBManager"] = None

    def __new__(cls) -> "DBManager":
        """har bar hamoon nemone ghabli ro bar migardoone"""

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """faghat yek bar database ro meghdardehi mikone"""

        if not hasattr(self, "_initialized"):
            self._initialized = True
            self._connected: bool = False
            self._data: dict[str, Any] = {}

    def connect(self) -> None:
        """etesal be database ro neshoon mide"""

        if not self._connected:
            self._connected = True

    def disconnect(self) -> None:
        """ghate etesal be database ro neshoon mide"""

        if self._connected:
            self._connected = False

    def is_connected(self) -> bool:
        """check mikone aya etesal bargharare ya kheir"""

        return self._connected

    def save(self, key: str, value: Any) -> None:
        """ye data ro to database zakhire mikone"""

        if not self._connected:
            raise ConnectionError("Not connected. Call connect() first.")
        self._data[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """ye data ro bar migardoone"""

        if not self._connected:
            raise ConnectionError("Not connected. Call connect() first.")
        return self._data.get(key, default)
