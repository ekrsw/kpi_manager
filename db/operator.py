from sqlalchemy import Boolean, Column, Integer, String, select
from .database import BaseDatabase, database


class Operator(BaseDatabase):
    __tablename__ = "operators"
    name = Column(String, nullable=False)
    ctstage_name = Column(String)
    sweet_name = Column(String)
    group = Column(Integer)
    is_sv = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)

    @classmethod
    async def create_operator(cls,
                              name: str,
                              ctstage_name: str,
                              sweet_name: str,
                              group: int,
                              is_sv: bool=False,
                              is_active: bool=True) -> None:
        """オペレーターを新規作成する

        Args:
            username (str): ユーザー名

        Returns:
            User: 作成されたユーザーインスタンス
        """
        await database.init()
        session = await database.connect_db()
        operator = cls(name=name,
                       ctstage_name=ctstage_name,
                       sweet_name=sweet_name,
                       group=group,
                       is_sv=is_sv,
                       is_active=is_active)
        session.add(operator)
        await session.commit()
        await session.close()
        return
    
    @classmethod
    async def get_all_operators(cls) -> list["Operator"]:
        """全てのオペレーターを取得する

        Returns:
            list[User]: 全てのオペレーターインスタンスのリスト
        """
        await database.init()
        session = await database.connect_db()
        result = await session.execute(select(cls))
        operators = result.scalars().all()
        await session.close()
        return operators
