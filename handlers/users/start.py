from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.language import inline_lang
from loader import dp, base, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom 👋🏼, Привет 👋🏼, {message.from_user.full_name}!", reply_markup=inline_lang)


    # name = message.from_user.first_name
    # surname = message.from_user.last_name
    # user = message.from_user.username
    # idd = message.from_user.id
    # try:
    #     base.add_users(name=name, telegram_id=idd, surname=surname, username=user)
    # except Exception as error:
    #     print(error)
    # await message.answer(f"Assalomu aleykum botga xush kelibsiz, {message.from_user.username}!")
