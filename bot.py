import telebot 
from telebot import types
import sqlite3

bot = telebot.TeleBot('6890583766:AAGQJggKd7PMXToN2mNx1zOeit49efm8oF4')
uname = None
passw = None

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Зарегистрироваться")
    markup.row(btn1)

    bot.send_message(message.chat.id, 'Привет, чтобы начать работу выбери, кто ты', reply_markup = markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Зарегистрироваться":
        conn = sqlite3.connect(r'D:\Proga\telegram bot\main_bot.sql')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), pass varchar(50))')

        conn.commit()
        cur.close()
        conn.close()
        
        bot.send_message(message.chat.id, 'Придумай и отправь мне твой логин')
        bot.register_next_step_handler(message, username)

def username(message):
    global uname
    uname = message.text.strip()
    bot.send_message(message.chat.id, 'Прекрасно, теперь пароль')
    bot.register_next_step_handler(message, password)

def password(message):
    global passw
    passw= message.text.strip()
    conn = sqlite3.connect(r'D:\Proga\telegram bot\main_bot.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users(name, pass) VALUES ("%s", "%s")' % (uname, passw))

    conn.commit()
    cur.close()
    conn.close()

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Узнать данные аккаунта")
    btn2 = types.KeyboardButton("Мои мероприятия")
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(message.chat.id, 'Поздравляю, ты успешно зарегистрирован!', reply_markup=markup)
    bot.register_next_step_handler(message, menu)

def menu(message):
    if message.text == "Узнать данные аккаунта":
        pass
    elif message.text == "Мои мероприятия":
        pass

    #Сделать меню, где пользователь может проверить свой логин и пароль
    pass

bot.polling(none_stop = True)