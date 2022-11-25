from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler 

bot = Bot(token = "5548072895:AAFZOcvGv2XKPHcv_vikG0LLVxvscO9vnQw")
updater = Updater(token="5548072895:AAFZOcvGv2XKPHcv_vikG0LLVxvscO9vnQw")
dispatcher = updater.dispatcher


A = 0
B = 1

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет, \n как у тебя дела ?")
    return A

def voice(update, context):
    context.bot.send_message(update.effective_chat.id, 'Я не умею обрабатывать гс')

def text(update, context):
    text = update.message.text
    if 'прив' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Привет как у тебя дела ?')

def howareyou(update, context):
    text = update.message.text
    if 'хор' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Я рад что у тебя всё хорошо !')
    else:
        context.bot.send_message(update.effective_chat.id, 'Не переживай всё будет хорошо !')
    context.bot.send_message(update.effective_chat.id, 'Как у тебя погода ?')
    return B

def weather(update, context):
    text = update.message.text
    if 'хор' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'У меня тоже солнце !')
    else:
        context.bot.send_message(update.effective_chat.id, 'У природы нет плохой погоды !')

    return ConversationHandler.END
    
def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'До встречи !')

start_handler = CommandHandler("start", start)
mes_haware_handler = MessageHandler(Filters.text, howareyou)
mes_weather_handler = MessageHandler(Filters.text, weather)
message_handler = MessageHandler(Filters.voice, voice)    #Filters.дальше могут быть другие функции
mes_text_handler = MessageHandler(Filters.text, text)
mes_canc_handler = MessageHandler(Filters.text, cancel)


conv_handler = ConversationHandler(entry_points=[start_handler], 
                                  states={A: [mes_haware_handler],
                                          B: [mes_weather_handler]},
                                  fallbacks=[mes_canc_handler])
                            

dispatcher.add_handler(conv_handler)

# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(mes_haware_handler)
# dispatcher.add_handler(mes_weather_handler)
# dispatcher.add_handler(message_handler)
# dispatcher.add_handler(mes_text_handler)
# dispatcher.add_handler(mes_canc_handler)


updater.start_polling()                  #запуск нашей программы
updater.idle()                           #остановка программы