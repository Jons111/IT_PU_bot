from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_button = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text='ITPU'),

    ]
    ],
    resize_keyboard=True
)

main_button_ru = ReplyKeyboardMarkup(
    keyboard=[[

        KeyboardButton(text='ITPU_RU')
    ]
    ],
    resize_keyboard=True
)

university_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ITPU haqida'),
            KeyboardButton(text="ITPU  Yo'nalishlar"),

        ],

    ],
    resize_keyboard=True
)

university_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Об ITPU'),
            KeyboardButton(text="Факультеты ITPU"),

        ],

    ],
    resize_keyboard=True
)