import telebot
bot = telebot.TeleBot(1849150185:AAHiJW86MLpittnm0Po5mAfbIsdPmzopuo4)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Отлично. Теперь отправьте мне любое сообщение. При отправке не допускайте нецензурных выражений, иначе вы будете забанены и потребуется обращение к администратору. Это не отменяет вашей анонимности. {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if 'хуй' or 'бля' or 'пизд' or 'ебат' or ' сука ' or ' залуп' or ' манда ' in message.text.lower():
        bot.send_message(message.from_user.id, 'Вы забанены. Для разбана пишите @Dgrmn Шутка. Тут пока ничего нет.')

bot.polling(none_stop=True)