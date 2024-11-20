from telebot import types

def tel_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Отправить номер 📞', request_contact=True)
    kb.add(item1)
    return kb