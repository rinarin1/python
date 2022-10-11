from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import emoji

TOKEN = ''

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)
Base = declarative_base()
class MediaTable(Base):
    __tablename__ = 'Media table'
    id = Column(Integer, primary_key=True)
    file_id = Column(String(255))
    filename = Column(String(255))
@dp.message_handler(commands = ['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет!\nНапиши мне что-нибудь! \nИспользуй кнопку help , чтобы узнать список доступных команд\.", parse_mode='MarkdownV2')
@dp.message_handler(commands = ['help'])
async def process_help_command(message: types.Message):
    await message.answer("Я могу ответить на следующие кнопки: \nvoice, \nphoto, \ngroup, \nnote, \nfile\.", parse_mode="MarkdownV2")
@dp.message_handler(commands='audio')
async def sadsvit_caseta(message: types.Message):
    await message.reply_audio('CQACAgIAAxkBAAOoY0VnKsONOJjWRtJyc0IchT7DrSwAAs4bAAKFyDBKILGp1ZdyccEqBA')
    await message.reply_audio('CQACAgIAAxkBAAOvY0VqWijl9ZHhsLcW-KpaH0m_V4oAAtMbAAKFyDBK43PDwkMpFKUqBA')
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