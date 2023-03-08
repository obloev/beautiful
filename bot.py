import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5714270219:AAGPXR6snLswGnRNtTwJI9bEPWorR4Gko7s'
ADMIN = 880280670

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

l = [
    '🍀  🌹🌹🌹\n🌹🌹         🌹🌹\n🌹🌹\n🌹🌹   🌹🌹🌹\n🌹🌹         🌹🌹\n    🌹🌹🌹🌹',
    '🍀🌹🌹🌹🌹       🌹🌹\n🌹🌹         🌹🌹   🌹🌹\n🌹🌹          🌹🌹\n🌹🌹          🌹🌹\n🌹🌹         🌹🌹\n    🌹🌹🌹🌹',
    '🍀🌹🌹🌹🌹🌹\n                       🌹🌹\n                  🌹🌹\n           🌹🌹\n      🌹🌹\n🌹🌹🌹🌹🌹🌹',
    '🍀        🌹🌹\n            🌹 🌹🌹\n        🌹🌹  🌹🌹\n     🌹🌹       🌹🌹\n  🌹🌹🌹🌹🌹🌹\n🌹🌹                 🌹🌹',
    '🍀🌹\n🌹🌹\n🌹🌹\n🌹🌹\n🌹🌹\n🌹🌹🌹🌹🌹🌹',
    '🧸🤍',
    'for Guzal by @obloevkomronbek ❤️'
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
