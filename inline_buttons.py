from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# Список курсов
def list_courses():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    course2 = KeyboardButton('Курс "Новая Я" 🌟🎓')
    back = KeyboardButton('Haзaд')
    kb.add(course2, back)

    return kb


# Чтобы начать курс
def some_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    some1 = InlineKeyboardMarkup(text='Начать курс! 🚀📚', callback_data='start')

    kb.add(some1)

    return kb


def sub_channel():
    kb = InlineKeyboardMarkup(row_width=1)
    sub_chan = InlineKeyboardButton(text='Подписаться 👍🔔', url='https://t.me/psychofemme')
    check_chan = InlineKeyboardButton(text='Подписался! 🎉👍', callback_data='subchanneldone')

    kb.add(sub_chan, check_chan)

    return kb


# Кнопка для оплаты
def sub_inline():
    kb = InlineKeyboardMarkup(row_width=2)
    pay_sub = InlineKeyboardButton(text='Оплатить 💳💰', callback_data='paysub')

    kb.insert(pay_sub)

    return kb

# Кнопка для оплаты
def pay_inline():
    kb = InlineKeyboardMarkup(row_width=2)
    pay_sub = InlineKeyboardButton(text='Оплатить 💳💰', url='https://www.youtube.com/channel/UCY9jGnDyqNCUUktm2ry-SFw')

    kb.insert(pay_sub)

    return kb

# Кнопка для продолжения первого дня
def info_course():
    kb = InlineKeyboardMarkup(row_width=2)
    next_ = InlineKeyboardButton(text='Продолжить ➡️', callback_data='next')

    kb.add(next_)

    return kb


# Кнопка для получения видео с Ютуба
def get_youtube():
    kb = InlineKeyboardMarkup(row_width=1)
    cont = InlineKeyboardButton(text='Перейти в YouTube 🎥👉',
                                url='https://www.youtube.com/channel/UCY9jGnDyqNCUUktm2ry-SFw')

    kb.add(cont)

    return kb


# Кнопка для получения аудио
def send_audio():
    kb = InlineKeyboardMarkup(row_width=1)
    audio = InlineKeyboardButton(text='Хочу аудио 🎧🎶', callback_data='send_audio')

    kb.add(audio)

    return kb


# Кнопка для отправки задание второго дня
def send_task():
    kb = InlineKeyboardMarkup(row_width=1)
    task = InlineKeyboardButton(text='Узнать задание дня 📝🤔', callback_data='send_task1')

    kb.add(task)

    return kb


# Кнопка для начинания второго дня
def day_two_yes():
    kb = InlineKeyboardMarkup(row_width=1)
    two = InlineKeyboardButton(text='Да хочу!!! 🙌😄', callback_data='day_two_yes')

    kb.add(two)

    return kb


# Кнопка для перехода третьего дня
def day_three_yes():
    kb = InlineKeyboardMarkup(row_width=1)
    three = InlineKeyboardButton(text='Перейти на третий день!!! 🚀🎉', callback_data='day_three_yes')

    kb.add(three)

    return kb


# Кнопка для перехода четвертого дня
def day_four_yes():
    kb = InlineKeyboardMarkup(row_width=1)
    three = InlineKeyboardButton(text='Перейти на четвертый день!!! 🚀📚', callback_data='day_four_yes')

    kb.add(three)

    return kb


def day_five_yes():
    kb = InlineKeyboardMarkup(row_width=1)
    three = InlineKeyboardButton(text='Перейти на пятый день!!! 🚀🎓', callback_data='day_five_yes')

    kb.add(three)

    return kb


# Кнопка для получения видео третья дня
def day_three_video():
    kb = InlineKeyboardMarkup(row_width=1)
    three = InlineKeyboardButton(text='Перейти в YouTube! 🎥👉',
                                 url='https://www.youtube.com/channel/UCY9jGnDyqNCUUktm2ry-SFw')

    kb.add(three)

    return kb


def day_five_video():
    kb = InlineKeyboardMarkup(row_width=1)
    five = InlineKeyboardButton(text='Перейти в YouTube! 🎥👉',
                                url='https://www.youtube.com/channel/UCY9jGnDyqNCUUktm2ry-SFw')

    kb.add(five)

    return kb


def day_three_ok():
    kb = InlineKeyboardMarkup(row_width=1)
    yes = InlineKeyboardButton(text='Готова!✨🎉', callback_data='yes')
    no = InlineKeyboardButton(text='Неготова... 😔🕳️', callback_data='No')

    kb.add(yes, no)

    return kb


def get_task_three():
    kb = InlineKeyboardMarkup(row_width=1)
    task = InlineKeyboardButton(text='Узнать задание дня 📝🤔', callback_data='send_task3')

    kb.add(task)

    return kb


def get_task_four():
    kb = InlineKeyboardMarkup(row_width=1)
    task = InlineKeyboardButton(text='Получить текст аудио 🔊📜', callback_data='send_task4')

    kb.add(task)

    return kb


def emotions_day_two():
    kb = InlineKeyboardMarkup(row_width=1)
    emotions = InlineKeyboardButton(text='💕💕💕', callback_data='emotions_day_two')
    emotions1 = InlineKeyboardButton(text='🔥🔥🔥', callback_data='emotions_day_two1')

    kb.add(emotions, emotions1)

    return kb


# Третий день
def emotions_day_three():
    kb = InlineKeyboardMarkup(row_width=1)
    emotions = InlineKeyboardButton(text='💕💕💕', callback_data='emotions_day_three')
    emotions1 = InlineKeyboardButton(text='🔥🔥🔥', callback_data='emotions_day_three1')

    kb.add(emotions, emotions1)

    return kb


# Четвертый день
def emotions_day_four():
    kb = InlineKeyboardMarkup(row_width=1)
    emotions = InlineKeyboardButton(text='💕💕💕', callback_data='emotions_day_four')
    emotions1 = InlineKeyboardButton(text='🔥🔥🔥', callback_data='emotions_day_four1')

    kb.add(emotions, emotions1)

    return kb


# Пятый день
def emotions_day_five():
    kb = InlineKeyboardMarkup(row_width=1)
    emotions = InlineKeyboardButton(text='💕💕💕', callback_data='emotions_day_five')
    emotions1 = InlineKeyboardButton(text='🔥🔥🔥', callback_data='emotions_day_five1')

    kb.add(emotions, emotions1)

    return kb
