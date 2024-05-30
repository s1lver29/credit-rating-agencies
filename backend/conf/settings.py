from enum import Enum
from os import getenv
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Environment(str, Enum):
    dev = "dev"
    prod = "prod"


class DatabaseSettings(BaseSettings):
    env: Environment
    db_url: None | str = None
    # db_host: None | int = None
    # db_port: None | str = None
    # db_user: None | str = None
    # db_password: None | str = None

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / f"{getenv('ENVIRONMENT')}.env",
        env_file_encoding="utf-8",
    )


class ModelSettings(BaseSettings):
    path_tokenizer: None | str = Field(None, env="PATH_TOKENIZER")
    path_model: None | str = Field(None, env="PATH_MODEL")

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / f"{getenv('ENVIRONMENT')}.env",
        env_file_encoding="utf-8",
    )

# class CelerySettings(BaseSettings):
#     broker_redis_url: None | str = None
#     backend_redis_url: None | str = None

#     model_config = SettingsConfigDict(
#         env_file=Path(__file__).parent / f"{getenv('ENVIRONMENT')}.env",
#         env_file_encoding="utf-8",
#     )


class Settings:
    def __init__(self, env: Environment):
        self.db_settings = DatabaseSettings(env=env)
        self.model_settings = ModelSettings()
        # self.celery_settings = CelerySettings()

    def get_db_settings(self):
        return self.db_settings

    def get_model_settings(self):
        return self.model_settings

    # def get_celery_settings(self):
    #     return self.celery_settings


environment = getenv("ENVIRONMENT")
if environment is None:
    raise ValueError("Environment variable 'ENVIRONMENT' is not set.")
settings = Settings(env=environment)

print(settings.get_db_settings())
