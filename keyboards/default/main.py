from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

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

university_button =InlineKeyboardMarkup (
    inline_keyboard=[
        [
            InlineKeyboardButton(text='ITPU haqida',url='https://itpu.uz/about/'),
            InlineKeyboardButton(text="ITPU  Yo'nalishlar",url='https://itpu.uz/epam/'),

        ],

    ],
    resize_keyboard=True
)

university_button_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Об ITPU',url='https://itpu.uz/about/'),
            InlineKeyboardButton(text="Факультеты ITPU",url='https://itpu.uz/epam/'),

        ],

    ],
    resize_keyboard=True
)