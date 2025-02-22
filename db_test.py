import asyncio
from db.user import User
from db.operator import Operator

async def main():
    await User.create_user("test_user")
    await Operator.create_operator(
        name="test_operator",
        ctstage_name="test_ctstage",
        sweet_name="test_sweet",
        group=1,
        is_sv=True,
        is_active=True
    )

if __name__ == "__main__":
    asyncio.run(main())
