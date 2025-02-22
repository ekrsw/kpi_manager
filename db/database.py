import asyncio
import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BaseDatabase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)

class Database:
    def __init__(self) -> None:
        self.engine = create_async_engine(
            "sqlite+aiosqlite:///db.sqlite3",
            connect_args={"check_same_thread": False}
        )
    
    async def init(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        await self.connect_db()
    
    async def connect_db(self) -> AsyncSession:
        Session = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autocommit=False,
            autoflush=False
        )
        return Session()

database = Database()
