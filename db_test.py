import asyncio
from db.user import User

async def main():
    users = await User.get_all_users()
    for user in users:
        print(user.username)

if __name__ == "__main__":
    asyncio.run(main())
