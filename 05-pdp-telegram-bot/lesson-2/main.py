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
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
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
async def full_name_handler(message: Message, state: FSMContext):
    await state.update_data({'full_name': message.text})
    await state.set_state(UserForm.age)
    await message.answer("Yoshingizni kiriting!")


@dp.message(UserForm.age)
async def age_handler(message: Message, state: FSMContext):
    await state.update_data({'age': message.text})
    await state.set_state(UserForm.phone_number)
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[KeyboardButton(text="Telefon raqam", request_contact=True)])
    rkb = rkb.as_markup(resize_keyboard=True)
    await message.answer("Telefon raqamingizni quyidagi tugma orqali yuboring!", reply_markup=rkb)


@dp.message(UserForm.phone_number)
async def phone_number_handler(message: Message, state: FSMContext):
    await state.update_data({'phone_number': message.contact.phone_number})
    await state.set_state(UserForm.location)
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[KeyboardButton(text="Location", request_location=True)])
    rkb = rkb.as_markup(resize_keyboard=True)
    await message.answer("Locationni quyidagi tugma orqali yuboring!", reply_markup=rkb)


@dp.message(UserForm.location)
async def location_handler(message: Message, state: FSMContext):
    await state.update_data({'location': message.location.longitude, 'latitude': message.location.latitude})
    user_data = await state.get_data()
    await state.clear()
    format = f"""
        Fullname: {user_data['full_name']}
        Age: {user_data['age']}
        Phone: {user_data['phone_number']}
        Location: {user_data['location']}
    """
    await message.answer(format, reply_markup=ReplyKeyboardRemove())


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
