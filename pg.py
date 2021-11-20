import random
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2114579841:AAFRsgLhy200qbHs_WqD10HLVmJRFHGbs5A'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nВведи длину символов пароля от 3 до 30")

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


        all = lower + upper + numbers + symbols
        length = int(message.text)
        
        password = ''.join(random.sample(all, length))

        await message.answer('Ваш новый пароль: ' + password)
    else:
        await message.answer('Введите цифру обозначающую длину пароля от 1 до 30')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)