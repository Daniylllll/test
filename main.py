from aiogram import types, executor, Bot, Dispatcher
from config import TOKEN
import asyncio
from time import time
from urllib.parse import urlparse
from uuid import uuid4
from bs4 import BeautifulSoup
import requests
from aiogram import types, executor, Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import random
from cloudipsp import Checkout, Order

bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def generate_channel_link(channel_username):
    try:
        chat_invite_link = await bot.export_chat_invite_link(chat_id=channel_username)
        return chat_invite_link
    except Exception as e:
        # Обработка возможных ошибок при получении ссылки
        print("Ошибка при создании ссылки:", e)
        return None

@dp.message_handler(commands=['start'])
async def cd_start(message : types.Message):
    channel_username = -1001979936516
    channel_link = await generate_channel_link(channel_username)
    await message.answer(f"Ваше посилання: {channel_link}")

@dp.message_handler(commands=['get_chat_id'])
async def cd_get_chat_id(message : types.Message):
    await message.answer(f"{message.chat.id}")


@dp.message_handler(commands=['finish'], state='*')
async def cd_finish(message : types.Message, state : FSMContext):
    await message.answer("Вы в главном меню:")
    await state.finish()

@dp.message_handler(commands=['help'])
async def cd_help(message : types.Message):
    await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)