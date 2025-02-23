from sqlalchemy import Column, String, select
from .database import BaseDatabase, database


class Group(BaseDatabase):
    __tablename__ = "group"
    group_name = Column(String, nullable=False, index=True)

    @classmethod
    async def create_user(cls, groupname: str) -> None:
        """グループを作成する

        Args:
            groupname (str): グループ名

        Returns:
            Group: 作成されたグループインスタンス
        """
        await database.init()
        session = await database.connect_db()
        group = cls(groupname=groupname)
        session.add(group)
        await session.commit()
        await session.close()
        return
    
    @classmethod
    async def get_all_users(cls) -> list["Group"]:
        """全てのグループを取得する

        Returns:
            list[Group]: 全てのユーザーインスタンスのリスト
        """
        await database.init()
        session = await database.connect_db()
        result = await session.execute(select(cls))
        users = result.scalars().all()
        await session.close()
        return users
    
    @classmethod
    async def get_group(cls, id: int) -> "Group | None":
        """指定されたIDのグループを取得する

        Args:
            id (int): グループID

        Returns:
            Group | None: グループインスタンス。存在しない場合はNone
        """
        await database.init()
        session = await database.connect_db()
        result = await session.execute(select(cls).where(cls.id == id))
        group = result.scalars().first()
        await session.close()
        return group
