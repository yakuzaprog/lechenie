
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from texts import ALCOHOL_INFO, DRUG_INFO, CODEPENDENCY_INFO, GAMBLING_INFO

API_TOKEN = '7682107039:AAGBFoPhVz3F24Gw9M_LLQ-cbS-_B5rU16M'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🍺 Алкоголь", callback_data='alcohol'),
        InlineKeyboardButton("💊 Наркотики", callback_data='drugs'),
        InlineKeyboardButton("🤝 Созависимость", callback_data='codependency'),
        InlineKeyboardButton("🎰 Игровая зависимость", callback_data='gambling')
    )
    await message.answer("👋 Привет! С чем связана ваша ситуация?\nВыберите вид зависимости:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data in ['alcohol', 'drugs', 'codependency', 'gambling'])
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    if data == 'alcohol':
        await bot.send_message(callback_query.from_user.id, ALCOHOL_INFO, parse_mode="Markdown", disable_web_page_preview=True)
    elif data == 'drugs':
        await bot.send_message(callback_query.from_user.id, DRUG_INFO, parse_mode="Markdown", disable_web_page_preview=True)
    elif data == 'codependency':
        await bot.send_message(callback_query.from_user.id, CODEPENDENCY_INFO, parse_mode="Markdown", disable_web_page_preview=True)
    elif data == 'gambling':
        await bot.send_message(callback_query.from_user.id, GAMBLING_INFO, parse_mode="Markdown", disable_web_page_preview=True)

    await bot.answer_callback_query(callback_query.id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
