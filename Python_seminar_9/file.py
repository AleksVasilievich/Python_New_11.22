from telegram import Bot
from telegram.ext import Updater, CommandHandler

bot = Bot(token = '')
updater = Updater(token = '')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Hello")

start_handler = CommandHandler("start", start)

dispahather.add_handler(start_handler)
updater.start_polling()
updater.idle()