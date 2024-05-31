from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from conf.settings import settings

database_url: str | None = settings.db_url

if database_url is None:
    raise ValueError("DATABASE_URL must not be None")

engine = create_async_engine(database_url)

async_session = async_sessionmaker(engine, expire_on_commit=False)
