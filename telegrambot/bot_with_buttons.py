INLINE
import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

# клавиатура
keyboard = telebot.types.InlineKeyboardMarkup()
button1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
button2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, 'CAACAgIAAxkBAAEGOvJjW2wbx0ORghuvOfMxW6WYNrgYYAAC-BoAAt0oMUs4yX8hzpAi2yoE')
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, 'CAACAgIAAxkBAAEGOqVjW2m8qpmg5eTUxCebGduCfL5GegACeRcAAvRKAUsu7NezbSnhtioE')


bot.polling()