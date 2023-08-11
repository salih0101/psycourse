from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup


def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('ОТПРАВИТЬ НОМЕР ТЕЛЕФОНА', request_contact=True)
    kb.add(button)

    return kb


def trial_time_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    lang = KeyboardButton("O'zbek")
    lang1 = KeyboardButton('Русский')

    kb.add(lang, lang1)

    return kb


def main_menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    set_subscribe = KeyboardButton('📝Оплата за курс')
    profile = KeyboardButton('⚙️НАСТРОЙКА')
    courses = KeyboardButton('📚КУРСЫ')

    kb.add(courses, set_subscribe, profile)

    return kb


def settings_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    change = KeyboardButton('👤ПОЛЬЗОВАТЕЛЬ')
    check = KeyboardButton('✅ПРОВЕРИТЬ ПОДПИСКУ')
    back = KeyboardButton('Haзад')
    kb.add(change, back)

    return kb


def change_data_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    ch_name = KeyboardButton('Изменить имя')
    ch_number = KeyboardButton('Изменить номер')
    back = KeyboardButton('Hазад')
    kb.add(ch_name, ch_number, back)

    return kb


def course_order_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    set_subscribe = KeyboardButton('📝ОФОРМИТЬ ПОДПИСКУ')

    kb.add(set_subscribe)

    return kb
