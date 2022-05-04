import mysql.connector
import telebot
import random
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="polina"
)

mycursor = mydb.cursor()

bot = telebot.TeleBot("5360551314:AAGBh2Srv9SaAAYywDXIigG9abtgGtatVco")

@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Комедия', 'Драма', 'Ужасы')
    user_markup.row('Боевик', 'Мультфильм')
    bot.send_message(message.from_user.id, 'Добро пожаловать! Что хотите сегодня посмотреть?', reply_markup=user_markup)

@bot.message_handler(commands=["stop"])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.lower() == 'комедия':
        sql = "SELECT * FROM comedies "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        rand = random.randint(1,len(result))
        print(result)
        for i in range(len(result)):
            if result[i][0] == rand:
                bot.send_message(message.chat.id, result[i][1] + "  " +result[i][2] )
                break

    elif message.text.lower() == 'драма':
        sql = "SELECT * FROM dramas"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        rand = random.randint(1, len(result))
        print(result)
        for i in range(len(result)):
            if result[i][0] == rand:
                bot.send_message(message.chat.id, result[i][1] + "  " + result[i][2])
                break
    elif message.text.lower() == 'ужасы':
        sql = "SELECT * FROM horrors"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        rand = random.randint(1, len(result))
        print(result)
        for i in range(len(result)):
            if result[i][0] == rand:
                bot.send_message(message.chat.id, result[i][1] + "  " + result[i][2])
                break
    elif message.text.lower() == 'мультфильм':
        sql = "SELECT * FROM cartoons"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        rand = random.randint(1, len(result))
        print(result)
        for i in range(len(result)):
            if result[i][0] == rand:
                bot.send_message(message.chat.id, result[i][1] + "  " + result[i][2])
                break
    elif message.text.lower() == 'боевик':
        sql = "SELECT * FROM actions"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        rand = random.randint(1, len(result))
        print(result)
        for i in range(len(result)):
            if result[i][0] == rand:
                bot.send_message(message.chat.id, result[i][1] + "  " + result[i][2])
                break

bot.polling(none_stop=True)