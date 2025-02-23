from sqlalchemy import Column, Integer, Float, String, select
from .database import BaseDatabase, database


class KPI(BaseDatabase):
    __tablename__ = "kpis"

    # 着信関連
    total_calls = Column(Integer, nullable=False, comment='総着信数')
    ivr_interruptions = Column(Integer, nullable=False, comment='自動音声ガイダンス途中切断数')
    abandoned_during_operator = Column(Integer, nullable=False, comment='オペレーター呼出途中放棄数')
    abandoned_in_ivr = Column(Integer, nullable=False, comment='留守電放棄件数')
    abandoned_calls = Column(Integer, nullable=False, comment='放棄呼数')
    voicemails = Column(Integer, nullable=False, comment='留守電数')
    responses = Column(Integer, nullable=False, comment='応答件数')
    response_rate = Column(Float, nullable=False, comment='応答率')
    phone_inquiries = Column(Integer, nullable=False, comment='電話問い合わせ件数')
    
    # 直受け関連
    direct_handling = Column(Integer, nullable=False, comment='直受け対応件数')
    direct_handling_rate = Column(Float, nullable=False, comment='直受け対応率')
    
    # コールバック時間帯別件数
    callback_count_0_to_20_min = Column(Integer, nullable=False, comment='お待たせ0分～20分対応件数')
    cumulative_callback_under_20_min = Column(Integer, nullable=False, comment='お待たせ20分以内累計対応件数')
    cumulative_callback_rate_under_20_min = Column(Float, nullable=False, comment='お待たせ20分以内累計対応率')
    
    callback_count_20_to_30_min = Column(Integer, nullable=False, comment='お待たせ20分～30分対応件数')
    cumulative_callback_under_30_min = Column(Integer, nullable=False, comment='お待たせ30分以内累計対応件数')
    cumulative_callback_rate_under_30_min = Column(Float, nullable=False, comment='お待たせ30分以内累計対応率')
    
    callback_count_30_to_40_min = Column(Integer, nullable=False, comment='お待たせ30分～40分対応件数')
    cumulative_callback_under_40_min = Column(Integer, nullable=False, comment='お待たせ40分以内累計対応件数')
    cumulative_callback_rate_under_40_min = Column(Float, nullable=False, comment='お待たせ40分以内累計対応率')
    
    callback_count_40_to_60_min = Column(Integer, nullable=False, comment='お待たせ40分～60分対応件数')
    cumulative_callback_under_60_min = Column(Integer, nullable=False, comment='お待たせ60分以内累計対応件数')
    cumulative_callback_rate_under_60_min = Column(Float, nullable=False, comment='お待たせ60分以内累計対応率')
    
    callback_count_over_60_min = Column(Integer, nullable=False, comment='お待たせ60分以上対応件数')
    
    # お待たせ時間超過件数
    waiting_for_callback_over_20min = Column(Integer, nullable=False, comment='お待たせ20分以上対応件数')
    waiting_for_callback_over_30min = Column(Integer, nullable=False, comment='お待たせ30分以上対応件数')
    waiting_for_callback_over_40min = Column(Integer, nullable=False, comment='お待たせ40分以上対応件数')
    waiting_for_callback_over_60min = Column(Integer, nullable=False, comment='お待たせ60分以上対応件数')
    
    # お待たせ時間超過案件番号リスト
    wfc_20min_list = Column(String, nullable=True, comment='お待たせ20分以上対応案件番号')
    wfc_30min_list = Column(String, nullable=True, comment='お待たせ30分以上対応案件番号')
    wfc_40min_list = Column(String, nullable=True, comment='お待たせ40分以上対応案件番号')
    wfc_60min_list = Column(String, nullable=True, comment='お待たせ60分以上対応案件番号')

    @classmethod
    async def get_latest_kpi(cls):
        await database.init()
        session = await database.connect_db()
        result = await session.execute(select(cls).order_by(cls.created_at.desc()).limit(1))
        kpi = result.scalars().first()
        await session.close()
        return kpi
    
    @classmethod
    async def add_kpi(cls, kpi: dict) -> None:
        await database.init()
        session = await database.connect_db()
        new_kpi = cls(**kpi)
        session.add(new_kpi)
        await session.commit()
        await session.close()
        return
