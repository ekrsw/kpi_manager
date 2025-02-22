from sqlalchemy import Column, String, select
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
    async def get_all_users(cls) -> list["User"]:
        """全てのユーザーを取得する

        Returns:
            list[User]: 全てのユーザーインスタンスのリスト
        """
        await database.init()
        session = await database.connect_db()
        result = await session.execute(select(User))
        users = result.scalars().all()
        await session.close()
        return users
