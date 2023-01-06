import telebot
from decouple import config



token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','hello'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')
    # отправить текстовое сообщение

    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGOYBjW12jb8SWxr8FhmWeyjhfnb1-iQACUxsAAvjkqEnKqaBqMN7P_CoE')
    # отправить стикер, чтобы получит id стикера @idstickerbot

    bot.send_photo(message.chat.id, 'https://www.google.com/imgres?imgurl=http%3A%2F%2Fsun9-13.userapi.com%2Fimpg%2Fc855736%2Fv855736186%2F213b49%2FFW46-YmEouA.jpg%3Fsize%3D346x604%26quality%3D96%26sign%3D6c3292e775640bee90dd5a2e19cc0d54%26type%3Dalbum&imgrefurl=https%3A%2F%2Fvk.com%2Fwall-73192688_57744&tbnid=YeG9fpC0dv471M&vet=12ahUKEwjN78aAj4L7AhUpmIsKHUtIB0YQMygEegUIARCWAQ..i&docid=E2mI4Z-AZrJjuM&w=346&h=604&q=gachi%204k&client=ubuntu&ved=2ahUKEwjN78aAj4L7AhUpmIsKHUtIB0YQMygEegUIARCWAQ')
    # отправить фото

    with open('/home/vivobook/Pictures/index.jpeg', 'rb') as img:
        bot.send_photo(message.chat.id, img)
    # отправить фото с компьютера


bot.polling()
# запуск бота
