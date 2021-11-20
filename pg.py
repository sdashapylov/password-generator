import random
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2114579841:AAFRsgLhy200qbHs_WqD10HLVmJRFHGbs5A'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ PassBot!\nСоздан в ASPIRE.")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Используй команду\n /gen")

@dp.message_handler(commands=['generate', 'gen'])
async def echo(message: types.Message):

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    all = lower + upper + numbers + symbols
    length = 16
    
    password = ''.join(random.sample(all, length))

    await message.reply('Ваш новый пароль: ' + password)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)