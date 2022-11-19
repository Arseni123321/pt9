from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os


bot = Bot('5882944378:AAHd1d93TBaG7IipIDhsqyMcrDfjAhsFu3k')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hi, Im stupid bot')

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp, skip_updates=True)