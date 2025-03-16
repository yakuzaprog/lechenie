import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Тексты для ответов
ALCOHOL_INFO = """
📖 *Как лечить алкогольную зависимость*

Статья: [Ссылка на статью](https://example.com)

👥 *Контакты специалистов:*
- Иван Иванов — нарколог: +7 900 000‑00‑00
- Центр помощи «Новая жизнь»: @newlife_center
"""

DRUG_INFO = """
📖 *Как лечить наркотическую зависимость*

Статья: [Ссылка на статью](https://example.com)

👥 *Контакты специалистов:*
- Алексей Петров — психиатр-нарколог: +7 911 111‑11‑11
- Реабилитационный центр «Путь»: @rehab_path
"""

CODEPENDENCY_INFO = """
🎥 *Лекции по теме созависимости:*
1. [Что такое созависимость](https://example.com/lecture1)
2. [Как выйти из круга](https://example.com/lecture2)

👥 *Контакт психолога:*
- Мария Смирнова — семейный психолог: +7 922 222‑22‑22
- Telegram: @maria_psy
"""

GAMBLING_INFO = """
🎯 *Как справиться с игровой зависимостью*

Статья: [Преодоление лудомании](https://example.com/gambling)

👥 *Контакты специалистов:*
- Сергей Кузнецов — психолог по зависимостям: +7 933 333‑33‑33
- Telegram: @sergey_gambling_help
"""

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота
TOKEN = "ТВОЙ_ТОКЕН_БОТА"


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"Пользователь {update.message.from_user.id} запустил бота.")
    keyboard = [
        [InlineKeyboardButton("🍺 Алкоголь", callback_data='alcohol')],
        [InlineKeyboardButton("💊 Наркотики", callback_data='drugs')],
        [InlineKeyboardButton("🤝 Созависимость", callback_data='codependency')],
        [InlineKeyboardButton("🎰 Игровая зависимость", callback_data='gambling')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Привет! С чем связана ваша ситуация?\nВыберите вид зависимости:",
        reply_markup=reply_markup
    )


# Обработка нажатий на кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    if data == 'alcohol':
        await query.message.reply_text(
            ALCOHOL_INFO,
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    elif data == 'drugs':
        await query.message.reply_text(
            DRUG_INFO,
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    elif data == 'codependency':
        await query.message.reply_text(
            CODEPENDENCY_INFO,
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    elif data == 'gambling':
        await query.message.reply_text(
            GAMBLING_INFO,
            parse_mode="Markdown",
            disable_web_page_preview=True
        )

    # Добавляем кнопку "Назад"
    keyboard = [[InlineKeyboardButton("⬅️ Назад", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)


# Обработка кнопки "Назад"
async def back_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Возвращаем пользователя к начальному меню
    await start(update, context)


# Запуск бота
def main():
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CallbackQueryHandler(back_button, pattern='back'))

    # Запускаем бота
    logger.info("Бот запущен.")
    application.run_polling()


if __name__ == '__main__':
    main()
