import asyncio
import logging
from aiogram import F
from aiogram.types import Message, ReactionTypeEmoji

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command


BOT_TOKEN = "8863916144:AAH6TJLyvd96XoEGEVq5ArI3a0v_Sk-EfI4"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()     # обработчик входящих обновлений


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет {message.from_user.full_name}, я твой бот!"
    )
    print(f"Пользователь {message.from_user.full_name} написал команду /start!")
@dp.message(Command("about"))
async def cmd_abt(message: Message):
    await message.answer(
        "Это бот Карыбаева Нурадила, это его первый бот\n"
        "Функционал пока не такой обширный, но это временно\n"
        "Я называюсь roj потому что это сокращение от rayofjustice\n"
        "что в переводе Луч Справедливости, то есть Нурадил на кыргызском :)"

    )

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "/start - команда для запуска\n"
        "/help - список команд"
    )
@dp.message(F.text.lower() == "пока")
async def cmd_bye(message: Message):
    await message.react([ReactionTypeEmoji(emoji="👌")])
@dp.message(F.text.lower() == "группа")
async def cmd_group(message: Message):
    await message.answer("Твоя группа 71-1!")


# @dp.message(F.from_user.id == 1288365917)
# async def cmd_group(message: Message):
#     await message.answer("Привет мой создатель!!!")


@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")


async def main():
    await dp.start_polling(bot)     # отправляет запросы на тг-сервер


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())