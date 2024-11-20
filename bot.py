import telebot
import datab, buttons

bot = telebot.TeleBot('8164538734:AAEtE9H4ex65jGQb8W-U6cOcLiDBIg')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if datab.check_user(user_id):
        user_name = datab.get_name(user_id)
        bot.send_message(user_id, f'{user_name}, с возвращением!', reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, f'Приветствуем!\nЧтобы продолжить, введите своё имя.',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)

@bot.message_handler(content_types=['text'])
def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, f'{user_name}, приятно познакомиться! 😊\n'
                              f'Отправьте нам свой номер телефона, чтобы мы могли связаться с вами.', reply_markup=buttons.tel_button())
    bot.register_next_step_handler(message, get_tel, user_name)

def get_tel(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        user_tel = message.contact.phone_number
        datab.register(user_id, user_name, user_tel)
        bot.send_message(user_id, 'Ура! Регистрация пройдена! 🥳', reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, 'Отправьте контакт через кнопку "Отправить номер" или прикрепите его в виде вложения через скрепку.')
        bot.register_next_step_handler(message, get_tel, user_name)

bot.polling(non_stop=True)