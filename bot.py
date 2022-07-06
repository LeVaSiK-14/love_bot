import telebot
from random import choice

TOKEN = '5372565381:AAGJ3YUDji2SuN55FhNJepp5lfuvoXCRVic'

bot = telebot.TeleBot(TOKEN)

love_text1 = 'I love you, my princess❤️❤️'
love_text2 = 'Ты самая лучшая❤️❤️'
love_text3 = 'Я люблю тебя❤️❤️'
love_text4 = 'Ты самая красивая❤️❤️'
love_text5 = 'Ты моя принцесса❤️❤️'
love_text6 = 'Ты самая милая❤️❤️'
love_text7 = 'Я тебе кохаю❤️❤️'
love_text8 = '❤️'

love_arr = [love_text1, love_text2, love_text3, love_text4, love_text5, love_text6, love_text7, love_text8]

@bot.message_handler(commands=['start'])
def send_mess_love(message):
    chat_id = message.chat.id
    print(message)
    print(chat_id)
    bot.send_message(chat_id, 'Привет, введи число от 1 до 100 :)')



@bot.message_handler(content_types=['text'])
def send_mess_love(message):
    chat_id = message.chat.id
    marisha_id = 5204404143
    try:
        quantity = int(message.text) + 1
        for i in range(1, quantity):
            rand_love = (f'{i}) {choice(love_arr)}')

            bot.send_message(marisha_id, rand_love)
    except:
        bot.send_message(chat_id, 'Введи число красавица моя😂😂')


if __name__ == '__main__':
    bot.polling(none_stop = True)