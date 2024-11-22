from telebot import types

def lang_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lang1 = types.KeyboardButton('Русский')
    lang2 = types.KeyboardButton('English')
    kb.add(lang1, lang2)
    return kb

def lang_buttons():
    kb = types.InlineKeyboardMarkup(row_width=2)
    lang1 = types.InlineKeyboardButton(text='Русский', callback_data='ru')
    lang2 = types.InlineKeyboardButton(text='English', callback_data='en')
    kb.add(lang1, lang2)
    return kb

def tel_button_ru():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Отправить номер 📞', request_contact=True)
    kb.add(item1)
    return kb

def tel_button_en():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Send my number 📞', request_contact=True)
    kb.add(item1)
    return kb