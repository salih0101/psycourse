from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup


def uz_phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Telefon raqamni yuborish", request_contact=True)
    kb.add(button)

    return kb



def uz_main_menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    set_subscribe = KeyboardButton("📝Kurs uchun to'lov")
    profile = KeyboardButton('⚙️Sozlamalar')
    courses = KeyboardButton('📚Kurslar')

    kb.add(courses, set_subscribe, profile)

    return kb


def uz_settings_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    change = KeyboardButton('👤Profil')
    back = KeyboardButton('Ortga qаytish')
    kb.add(change, back)

    return kb


def uz_change_data_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    ch_name = KeyboardButton("Ismni o'zgratirish")
    ch_number = KeyboardButton("Raqamni o'zgratirish")
    back = KeyboardButton('Ortgа qaytish')
    kb.add(ch_name, ch_number, back)

    return kb


def uz_course_order_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    set_subscribe = KeyboardButton("📝Obuna bo'lish")

    kb.add(set_subscribe)

    return kb
