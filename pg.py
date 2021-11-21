import random
import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nВведи длину символов пароля от 3 до 30")

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        number = int(message.text)
        if number <= 2:
            await message.answer('Введите цифру больше 3')
        elif number >= 31:
            await message.answer("Введите цифру меньше 30")
        else:
            lower = 'abcdefghijklmnopqrstuvwxyz'
            upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numbers = '0123456789'
            symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

            all = lower + upper + numbers + symbols
            length = int(message.text)
            
            password = ''.join(random.sample(all, length))

            await message.answer('Ваш новый пароль: ' + password)
    else:
        await message.answer('Введите цифру обозначающую длину пароля от 3 до 30')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)