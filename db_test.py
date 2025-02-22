from db.user import User
from db.database import init_models
import asyncio

async def main():
    # テーブルを作成
    await init_models()
    # ユーザーを作成
    await User.create_user("test")

asyncio.run(main())
