"""Tests for Singleton pattern."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.taamekhoob.infrastructure.logger import Logger
from src.taamekhoob.infrastructure.config_manager import ConfigManager
from src.taamekhoob.infrastructure.db_manager import DBManager


def test_logger_singleton():
    logger1 = Logger()
    logger2 = Logger()
    assert logger1 is logger2


def test_logger_saves_messages():
    logger = Logger()
    logger._messages.clear()
    logger.log("Test message")
    assert len(logger.get_messages()) == 1


def test_config_manager_singleton():
    config1 = ConfigManager()
    config2 = ConfigManager()
    assert config1 is config2


def test_db_manager_singleton():
    db1 = DBManager()
    db2 = DBManager()
    assert db1 is db2


if __name__ == "__main__":
    test_logger_singleton()
    test_logger_saves_messages()
    test_config_manager_singleton()
    test_db_manager_singleton()
