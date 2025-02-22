import datetime
from sqlalchemy import Column, DateTime, Integer, String
from .database import BaseDatabase


class User(BaseDatabase):
    __tablename__ = "users"
    name = Column(String)

    @classmethod
    async def create_user(cls, name):
        from db.database import async_session
        async with async_session() as session:
            user = cls(name=name)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user
