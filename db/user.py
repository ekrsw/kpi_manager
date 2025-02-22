from sqlalchemy import Column, String
from .database import BaseDatabase, db


class User(BaseDatabase):
    __tablename__ = "users"
    username = Column(String, nullable=False)

    @classmethod
    async def create_user(cls, username: str) -> "User":
        """ユーザーを作成する

        Args:
            username (str): ユーザー名

        Returns:
            User: 作成されたユーザーインスタンス
        """
        async with db.session() as session:
            user = cls(username=username)
            session.add(user)
            await session.flush()
            await session.refresh(user)
            return user
    
    
