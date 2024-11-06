from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Стоимость'),
            KeyboardButton(text='О нас')
        ],
        [
            KeyboardButton(text='Купить')
        ]
    ], resize_keyboard=True
)


catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Bitch game', callback_data='bitch')],
        [InlineKeyboardButton(text='Midle game', callback_data='middle')],
        [InlineKeyboardButton(text='Big game', callback_data='big')],
        [InlineKeyboardButton(text='More game', callback_data='other')]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Buy', url='https://www.google.ru/?hl=ru')],
        [InlineKeyboardButton(text ='Back', callback_data='back_to_catalog')]
    ]
)

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пользователи', callback_data='users')],
        [InlineKeyboardButton(text='Статистика', callbakc_data='stat')],
        [
            InlineKeyboardButton(text='Блокировка', callback_data='block'),
            InlineKeyboardButton(text='Разблокировка', callback_data='unblock'),
        ]
    ]
)