

from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.config import secret


typeID = Annotated[int, mapped_column(primary_key=True, nullable=False)]
typeSTR = Annotated[str, mapped_column(nullable=False)]



class Base(AsyncAttrs, DeclarativeBase):
     pass
     
     
     
class Tables(Base):
     __tablename__ = 'tables'
     
     id: Mapped[typeID]
     name: Mapped[typeSTR]
     password: Mapped[typeSTR]
     
     
     
class Pool:
     __path = f'postgresql+asyncpg://{secret.DB_USER}:{secret.DB_PASS}@{secret.DB_HOST}:{secret.DB_PORT}/{secret.DB_NAME}'
     _eng = create_async_engine(__path, echo=True)
     _sessions = async_sessionmaker(_eng)
     
     
     @classmethod
     async def create_table(cls) -> None:
          async with cls._eng.begin() as connect:
               await connect.run_sync(Base.metadata.create_all)
               
               
     @classmethod
     async def drop_tables(cls) -> None:
          async with cls._eng.begin() as connect:
               await connect.run_sync(Base.metadata.drop_all)





     