import logging
from aiogram import Bot,Dispatcher, types

bot_token ="7800832102:AAF9Zz2dKmD3yGNNWnjsdmlXr9cA-z056s8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp=Dispatcher(bot)

@dp.message_hundler(commands=['start'])
async def salom(message: types.Message):
  await message.answer('Salom botga hush kelibsiz')

@dp.message_hundler(commands=['go'])
async def test(message: types.Message):
    await message.answer('qalesz')


