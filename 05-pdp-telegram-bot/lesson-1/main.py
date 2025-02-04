import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Hello World")
    # await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(F.text == 'Assalomu alaykum')
async def alikum(message: Message) -> None:
    await message.reply(text="Va alaykum")


@dp.message(Command('menu'))
async def menu(message: Message) -> None:
    await message.reply(text="Menu'ga xush kelibsiz")


@dp.message(Command('help'))
async def menu(message: Message) -> None:
    await message.reply(text="help'ga xush kelibsiz")


@dp.message((F.text == 'admin') & (F.from_user.id == 5987124979))
async def from_user_handler(message: Message) -> None:
    await message.answer(text='5987124979 xabar yubordi')


@dp.message(F.photo)
async def photo(message: Message) -> None:
    await message.answer(text='Bu xabar rasm ichida')


@dp.message(Command('reply_button'))
async def reply_button_handler(message: Message) -> None:
    design = [
        [
            KeyboardButton(text="What are you hours?"),
            KeyboardButton(text="What is your name")
        ],
        [
            KeyboardButton(text="Can I track my orders?")
        ],
        [
            KeyboardButton(text="How do I report a problem?")
        ]
    ]

    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
    await message.answer("Quyidagi so'rovlardan birini tanlang", reply_markup=rkm)


@dp.message(Command('evos'))
async def reply_evos_button_handler(message: Message) -> None:
    design = [
        [
            KeyboardButton(text="What are you hours?"),
            KeyboardButton(text="What is your name")
        ],
        [
            KeyboardButton(text="Can I track my orders?")
        ],
        [
            KeyboardButton(text="How do I report a problem?"),
            KeyboardButton(text="How do I report a problem?")
        ],
        [
            KeyboardButton(text="How do I report a problem?"),
            KeyboardButton(text="How do I report a problem?")
        ]
    ]

    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
    await message.answer("Quyidagi so'rovlardan birini tanlang", reply_markup=rkm)


@dp.message(Command('inline'))
async def reply_inline_button_handler(message: Message) -> None:
    design = [
        [
            InlineKeyboardButton(text="Python", callback_data="python"),
            InlineKeyboardButton(text="❌", callback_data="x1")
        ],
        [
            InlineKeyboardButton(text="Choose", callback_data="choose"),
            InlineKeyboardButton(text="❌", callback_data="x2")
        ],
        [
            InlineKeyboardButton(text="C#", callback_data="c#"),
            InlineKeyboardButton(text="❌", callback_data="x3")
        ]
    ]

    rkm = InlineKeyboardMarkup(inline_keyboard=design)
    await message.answer("Quyidagi so'rovlardan birini tanlang", reply_markup=rkm)


@dp.message(Command('phone_number'))
async def phone_number_handler(message: Message) -> None:
    design = [
        [
            KeyboardButton(text='Click to send phone number', request_contact=True),
            KeyboardButton(text='Click to send location', request_location=True)
        ]
    ]

    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
    await message.answer(text='Telefon nomeringizni yuboring', reply_markup=rkm)


@dp.message(F.contact)
async def contact_handler(message: Message) -> None:
    await message.answer(text=message.contact.phone_number)


@dp.message(F.location)
async def location_handler(message: Message) -> None:
    await message.answer(text=f"{message.contact.latitude}, {message.contact.longitude}")


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