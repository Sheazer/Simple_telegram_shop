import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import asyncio

from admin import *
from db import *

from config import *
from keyboards import *
import texts

logging.basicConfig(level=logging.INFO)
Bot = Bot(token=API)
dp = Dispatcher(Bot, storage=MemoryStorage())

#message.answer_photo
#message.answer_video
#message.answer_file

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Hi,  {message.from_user.username}!\n'+texts.start, reply_markup=start_kb)


@dp.message_handler(text='О нас')
async def start(message):
    with open('files/1.jpg', 'rb') as img:
        await message.answer_photo(img, texts.about, reply_markup=start_kb)


@dp.message_handler(text='Стоимость')
async def start(message):
    await message.answer('Что вас интересует?', reply_markup=catalog_kb)


@dp.callback_query_handler(text='bitch')
async def buy_m(call):
    await call.message.answer(text=texts.Mgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='middle')
async def buy_l(call):
    await call.message.answer(text=texts.Lgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='big')
async def buy_xl(call):
    await call.message.answer(text=texts.XLgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(text=texts.other, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer('Что вас интересует?', reply_markup=catalog_kb)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
