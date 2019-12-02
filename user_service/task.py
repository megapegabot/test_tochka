from asyncio import sleep
from user_service.db.client import DBClient


async def subtract_balance(db: DBClient, timeout: int):
    while True:
        await sleep(timeout)
        await db.subtract_balance()



