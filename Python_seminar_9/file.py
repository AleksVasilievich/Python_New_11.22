from telegram import Bot
from telegram.ext import Updater, CommandHandler

bot = Bot(token = '')                     # Создаём бота
updater = Updater(token = '')     # Здесь будут хронится все обновления нашего чата,имя id и вся ифа.
dispatcher = updater.dispatcher   # Переменная которая будет хранить всё что в updater 

def start(update, context):        # Функция - (update и context - всегда ! ) 1 - инфа о чате, 2 - встроинные команды 
    context.bot.send_message(update.effective_chat.id, "Hello")     # команда ответа бота

start_handler = CommandHandler("start", start)     # Если человек боту напишет "/start", то он запустит функцию старт
                                                   # Функция выполница, бот ответит "Hello"
                                                   
dispahather.add_handler(start_handler)             # Обучаем бота добовленным фунциям, которые мы прописали ранее

updater.start_polling()      # Старт программы
updater.idle()               # Конец программы