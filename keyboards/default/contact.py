from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Telefon raqamini ulashish', request_contact=True)
        ]
    ],
    resize_keyboard=True
)


contact_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Поделиться номером телефона', request_contact=True)
        ]
    ],
    resize_keyboard=True
)


next_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Next',)
        ]
    ],
    resize_keyboard=True
)