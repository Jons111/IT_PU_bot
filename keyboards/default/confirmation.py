from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

confirmation_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ha')
        ],
        [
            KeyboardButton(text="Yo'q")
        ]
    ],
    resize_keyboard=True
)

confirmation_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да')
        ],
        [
            KeyboardButton(text="Нет")
        ]
    ],
    resize_keyboard=True
)
