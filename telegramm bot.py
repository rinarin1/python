from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands = ['start'])
async def process_start_command(msg: types.Message):
    await msg.reply("Привет!\nНапиши мне что-нибудь!")
@dp.message_handler(commands = ['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")
@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text.lower() == 'привет':
        await bot.send_message(msg.from_user.id, 'Привет!')
    elif msg.text.lower() == 'как дела':
        await bot.send_message(msg.from_user.id, 'У меня все хорошо. А у тебя?')
    elif msg.text.lower() == 'норм':
        await bot.send_message(msg.from_user.id, 'Пон')
    else:
        await bot.send_message(msg.from_user.id, msg.text)
if __name__ == '__main__':
    executor.start_polling(dp)