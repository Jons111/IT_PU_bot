from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿 Uz', callback_data='Uzb'),
            InlineKeyboardButton(text='🇷🇺 Ru', callback_data='Rus'),
        ],
        [
            InlineKeyboardButton(text='Share 📣',
                                 switch_inline_query="\n 🇺🇿 ITPU so'rov telegram bot \n 🇷🇺 ITPU опросник телеграм бот")
        ]
    ]
)
inline_pre = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ha', callback_data='1'),
            InlineKeyboardButton(text="Yo'q", callback_data='2'),
        ],

    ]
)


inline_pre_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='1'),
            InlineKeyboardButton(text="Нет", callback_data='2'),
        ],

    ]
)
