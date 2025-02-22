import asyncio
from db.user import User

async def main():
    # データベースの初期化
    await User.create_user("test_user")

if __name__ == "__main__":
    asyncio.run(main())
