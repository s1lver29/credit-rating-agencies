from os import getenv

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

load_dotenv()

environment = getenv("ENVIRONMENT")
database_url = getenv("DATABASE_URL")

engine = create_async_engine(database_url)

async_session = async_sessionmaker(engine, expire_on_commit=False)

