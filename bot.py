import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5714270219:AAGPXR6snLswGnRNtTwJI9bEPWorR4Gko7s'
ADMIN = 880280670

logging.basicConfig(level=logging.INFO)

proxy_url = 'http://proxy.server:3128'
bot = Bot(token=TOKEN, proxy=proxy_url)
dp = Dispatcher(bot)

l = [
    'š  š¹š¹š¹\nš¹š¹         š¹š¹\nš¹š¹\nš¹š¹   š¹š¹š¹\nš¹š¹         š¹š¹\n    š¹š¹š¹š¹',
    'šš¹š¹š¹š¹       š¹š¹\nš¹š¹         š¹š¹   š¹š¹\nš¹š¹          š¹š¹\nš¹š¹          š¹š¹\nš¹š¹         š¹š¹\n    š¹š¹š¹š¹',
    'šš¹š¹š¹š¹š¹\n                       š¹š¹\n                  š¹š¹\n           š¹š¹\n      š¹š¹\nš¹š¹š¹š¹š¹š¹',
    'š        š¹š¹\n            š¹ š¹š¹\n        š¹š¹  š¹š¹\n     š¹š¹       š¹š¹\n  š¹š¹š¹š¹š¹š¹\nš¹š¹                 š¹š¹',
    'šš¹\nš¹š¹\nš¹š¹\nš¹š¹\nš¹š¹\nš¹š¹š¹š¹š¹š¹',
    'š§øš¤',
    'for Guzal by @obloevkomronbek ā¤ļø'
]


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    for i in l:
        await message.answer(i)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
