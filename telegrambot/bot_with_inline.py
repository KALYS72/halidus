import telebot

from decouple import config
token = config('TOKEN')
bot = telebot.TeleBot(token)


keyboard = telebot.types.InlineKeyboardMarkup()
button1 = telebot.types.InlineKeyboardButton('Да',callback_data='yes')
button2 = telebot.types.InlineKeyboardButton('Нет',callback_data='no')
keyboard.add(button1,button2)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEGOphjW2moIoaRV2zdTzIRRJgnvOybcAACuhoAAirCKEtHodmNi65oFyoE',reply_markup=keyboard)

@bot.callback_query_handler(func=lambda x:True)
def repl(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id,'CAACAgIAAxkBAAEGOrtjW2nwMXDMN19UgSjfcX2RplqMIgAC-BoAAt0oMUs4yX8hzpAi2yoE')
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id,'CAACAgIAAxkBAAEGOvBjW2wIHsfUhpD1OnUNYWbxFOn4GAAC-RgAAuQjoEk3wXiGTOACqyoE')


bot.polling()