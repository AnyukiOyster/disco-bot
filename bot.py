import telebot
import datab, buttons

bot = telebot.TeleBot('8164538734:AAEtE9H4ex65jGQb8W-U6cOcLiDBIg')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'Чтобы продолжить, выберите язык.\n\nChoose language to continue.', reply_markup=buttons.lang_button())
    bot.register_next_step_handler(message, choose_lang)

def choose_lang(message):
    user_id = message.from_user.id
    if message.text == 'Русский':
        if datab.check_user(user_id):
            user_name = datab.get_name(user_id)
            bot.send_message(user_id, f'{user_name}, с возвращением!', reply_markup=telebot.types.ReplyKeyboardRemove())
        else:
            bot.send_message(user_id, f'Приветствуем!\nЧтобы продолжить, введите своё имя.', reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_name_ru)
    elif message.text == 'English':
        if datab.check_user(user_id):
            user_name = datab.get_name(user_id)
            bot.send_message(user_id, f'Welcome back, {user_name}!', reply_markup=telebot.types.ReplyKeyboardRemove())
        else:
            bot.send_message(user_id, f'Hello!\nPlease enter your name.', reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, get_name_en)
    else:
        bot.send_message(user_id, f'Введена некорректная команда. Чтобы продолжить, выберите язык с помощью одной из кнопок ниже.\n\n'
                                      f'Incorrect input. Please choose your preferred language via buttons below.')

def get_name_ru(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, f'{user_name}, приятно познакомиться! 😊\n'
                              f'Отправьте нам свой номер телефона, чтобы мы могли связаться с вами.', reply_markup=buttons.tel_button_ru())
    bot.register_next_step_handler(message, get_tel_ru, user_name)

def get_tel_ru(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        user_tel = message.contact.phone_number
        datab.register(user_id, user_name, user_tel)
        bot.send_message(user_id, 'Ура! Регистрация пройдена! 🥳', reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, 'Отправьте контакт через кнопку "Отправить номер" или прикрепите его в виде вложения через скрепку.')
        bot.register_next_step_handler(message, get_tel_ru, user_name)

def get_name_en(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, f'Nice to meet you, {user_name}! 😊\n'
                              f'Please send us your number so we could get in tough with you.', reply_markup=buttons.tel_button_en())
    bot.register_next_step_handler(message, get_tel_en, user_name)

def get_tel_en(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        user_tel = message.contact.phone_number
        datab.register(user_id, user_name, user_tel)
        bot.send_message(user_id, 'Registration is complete! 🥳', reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, 'To send you contact information use the "Send my number" button or send it as an attachment.')
        bot.register_next_step_handler(message, get_tel_en, user_name)

bot.polling(non_stop=True)