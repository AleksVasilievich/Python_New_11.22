from controller import line, calaulate
from log import id_user, input_data, results,write_log
from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler

bot = Bot(token = '5548072895:AAFZOcvGv2XKPHcv_vikG0LLVxvscO9vnQw')                    
updater = Updater(token = '5548072895:AAFZOcvGv2XKPHcv_vikG0LLVxvscO9vnQw')     
dispatcher = updater.dispatcher   

def start(update, context):        
    context.bot.send_message(update.effective_chat.id, 'Привет , давай посчитаем')    
    context.bot.send_message(update.effective_chat.id, 'Напишите мне арифметическое выражение ')
    id_user(update.effective_chat.id)


def text_task(update, context):
    text = update.message.text
    input_data(text)
    data = line(st)
    result = callable(data)
    
    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')

    # return ConversationHandler.END

start_handler = CommandHandler('start', start)    
                                                

text_task_handler = MessageHandler(Filters.text, text_task)



dispatcher.add_handler(start_handler)            

dispatcher.add_handler(text_handler)

updater.start_polling()     
updater.idle()              