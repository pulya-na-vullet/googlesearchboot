import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from googlesearch import search

TOKEN = 'Введи сюда свой токен'
#токен для своего телеграмм бота можно получть в https://t.me/BotFather 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Давай что нибудь поищем в сети?")

async def search_google(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    search_results = list(search(query, num=1, stop=1))
    
    if len(search_results) > 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Вот что я смог найти: {search_results[0]}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Извини, я не смог найти релевантный результат.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT, search_google)
    
    application.add_handler(start_handler)
    application.add_handler(message_handler)
    
    application.run_polling()