import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from db.database import init_db
from src.handlers import router


BOT_TOKEN = "8863916144:AAH6TJLyvd96XoEGEVq5ArI3a0v_Sk-EfI4"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    init_db()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())