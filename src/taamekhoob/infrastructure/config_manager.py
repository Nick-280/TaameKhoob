"""class config manager ba Singleton pattern.
setting barname ro modiriat mikone"""

import json
from typing import Optional, Any


class ConfigManager:
    """ConfigManager ba Singleton pattern.
    faghat ye nemone misaze"""

    _instance: Optional["ConfigManager"] = None

    def __new__(cls) -> "ConfigManager":
        """hamoon nemone ghabli ro bar migardoone"""

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, path: str = "config.json") -> None:
        """faghat yek bar meghdardehi mikone"""

        if not hasattr(self, "_initialized"):
            self._initialized = True

            with open(path, "r") as file:
                self._config: dict[str, Any] = json.load(file)

    def set(self, key: str, value: Any) -> None:
        """ye setting ro zakhire mikone"""

        self._config[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """ye setting ro barmigardoone"""

        return self._config.get(key, default)
