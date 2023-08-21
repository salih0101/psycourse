from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# Список курсов
def uz_list_courses():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    course2 = KeyboardButton('"Yangi Men" kursi 🌟🎓')
    back = KeyboardButton('Ortga qaytish')
    kb.add(course2, back)

    return kb


# Чтобы начать курс
def uz_some_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    some1 = InlineKeyboardMarkup(text='Kursni boshlash! 🚀📚', callback_data='uz_start')

    kb.add(some1)

    return kb


def uz_sub_channel():
    kb = InlineKeyboardMarkup(row_width=1)
    sub_chan = InlineKeyboardButton(text="Kanalga obuna bo'lish 👍🔔", url='https://t.me/psychofemme')
    check_chan = InlineKeyboardButton(text="Obuna bo'ldim 🎉👍", callback_data='uz_subchanneldone')

    kb.add(sub_chan, check_chan)

    return kb


# Кнопка для оплаты
def uz_sub_inline():
    kb = InlineKeyboardMarkup(row_width=2)
    pay_sub = InlineKeyboardButton(text="To'lov 💳💰", callback_data='uz_paysub')

    kb.insert(pay_sub)

    return kb

# Кнопка для оплаты
def uz_pay_inline():
    kb = InlineKeyboardMarkup(row_width=2)
    pay_sub = InlineKeyboardButton(text="To'lov 💳💰", url='https://www.youtube.com/channel/UCY9jGnDyqNCUUktm2ry-SFw')

    kb.insert(pay_sub)

    return kb

# Кнопка для продолжения первого дня
def uz_info_course():
    kb = InlineKeyboardMarkup(row_width=2)
    next_ = InlineKeyboardButton(text='Davom etish ➡️', callback_data='uz_next')

    kb.add(next_)

    return kb


# Кнопка для получения видео с Ютуба
def uz_get_youtube():
    kb = InlineKeyboardMarkup(row_width=1)
    cont = InlineKeyboardButton(text="YouTube ga o'tish 🎥👉",
                                url='https://youtu.be/qranD_Dx8aM')

    kb.add(cont)

    return kb


# Кнопка для получения аудио
def uz_send_audio():
    kb = InlineKeyboardMarkup(row_width=1)
    audio = InlineKeyboardButton(text='Audioni yuklash 🎧🎶', callback_data='uz_send_audio')

    kb.add(audio)

    return kb


# Кнопка для отправки задание второго дня
def uz_send_task():
    kb = InlineKeyboardMarkup(row_width=1)
    task = InlineKeyboardButton(text='Kunning vazifasini bilish 📝🤔', callback_data='uz_send_task1')

    kb.add(task)

    return kb


# Кнопка для начинания второго дня
def uz_day_two_yes():
    kb = InlineKeyboardMarkup(row_width=1)
    two = InlineKeyboardButton(text='Xa xohlayman!!! 🙌😄', callback_data='uz_day_two_yes')

    kb.add(two)

    return kb


# Кнопка для перехода третьего дня
def uz_day_three_yes():
    kb = InlineKeyboardMarkup(row_width=1)
    three = InlineKeyboardButton(text="Uchinchi kunga o'tish!!! 🚀🎉", callback_data='uz_day_three_yes')

    kb.add(three)

    return kb


# Кнопка для перехода четвертого дня
def uz_day_four_yes():
    kb = InlineKeyboardMarkup(row_width=1)
    three = InlineKeyboardButton(text="To'rtinchi kunga o'tish!!! 🚀📚", callback_data='uz_day_four_yes')

    kb.add(three)

    return kb


def uz_day_five_yes():
    kb = InlineKeyboardMarkup(row_width=1)
    three = InlineKeyboardButton(text="Beshinchi kunga o'tish!! 🚀🎓", callback_data='uz_day_five_yes')

    kb.add(three)

    return kb


# Кнопка для получения видео третья дня
def uz_day_three_video():
    kb = InlineKeyboardMarkup(row_width=1)
    three = InlineKeyboardButton(text="YouTube ga o'tish 🎥👉",
                                 url='https://youtu.be/ZGqZs_VX_rk')

    kb.add(three)

    return kb


def uz_day_five_video():
    kb = InlineKeyboardMarkup(row_width=1)
    five = InlineKeyboardButton(text="YouTube ga o'tish 🎥👉",
                                url='https://youtu.be/PWzTlZXTuLI')

    kb.add(five)

    return kb


def uz_day_three_ok():
    kb = InlineKeyboardMarkup(row_width=1)
    yes = InlineKeyboardButton(text='Tayyorman!✨🎉', callback_data='uz_yes')
    no = InlineKeyboardButton(text='Tayyor emasman... 😔🕳️', callback_data='uz_No')

    kb.add(yes, no)

    return kb


def uz_get_task_three():
    kb = InlineKeyboardMarkup(row_width=1)
    task = InlineKeyboardButton(text='Kunning vazifasini bilish 📝🤔', callback_data='uz_send_task3')

    kb.add(task)

    return kb


def uz_get_task_four():
    kb = InlineKeyboardMarkup(row_width=1)
    task = InlineKeyboardButton(text='Audioning matnini yuklash 🔊📜', callback_data='uz_send_task4')

    kb.add(task)

    return kb


def uz_emotions_day_two():
    kb = InlineKeyboardMarkup(row_width=1)
    emotions = InlineKeyboardButton(text='💕💕💕', callback_data='uz_emotions_day_two')
    emotions1 = InlineKeyboardButton(text='🔥🔥🔥', callback_data='uz_emotions_day_two1')

    kb.add(emotions, emotions1)

    return kb


# Третий день
def uz_emotions_day_three():
    kb = InlineKeyboardMarkup(row_width=1)
    emotions = InlineKeyboardButton(text='💕💕💕', callback_data='uz_emotions_day_three')
    emotions1 = InlineKeyboardButton(text='🔥🔥🔥', callback_data='uz_emotions_day_three1')

    kb.add(emotions, emotions1)

    return kb


# Четвертый день
def uz_emotions_day_four():
    kb = InlineKeyboardMarkup(row_width=1)
    emotions = InlineKeyboardButton(text='💕💕💕', callback_data='uz_emotions_day_four')
    emotions1 = InlineKeyboardButton(text='🔥🔥🔥', callback_data='uz_emotions_day_four1')

    kb.add(emotions, emotions1)

    return kb


# Пятый день
def uz_emotions_day_five():
    kb = InlineKeyboardMarkup(row_width=1)
    emotions = InlineKeyboardButton(text='💕💕💕', callback_data='uz_emotions_day_five')
    emotions1 = InlineKeyboardButton(text='🔥🔥🔥', callback_data='uz_emotions_day_five1')

    kb.add(emotions, emotions1)

    return kb
