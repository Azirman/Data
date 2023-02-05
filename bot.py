import telebot
from telebot import types
bot = telebot.TeleBot("6134274844:AAETBT-DiyuLxxIR9z3L5BQt-A9iThoNWow")
@bot.message_handler(commands=["start"])
def inline(message):
    key = types.InlineKeyboardMarkup()
    but_2 = types.InlineKeyboardButton(text="Черт", callback_data="data_1")
    but_3 = types.InlineKeyboardButton(text="Ебланище", callback_data="data_2")
    but_4 = types.InlineKeyboardButton(text="Дима", callback_data="data_3")
    but_5 = types.InlineKeyboardButton(text="Дальше", callback_data="data_4")
    key.add(but_2, but_3, but_4, but_5)
    bot.send_message(message.chat.id, "Представься на хуй", parse_mode='Markdown', reply_markup=key)
@bot.callback_query_handler(func=lambda c: True)
def inlin(c):
    if c.data == 'data_1':
        bot.send_message(c.message.chat.id, "Все верно, ты именно беспросветный черт-ебун:)))")
    if c.data == 'data_2':
        bot.send_message(c.message.chat.id, "ВСЕ ВЕРНО ХУЕСОС, ты самый настоящий Еблан!")
    if c.data == 'data_3':
        bot.send_message(c.message.chat.id, "Добрый день полурослик.")
    if c.data == 'data_4':
        bot.send_message(c.message.chat.id, "Окей :0\nТы наконец-то решил продвинуться !")

@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "Черт":
        bot.send_message(message.from_user.id, "Очень приятно, а меня зовут CocoJambo228, Что вы именно хотите ?")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Напиши мне: \nЧерт, либо представься как тебя зовут.")
    else:
        bot.send_message(message.from_user.id, "Нормально пизди полурослик:)\nпросто напиши команду /start")
#my_id = "474635851"
    #bot.send_message(message.from_user.id, message.text)


bot.polling(none_stop=True, interval=0)






#474635851
#👋