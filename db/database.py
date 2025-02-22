import asyncio
import datetime
from contextlib import asynccontextmanager
from typing import AsyncGenerator

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
    def __init__(self):
        self.engine = create_async_engine(
            "sqlite+aiosqlite:///db.sqlite3",
            connect_args={"check_same_thread": False}
        )
    
    async def init(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        await self.connect_db()
    
    async def connect_db(self):
        Session = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autocommit=False,
            autoflush=False
        )
        return Session()

database = Database()
asyncio.run(database.init())

'''
class DatabaseManager:
    def __init__(self, database_url: str = 'sqlite+aiosqlite:///db.sqlite3'):
        self._database_url = database_url
        self._engine = None
        self._session_factory = None

    def init(self) -> None:
        """データベースエンジンとセッションファクトリを初期化"""
        self._engine = create_async_engine(
            self._database_url,
            connect_args={"check_same_thread": False}
        )

        self._session_factory = sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            autocommit=False,
            autoflush=False
        )

    async def create_tables(self) -> None:
        """データベーステーブルを作成"""
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        """非同期セッションを提供するコンテキストマネージャ"""
        if not self._session_factory:
            raise RuntimeError("DatabaseManager has not been initialized")

        session = self._session_factory()
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def close(self) -> None:
        """データベース接続をクリーンアップ"""
        if self._engine:
            await self._engine.dispose()

# デフォルトのデータベースマネージャーインスタンスを作成
db = DatabaseManager()
'''