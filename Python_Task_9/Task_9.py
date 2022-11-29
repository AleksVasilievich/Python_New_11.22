from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

bot = Bot(token = '5548072895:AAFZOcvGv2XKPHcv_vikG0LLVxvscO9vnQw')                     # Создаём бота
updater = Updater(token = '5548072895:AAFZOcvGv2XKPHcv_vikG0LLVxvscO9vnQw')     # Здесь будут хронится все обновления нашего чата,имя id и вся ифа.
dispatcher = updater.dispatcher   # Переменная которая будет хранить всё что в updater 

def start(update, context):        # Функция - (update и context - всегда ! ) 1 - инфа о чате, 2 - встроинные команды 
    context.bot.send_message(update.effective_chat.id, 'Hello')     # команда ответа бота
    context.bot.send_message(update.effective_chat.id, 'Напишите мне, я возьму слова где нет "абв"')

def text_filtr(update, context):
    text = update.message.text.split()
    ls = []
    for i in text:
        if 'абв' not in i:
            ls.append(i)
    context.bot.send_message(update.effective_chat.id, ' '.join(ls))


start_handler = CommandHandler('start', start)     # Если человек боту напишет '/start', то он запустит функцию старт
                                                   # Функция выполница, бот ответит "Hello"

text_handler = MessageHandler(Filters.text, text_filtr)


dispatcher.add_handler(start_handler)             # Обучаем бота добовленным фунциям, которые мы прописали ранее

dispatcher.add_handler(text_handler)

updater.start_polling()      # Старт программы
updater.idle()               # Конец программы