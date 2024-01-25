import telebot
api_token = '6953163476:AAGSosLT78LMgQecZJvz5XGt0Mz7K4OUMIw'
bot = telebot.TeleBot(api_token)

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, text=f"{message.text}")
bot.polling()