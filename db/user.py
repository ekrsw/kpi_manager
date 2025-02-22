from sqlalchemy import Column, String
from .database import BaseDatabase, database


class User(BaseDatabase):
    __tablename__ = "users"
    username = Column(String, nullable=False)

    @classmethod
    async def create_user(cls, username: str) -> None:
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
        await session.close()
        return
    
    @classmethod
    async def get_all_user(cls):
        await database.init()
        session = await database.connect_db()
        users = session.query(User).all()
        session.close()
        return users
