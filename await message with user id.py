import logging
from aiogram import Bot, Dispatcher, executor, types 

logging.basicConfig(level=logging.INFO)

bot = Bot(token = "")

dp = Dispatcher(bot)
    
@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)