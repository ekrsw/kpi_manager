import asyncio
import uuid
from sqlalchemy import select
from db.database import db
from db.user import User

async def main():
    # データベースの初期化
    db.init()
    await db.create_tables()

    try:
        # セッションを使用したデータベース操作
        async with db.session() as session:

            # ユーザーの作成
            new_user = User(username="テストユーザー")
            session.add(new_user)
            await session.flush()

            # ユーザーの取得（プライマリーキーによる取得）
            user = await session.get(User, new_user.id)
            print(f"Created user: {user.username})")

    finally:
        # データベース接続のクリーンアップ
        await db.close()

if __name__ == "__main__":
    asyncio.run(main())
