from functools import lru_cache
import os
import tomllib
from typing import TypeVar

from adaptix import Retort

from app.shared.logger import get_logger

T = TypeVar("T")
DEFAULT_CONFIG_PATH = "./config/config.toml"


logger = get_logger(__name__)


def read_toml(path: str) -> dict:
    """Read TOML configuration file."""
    with open(path, "rb") as f:
        return tomllib.load(f)


@lru_cache
def load_config(config_type: type[T], config_scope: str | None = None, path: str | None = None) -> T:
    """Load configuration using adaptix."""
    logger.info(f"Loading config from: {os.getcwd()}")

    if path is None:
        path = os.getenv("CONFIG_PATH", DEFAULT_CONFIG_PATH)

    data = read_toml(path)

    if config_scope is not None:
        data = data[config_scope]

    dcf = Retort()
    config = dcf.load(data, config_type)
    return config
