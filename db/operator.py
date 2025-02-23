from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, select
from .database import BaseDatabase, database
from db.group import Group


class Operator(BaseDatabase):
    __tablename__ = "operator"
    name = Column(String, nullable=False, index=True, comment='氏名')
    ctstage_name = Column(String, comment='CTStage名')
    sweet_name = Column(String, comment='Sweet名')
    group_id = Column(ForeignKey('group.id', ondelete='RESTRICT'), nullable=False, comment='グループID')
    is_sv = Column(Boolean, nullable=False, comment='SV')
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
