from enum import Enum
from os import getenv
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    dev = "dev"
    prod = "prod"


class GlobalSettings(BaseSettings):
    env: Environment
    db_url: None | str = None
    path_tokenizer: None | str = None
    path_model: None | str = None
    broker_redis_url: None | str = None
    backend_redis_url: None | str = None

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / f"{getenv('ENVIRONMENT')}.env",
        env_file_encoding="utf-8",
    )


def get_settings() -> GlobalSettings:
    environment = getenv("ENVIRONMENT")
    if environment is None:
        raise ValueError("Environment variable 'ENVIRONMENT' is not set.")
    settings = GlobalSettings(env=environment)  # type: ignore

    return settings


settings = get_settings()
