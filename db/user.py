from sqlalchemy import Column, String
from .database import BaseDatabase, database


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
        await database.init()
        session = await database.connect_db()
        user = User(username=username)
        session.add(user)
        await session.commit()
        await session.flush(user)
        return
    
