from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from controller import line, calaulate 
from log import id_user, input_data, results, write_log


bot = Bot(token = '5548072895:AAFZOcvGv2XKPHcv_vikG0LLVxvscO9vnQw')                     # Создаём бота
updater = Updater(token = '5548072895:AAFZOcvGv2XKPHcv_vikG0LLVxvscO9vnQw')     # Здесь будут хронится все обновления нашего чата,имя id и вся ифа.
dispatcher = updater.dispatcher   # Переменная которая будет хранить всё что в updater 

def start(update, context):        # Функция - (update и context - всегда ! ) 1 - инфа о чате, 2 - встроинные команды 
    context.bot.send_message(update.effective_chat.id, 'Hello')     # команда ответа бота
    context.bot.send_message(update.effective_chat.id, 'Давай посчитаем !')
    id_user(update.effective_chat.id)

def text_filtr(update, context):
    text = update.message.text
    input_data(text)                     # Передача данных для записи в log
    stroka = text                        # Обрабоека данных
    res = line(stroka)                   # Обрабоека данных
    result = calaulate(res)              # Получение результата
    results(result)                      # Переддача результата для записи в log
    write_log()                          # Запуск фунции записи в log
    context.bot.send_message(update.effective_chat.id, result)


start_handler = CommandHandler('start', start)     # Если человек боту напишет '/start', то он запустит функцию старт
text_handler = MessageHandler(Filters.text, text_filtr)

dispatcher.add_handler(start_handler)             # Обучаем бота добовленным фунциям, которые мы прописали ранее
dispatcher.add_handler(text_handler)


updater.start_polling()      # Старт программы
updater.idle()               # Конец программы