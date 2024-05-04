import telebot
from telebot import types


bot = telebot.TeleBot('6890583766:AAGQJggKd7PMXToN2mNx1zOeit49efm8oF4')



@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Я работодатель', callback_data= 'rabotodatel')
    btn2 = types.InlineKeyboardButton('Я ищу работу', callback_data= 'user')
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(message.chat.id, 'Привет, я ЭйДжэй бот. Выбери, кто ты и поехали)', reply_markup = markup)





@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "rabotodatel":
        bot.delete_message(callback.message.chat.id,callback.message.message_id)
        bot.send_message(callback.message.chat.id, '/rabot')

    elif callback.data == "user":
        bot.send_message(callback.message.chat.id, "Прекрасно, тогда заполните анкету, которая будет передана работодателю")
        bot.delete_message(callback.message.chat.id,callback.message.message_id)

@bot.message_handler(commands=['rabot'])
def rabotodatel_f(message):
    bot.delete_message(message.chat.id,message.message_id-1)
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Создать открытую ваканисию')
    markup.row(btn1)
    bot.send_message(message.chat.id, 'Хорошо, тогда разместите вакансию, на которую ищите специалиста', reply_markup= markup)        




bot.polling(none_stop = True)