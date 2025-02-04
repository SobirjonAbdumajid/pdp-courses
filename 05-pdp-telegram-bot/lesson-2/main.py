import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher()


class UserForm(StatesGroup):
    full_name = State()
    age = State()
    phone_number = State()
    location = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await state.set_state(UserForm.full_name)
    await message.answer(f"To'liq ism familiyangizni kiriting")


@dp.message(UserForm.full_name)
async def command_user_handler(message: Message, state: FSMContext):
    await state.update_data({'full_name': message.text})
    await state.set_state(UserForm.age)
    await message.answer("Yoshingizni kiriting!")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
