from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher.filters import Text

TOKEN = '5640107061:AAFSseTGf8uiLYB4yY8eNXi2V5R73dLBxsc'

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


   
@dp.message_handler(commands = ['start'])
async def music(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="музыка")
    keyboard.add(button_1)
    await message.answer("Привет\!\nНапиши мне что\-нибудь\.\nИспользуй комманду /help  чтобы узнать список доступных команд\.", parse_mode = 'MarkdownV2', reply_markup = keyboard)

@dp.message_handler(lambda message: message.text == "музыка")
async def l_s_theme(message: types.Message):
    buttons = [types.InlineKeyboardButton(text = "L\'s theme A", callback_data = "muz_a"),
               types.InlineKeyboardButton(text = "L\'s theme B", callback_data = "muz_b")]
    keyboard = types.InlineKeyboardMarkup(row_width = 1)
    keyboard.add(*buttons)
    await message.answer("Выбери трек:", reply_markup = keyboard)


@dp.callback_query_handler(Text(startswith = "muz_"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split("_")[1]
    if action == "a":
        await call.message.reply_audio('CQACAgIAAxkBAAIBc2OJ88uexdTZR4dDJub5ltwHBD9wAAIbIwACs5hQSEG9pbV3rtfJKwQ')
        await call.answer(text="Спасибо, что воспользовались ботом!", show_alert = True)
    elif action == "b":
        await call.message.reply_audio('CQACAgIAAxkBAAIBcGOJ85SP4mr7-63AAAFN5mrsuBZD2QACGCMAArOYUEgujmOL2mgAAQ4rBA')
        await call.answer(text="Спасибо, что воспользовались ботом!", show_alert = True)

@dp.message_handler(commands = ['help'])
async def process_help_command(message: types.Message):
    await message.answer("Я могу ответить на следующие кнопки: \n музыка", parse_mode="MarkdownV2")

@dp.message_handler(content_types=[types.ContentType.AUDIO])
async def echo_document(message: types.Message):
    await message.reply_audio(message.audio.file_id)
    await message.reply(message.audio.file_id)

@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text.lower() == 'привет':
        await bot.send_message(message.from_user.id, 'Привет!')
    elif message.text.lower() == 'как дела':
        await bot.send_message(message.from_user.id, 'У меня все хорошо. А у тебя?')
    elif message.text.lower() == 'норм':
        await bot.send_message(message.from_user.id, 'Пон')
    else:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp)