from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
import inline_buttons
from List_of_courses.list_course import *
from config import CHANNEL_ID
import types
import config
from settings import *
import asyncio

from states import Uz_Settings

bot = Bot(config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

NOTSUB_MESSAGE = 'Для доступа к функционалу бота, подпишетесь на канал'


def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    user_id = message.from_user.id
    checker = database.check_user(user_id)

    if checker:
        await message.answer('Приветствуем вас \n\nВыберите раздел🔽',
                             reply_markup=btns.trial_time_kb())

    else:

        channel_id = CHANNEL_ID
        chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        if check_sub_channel(chat_member):
            await message.answer(
                "Добро пожаловать. Пожалуйста пройдите регистрацию\n\nОтправьте имя!",
                reply_markup=btns.ReplyKeyboardMarkup())
            await UserRegistration.getting_name_state.set()

        else:
            await message.answer(
                "Привет! Пожалуйста, подпишитесь на наш канал, чтобы продолжить регистрацию.",
                reply_markup=inline_buttons.sub_channel())

@dp.message_handler(state=UserRegistration.getting_name_state)
async def get_name(message, state=UserRegistration.getting_name_state):
    user_answer = message.text

    await state.update_data(name=user_answer)
    await message.answer("Имя сохранил!\n\nОтправьте номер телефона!",
                         reply_markup=btns.phone_number_kb())

    await UserRegistration.getting_phone_number.set()


@dp.message_handler(state=UserRegistration.getting_phone_number, content_types=['text', 'contact'])
async def get_number(message: types.Message, state: FSMContext):
    user_answer = message.text

    if message.content_type == 'text':
        user_answer = message.text

        if not user_answer.replace('+', '').isdigit():
            await message.answer('Отправьте номер телефона')
            return

    elif message.content_type == 'contact':
        user_answer = message.contact.phone_number

    await state.update_data(number=user_answer)
    await message.answer("Номер сохранил! Вы прошли регистрацию\n\nВыберите раздел.",
                         reply_markup=btns.main_menu_kb())


    all_info = await state.get_data()
    user_id = message.from_user.id
    name = all_info.get("name")
    phone_number = all_info.get("number")
    times = all_info.get("time_sub")
    end_subb = all_info.get("end_sub")
    gender = user_answer
    user_status = all_info.get("status")
    price = all_info.get("amount_sub")


    database.add_user(user_id, name, phone_number, times, end_subb, gender, user_status, price)


    admin_user_id = 5928000362
    notification_message = (
        f"Новый пользователь зарегистрирован:\n"
        f"Имя: {name}\n"
        f"Номер телефона: {phone_number}\n")

    await bot.send_message(admin_user_id, notification_message, parse_mode=ParseMode.MARKDOWN)

    await state.finish()

@dp.callback_query_handler(text='subchanneldone')
async def sub_channel_done(call: types.CallbackQuery):

    await bot.delete_message(call.from_user.id, call.message.message_id)

    user_id = call.from_user.id
    checker = database.check_user(user_id)

    channel_id = CHANNEL_ID
    if check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=user_id)):

        if checker:
            await bot.send_message(user_id, 'Привет', reply_markup=btns.trial_time_kb())

        else:
            await bot.send_message(
                user_id,
                "Привет! Пожалуйста, пройдите регистрацию, отправив ваше имя.",
                reply_markup=btns.ReplyKeyboardMarkup())
            await UserRegistration.getting_name_state.set()

    else:
        await bot.send_message(
            user_id,
            "Привет! Пожалуйста, подпишитесь на наш канал, чтобы продолжить регистрацию.",
            reply_markup=inline_buttons.sub_channel())


@dp.message_handler(state=Settings.set_name)
async def change_name_db(message, state=Settings.set_name):
    user_answer = message.text

    await state.update_data(name=user_answer)

    ch_name = await state.get_data()
    user_id = message.from_user.id
    database.change_name(user_id, ch_name)
    await state.finish()
    await message.answer("Имя Успешно изменено",
                         reply_markup=btns.settings_kb())


@dp.message_handler(state=Settings.set_number)
async def change_number_db(message, state=Settings.set_number):
    user_answer = message.text

    await state.update_data(phone_number=user_answer)

    ch_number = await state.get_data()
    user_id = message.from_user.id
    database.change_number(user_id, ch_number)
    await state.finish()
    await message.answer("Номер успешно изменен",
                         reply_markup=btns.settings_kb())

@dp.message_handler(state=Settings.set_setting, content_types=["text"])
async def set_name(message):
    user_answer = message.text
    user_id = message.from_user.id

    if user_answer == 'Изменит имя':
        await message.answer("Отправьте имя!")
        await Settings.set_name.set()

    elif user_answer == 'Изменит номер':
        await message.answer("Отправьте номер телефона")
        await Settings.set_number.set()

    elif user_answer == 'Hазад':
        await message.answer("Вы вернулись в раздел НАСТРОЙКИ",
                             reply_markup=btns.settings_kb())
        await dp.current_state(user=user_id).finish()


# Обработчик основного меню
@dp.message_handler(content_types=["text"])
async def main_menu(message):
    user_id = message.from_user.id
    user_answer = message.text

    if message.text == 'Русский':

        status = 1
        database.set_status(user_id, status)

        start = datetime.now()
        end = start + timedelta(days=7)
        dpp = end.strftime("%d/%m/%y, %H:%M:%S")
        database.set_trial_sub(user_id, start, end)

        await message.answer(f"Бесплатный курс \nДействует до: \n\n{dpp}",
                             reply_markup=btns.main_menu_kb(), parse_mode="HTML")
        return


    photo_path = 'List_of_courses/course_photo.png'

    if user_answer == "📝Оплата за курс":
        await message.answer("Чтобы оплатить за курс нажмите кнопку 'Оплатить 💳💰'",
                             reply_markup=course.pay_inline())

    elif user_answer == "📚КУРСЫ":
        await message.answer("Выберите одного из курсов",
                             reply_markup=course.list_courses())

    elif user_answer == "⚙️НАСТРОЙКА":
        await message.answer("Вы в разделе '⚙️НАСТРОЙКА'",
                             reply_markup=btns.settings_kb())

    elif user_answer == "👤ПОЛЬЗОВАТЕЛЬ":
        await message.answer("Выберите кнопку",
                             reply_markup=btns.change_data_kb())
        await states.Settings.set_setting.set()

    elif user_answer == 'Курс "Новая Я" 🌟🎓':
        await bot.send_photo(photo=open(photo_path, 'rb'), chat_id=user_id, caption=welcome_msg, reply_markup=course.some_kb())




    elif user_answer == "НАЗАД":
        await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
                             reply_markup=btns.main_menu_kb())
        await dp.current_state(user=user_id).finish()

    elif user_answer == "Haзад":
        await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
                             reply_markup=btns.main_menu_kb())
        await dp.current_state(user=user_id).finish()

    elif user_answer == "Haзaд":
        await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
                             reply_markup=btns.main_menu_kb())
        await dp.current_state(user=user_id).finish()

    elif user_answer == "Назад":
        await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
                             reply_markup=btns.main_menu_kb())
        await dp.current_state(user=user_id).finish()



# Узб поток
# -----------------------------------------------------------------------------------------


    if user_answer == "O'zbek":


        status = 11
        database.set_status(user_id, status)

        start = datetime.now()
        end = start + timedelta(days=7)
        dpp = end.strftime("%d/%m/%y, %H:%M:%S")
        database.set_trial_sub(user_id, start, end)

        await message.answer(f"Bepul kursning \nAmal qilish muddati: \n\n{dpp} gacha",
                             reply_markup=uzbtns.uz_main_menu_kb(), parse_mode="HTML")
        return

    photo_path = 'List_of_courses/course_photo.png'

    if user_answer == "📝Kurs uchun to'lov":
        await message.answer("Kurs uchun to'lovni amalga oshirish uchun 'To'lov 💳💰 tugmasini bosing'",
                             reply_markup=uzcourse.uz_pay_inline())

    elif user_answer == "📚Kurslar":
        await message.answer("Kursni tanlang!",
                             reply_markup=uzcourse.uz_list_courses())

    elif user_answer == "⚙️Sozlamalar":
        await message.answer("Siz '⚙️Sozlamalar' bo'limidasiz",
                             reply_markup=uzbtns.uz_settings_kb())

    elif user_answer == "👤Profil":
        await message.answer("Bo'limni tanlang",
                             reply_markup=uzbtns.uz_change_data_kb())
        await states.Settings.set_setting.set()

    elif user_answer == '"Yangi Men" kursi 🌟🎓':
        await bot.send_photo(photo=open(photo_path, 'rb'), chat_id=user_id, caption=welcome_msg_uz,
                             reply_markup=uzcourse.uz_some_kb())


    elif user_answer == "Ortga qaytishh":
        await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
                             reply_markup=uzbtns.uz_main_menu_kb())
        await dp.current_state(user=user_id).finish()

    elif user_answer == "Ortgа qaytish":
        await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
                             reply_markup=uzbtns.uz_main_menu_kb())
        await dp.current_state(user=user_id).finish()

    elif user_answer == "Ortga qаytish":
        await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
                             reply_markup=uzbtns.uz_main_menu_kb())
        await dp.current_state(user=user_id).finish()

    elif user_answer == "Ortga qaytish":
        await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
                             reply_markup=uzbtns.uz_main_menu_kb())
        await dp.current_state(user=user_id).finish()



# Обработчик курса "Новая Я"
@dp.callback_query_handler(lambda query: True)
async def course_fivedays(call: types.CallbackQuery):
    user_id = call.from_user.id

    # Первый день
    if call.data == "start":

        # status = 1
        # database.set_status(user_id, status)

        # Отправляем действие "печатание" перед отправкой изображения и приветственного сообщения
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await bot.answer_callback_query(call.id)

        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(0.5)
        await bot.send_message(call.from_user.id, text, reply_markup=btns.ReplyKeyboardRemove())

        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, text2,
                               reply_markup=course.info_course())


    # При нажатии кнопку Продолжить
    elif call.data == "next":

        # await bot.delete_message(call.message.chat.id, call.message.message_id)
        current_status = database.get_status(user_id)

        if current_status == 1:

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)

            await bot.send_message(call.from_user.id, "Чтобы открыть видео 1-го дня. Нажми кнопку ниже. 👇\n\n",
                                   reply_markup=course.get_youtube())

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, day_one)

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, emotions_text,
                                   reply_markup=inline_buttons.emotions_day_two())

        else:
            await bot.send_message(call.from_user.id, "Курс еще не закончен. Хотите продолжить просмотр? 📚💡",
                                   reply_markup=course.day_two_yes())


    # Переход на Второй день
    if call.data == 'emotions_day_two' or call.data == 'emotions_day_two1' or call.data == 'day_two_yes':

        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id, 'Вы перешли на Второй день курса. 🌟\nСкором времени будет отправлено новое сообщение! 🚀')
        await bot.delete_message(call.message.chat.id, call.message.message_id)

        # Ожидание 24 часа
        await asyncio.sleep(86400)
        database.update_status(user_id)

        await asyncio.sleep(2)
        current_status = database.get_status(user_id)

        if current_status == 2:

            await asyncio.sleep(5)

            await bot.send_message(call.from_user.id, day_two_notif, reply_markup=inline_buttons.send_audio())

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(2)


    elif call.data == 'send_audio':
        current_status = database.get_status(user_id)

        if current_status == 2:
            audio_path = 'List_of_courses/1.ogg'
            audio_path2 = 'List_of_courses/2.ogg'

            if os.path.exists(audio_path) and os.path.exists(audio_path2):
                with open(audio_path, 'rb') as audio_file:
                    await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.UPLOAD_AUDIO)
                    await bot.send_audio(call.from_user.id,
                                         audio_file,
                                         caption='Ознакомления')
            await bot.answer_callback_query(call.id)
            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, 'Чтобы открыть аудио 2-го дня. Нажми кнопку ниже. 👇',
                                   reply_markup=inline_buttons.send_task())

    # Задание второго дня
    elif call.data == 'send_task1':

        audio_path2 = 'List_of_courses/2.ogg'

        if os.path.exists(audio_path2) and os.path.exists(audio_path2):

            with open(audio_path2, 'rb') as audio_file4:

                await bot.answer_callback_query(call.id)
                await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.UPLOAD_AUDIO)
                await asyncio.sleep(3)
                await bot.send_audio(call.from_user.id, audio_file4, caption='Задание')
                await asyncio.sleep(3)
                await bot.send_message(call.from_user.id, emotions_text,
                                       reply_markup=inline_buttons.emotions_day_three())

        else:
            await bot.send_message(call.from_user.id, 'Курс еще не закончен. Пожалуйста, заверши предыдущие дни. 🔒📚')
            await asyncio.sleep(0.5)
            await bot.send_message(call.from_user.id, 'Курс еще не закончен! 💫 Если ты прошел предыдущие 2 дня, нажми на кнопку 👉🎯',
                                   reply_markup=inline_buttons.day_three_yes())


    # Переход на Третий день
    if (call.data == 'emotions_day_three' or
            call.data == 'emotions_day_three1' or call.data == 'day_three_yes'):

        await bot.send_message(call.from_user.id, 'Вы перешли на Третий день курса. 🎉📚\nСкором времени вам будет отправлено новое сообщение! 🚀')
        await bot.delete_message(call.message.chat.id, call.message.message_id)

        # Ожидание 24 часа
        await asyncio.sleep(86400)
        database.update_status(user_id)

        await asyncio.sleep(2)
        current_status = database.get_status(user_id)

        if current_status == 3:

            await asyncio.sleep(5)
            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await bot.send_message(call.from_user.id, day_three_notif)

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.UPLOAD_VIDEO)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, 'Чтобы получить видео, жми на кнопку 🎥👇',
                                   reply_markup=inline_buttons.day_three_video())
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, day_three_message,
                                   reply_markup=inline_buttons.day_three_ok())

        else:
            await bot.send_message(call.from_user.id, 'Курс еще не закончен. Пожалуйста, заверши предыдущие дни. 📚🔒')
            await asyncio.sleep(0.5)
            await bot.send_message(call.from_user.id, 'Курс еще не закончен. Если ты прошел предыдущие 3 дня, Нажми на кнопку 👉🎓',
                                   reply_markup=inline_buttons.day_four_yes())

    # ---Если нажал "Готова"---
    elif call.data == 'yes':

        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, day_three_yes_message)
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, 'Теперь задание от Психолога. 💡💭\n\nЧтобы получить задание, жми на кнопку 👉📝',
                               reply_markup=inline_buttons.get_task_three())

    # ---Отправка задание к третьему дню---
    elif call.data == 'send_task3':
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, day_three_task)
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, emotions_text,
                               reply_markup=inline_buttons.emotions_day_four())


    elif call.data == 'emotions_day_four' or call.data == 'emotions_day_four1' or call.data == 'day_four_yes':


        await bot.delete_message(call.message.chat.id, call.message.message_id)

        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(2)
        await bot.send_message(call.from_user.id, 'Вы успешно прошли третий день курса!!! 🎉🎓✨')

        # Ожидание 24 часа
        await asyncio.sleep(86400)
        database.update_status(user_id)

        await asyncio.sleep(2)
        current_status = database.get_status(user_id)

        if current_status == 4:

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, day_four_notif)

            audio_path2 = 'List_of_courses/day_four.ogg'

            if os.path.exists(audio_path2) and os.path.exists(audio_path2):
                with open(audio_path2, 'rb') as audio_file4:

                    await asyncio.sleep(0.5)

                    await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.UPLOAD_AUDIO)
                    await bot.send_audio(call.from_user.id, audio_file4,
                                         reply_markup=inline_buttons.get_task_four())

            else:
                await bot.send_message(call.from_user.id,
                                       'Курс еще не закончен. Если ты прошел предыдущие 3 дня, Нажми на кнопку 👉',
                                       reply_markup=inline_buttons.day_five_yes())


    elif call.data == 'send_task4':

        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, day_four_task)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, emotions_text,
                               reply_markup=inline_buttons.emotions_day_five())

    # ---Пятый день---
    elif call.data == 'emotions_day_five' or call.data == 'emotions_day_five1' or call.data == 'day_five_yes':

        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(call.from_user.id,
                               'Вы перешли на Пятый день курса. 🌟📚\nСкоро вам будет отправлено новое сообщение! 🚀')
        # Ожидание 24 часа
        await asyncio.sleep(86400)
        database.update_status(user_id)

        await asyncio.sleep(2)
        current_status = database.get_status(user_id)

        if current_status == 5:

            await asyncio.sleep(3)
            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await bot.send_message(call.from_user.id, day_five_notif)

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.UPLOAD_VIDEO)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, 'Чтобы получить видео, жми на кнопку 🎥👇',
                                   reply_markup=inline_buttons.day_five_video())

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, day_five_text)
            await asyncio.sleep(5)
            await bot.send_message(call.from_user.id, discount_text)

        else:
            await bot.send_message(call.from_user.id, 'Курс еще не закончен. Пожалуйста, заверши предыдущие дни. 📚🔒')
            await asyncio.sleep(0.5)
            await bot.send_message(call.from_user.id,
                                   'Курс еще не закончен. Если ты прошел предыдущие 4 дня, Нажми на кнопку 👉🏅',
                                   reply_markup=inline_buttons.day_five_yes())

# ---Если нажал "Не готова"---
    elif call.data == 'no':
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, day_three_no_message)
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, 'Сообщения от бота со скидкой на курс')




# ------------------------------------------------------------------------------------------
# Узбек поток
    if call.data == "uz_start":

        # status = 10
        # database.set_status(user_id, status)

        # Отправляем действие "печатание" перед отправкой изображения и приветственного сообщения
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await bot.answer_callback_query(call.id)

        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(0.5)
        await bot.send_message(call.from_user.id, text_uz, reply_markup=btns.ReplyKeyboardRemove())

        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, text2_uz,
                               reply_markup=uzcourse.uz_info_course())


    # При нажатии кнопку Продолжить
    elif call.data == "uz_next":

        # await bot.delete_message(call.message.chat.id, call.message.message_id)
        current_status = database.get_status(user_id)

        if current_status == 11:

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)

            await bot.send_message(call.from_user.id, "1-kun videosini ochish uchun. Quyidagi tugmani bosing. 👇\n\n",
                                   reply_markup=uzcourse.uz_get_youtube())

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, day_one_uz)

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, emotions_text_uz,
                                   reply_markup=uz_inline_buttons.uz_emotions_day_two())

        else:
            await bot.send_message(call.from_user.id, "Kurs hali tugamagan. Kursni davom ettirmoqchimisiz? 📚💡",
                                   reply_markup=uzcourse.uz_day_two_yes())

    # Переход на Второй день
    if call.data == 'uz_emotions_day_two' or call.data == 'uz_emotions_day_two1' or call.data == 'uz_day_two_yes':

        await bot.answer_callback_query(call.id)
        await bot.send_message(call.from_user.id,
                               "Siz kursning ikkinchi kuniga o'tdingiz. 🌟\nSizga tez orada yangi xabar yuboriladi! 🚀")
        await bot.delete_message(call.message.chat.id, call.message.message_id)

        # Ожидание 24 часа
        await asyncio.sleep(86400)
        database.update_status(user_id)

        await asyncio.sleep(2)
        current_status = database.get_status(user_id)

        if current_status == 2:
            await asyncio.sleep(5)

            await bot.send_message(call.from_user.id, day_two_notif_uz, reply_markup=uzcourse.uz_send_audio())

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(2)


    elif call.data == 'uz_send_audio':
        current_status = database.get_status(user_id)

        if current_status == 12:
            audio_path = 'List_of_courses/1.ogg'
            audio_path2 = 'List_of_courses/2.ogg'

            if os.path.exists(audio_path) and os.path.exists(audio_path2):
                with open(audio_path, 'rb') as audio_file:
                    await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.UPLOAD_AUDIO)
                    await bot.send_audio(call.from_user.id,
                                         audio_file,
                                         caption="Kunnig temasi bo'yicha audio")
            await bot.answer_callback_query(call.id)
            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, 'Ikkinchi kunning audiosini ochish uchun. Tugmani bosing. 👇',
                                   reply_markup=uz_inline_buttons.uz_send_task())

    # Задание второго дня
    elif call.data == 'uz_send_task1':

        audio_path2 = 'List_of_courses/2.ogg'

        if os.path.exists(audio_path2) and os.path.exists(audio_path2):

            with open(audio_path2, 'rb') as audio_file4:

                await bot.answer_callback_query(call.id)
                await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.UPLOAD_AUDIO)
                await asyncio.sleep(3)
                await bot.send_audio(call.from_user.id, audio_file4,
                                     caption='Kunning vazifasi')
                await asyncio.sleep(3)
                await bot.send_message(call.from_user.id, emotions_text_uz,
                                       reply_markup=uz_inline_buttons.uz_emotions_day_three())

        else:
            await bot.send_message(call.from_user.id, "Kurs hali tugamagan. Iltimos, oldingi kunlarni yakunlang. 🔒📚")
            await asyncio.sleep(0.5)
            await bot.send_message(call.from_user.id,
                                   "Kurs hali tugamagan. Agar siz oldingi kunni tugatgan bo'lsangiz, tugmani bosing 👉🎯",
                                   reply_markup=uz_inline_buttons.uz_day_three_yes())

    # Переход на Третий день
    if (call.data == 'uz_emotions_day_three' or
            call.data == 'uz_emotions_day_three1' or call.data == 'uz_day_three_yes'):

        await bot.send_message(call.from_user.id,
                               "Siz kursning uchinchi kuniga o'tdingiz. 🎉📚\nSizga tez orada yangi xabar yuboriladi! 🚀")
        await bot.delete_message(call.message.chat.id, call.message.message_id)

        # Ожидание 24 часа
        await asyncio.sleep(86400)
        database.update_status(user_id)

        await asyncio.sleep(2)
        current_status = database.get_status(user_id)

        if current_status == 13:

            await asyncio.sleep(5)
            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await bot.send_message(call.from_user.id, day_three_notif_uz)

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.UPLOAD_VIDEO)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, "Videoga o'tish uchun, tugmani bosing 🎥👇",
                                   reply_markup=uz_inline_buttons.uz_day_three_video())
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, day_three_message_uz,
                                   reply_markup=uz_inline_buttons.uz_day_three_ok())

        else:
            await bot.send_message(call.from_user.id, "Kurs hali tugamagan. Iltimos, oldingi kunlarni yakunlang. 📚🔒")
            await asyncio.sleep(0.5)
            await bot.send_message(call.from_user.id,
                                   "Kurs hali tugamagan. Agar siz oldingi 2 kunni tugatgan bo'lsangiz, tugmani bosing 👉🎓",
                                   reply_markup=uz_inline_buttons.uz_day_four_yes())

    # ---Если нажал "Готова"---
    elif call.data == 'uz_yes':

        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, day_three_yes_message_uz)
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id,
                               'Endi Psixologdan vazifa. 💡💭\n\nVazifani ochish uchun, tugmani bosing 👉📝',
                               reply_markup=uz_inline_buttons.uz_get_task_three())


    # ---Отправка задание к третьему дню---
    elif call.data == 'uz_send_task3':
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, day_three_task_uz)
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, emotions_text_uz,
                               reply_markup=uz_inline_buttons.uz_emotions_day_four())


    elif call.data == 'uz_emotions_day_four' or call.data == 'uz_emotions_day_four1' or call.data == 'uz_day_four_yes':

        await bot.delete_message(call.message.chat.id, call.message.message_id)

        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(2)
        await bot.send_message(call.from_user.id, "Siz kursning to'rtinchi kuniga o'tdingiz!!!\nTez orada sizga habar yuboriladi! 🚀 🎓")

        # Ожидание 24 часа
        await asyncio.sleep(86400)
        database.update_status(user_id)

        await asyncio.sleep(2)
        current_status = database.get_status(user_id)

        if current_status == 14:

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, day_four_notif_uz)

            audio_path2 = 'List_of_courses/day_four.ogg'

            if os.path.exists(audio_path2) and os.path.exists(audio_path2):
                with open(audio_path2, 'rb') as audio_file4:

                    await asyncio.sleep(0.5)

                    await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.UPLOAD_AUDIO)
                    await bot.send_audio(call.from_user.id, audio_file4,
                                         reply_markup=uz_inline_buttons.uz_get_task_four())

            else:
                await bot.send_message(call.from_user.id,
                                       "Kurs hali tugamagan. Agar siz oldingi 3 kunni tugatgan bo'lsangiz, tugmani bosing 👉",
                                       reply_markup=uz_inline_buttons.uz_day_five_yes())


    elif call.data == 'uz_send_task4':

        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, day_four_task_uz)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, emotions_text_uz,
                               reply_markup=uz_inline_buttons.uz_emotions_day_five())

    # ---Пятый день---
    elif call.data == 'uz_emotions_day_five' or call.data == 'uz_emotions_day_five1' or call.data == 'uz_day_five_yes':

        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(call.from_user.id,
                               "Siz kursning beshinchi kuniga o'tdingiz. 🌟📚\nTez orada sizga habar yuboriladi! 🚀")
        # Ожидание 24 часа
        await asyncio.sleep(86400)
        database.update_status(user_id)

        await asyncio.sleep(2)
        current_status = database.get_status(user_id)

        if current_status == 15:

            await asyncio.sleep(3)
            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await bot.send_message(call.from_user.id, day_five_notif_uz)

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.UPLOAD_VIDEO)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, "Videoni ko'rish uchun tugmani bosing 🎥👇",
                                   reply_markup=uz_inline_buttons.uz_day_five_video())

            await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
            await asyncio.sleep(3)
            await bot.send_message(call.from_user.id, day_five_text_uz)
            await asyncio.sleep(5)
            await bot.send_message(call.from_user.id, discount_text_uz)

        else:
            await bot.send_message(call.from_user.id, 'Kurs hali tugamagan. Iltimos, oldingi kunlarni yakunlang. 📚🔒')
            await asyncio.sleep(0.5)
            await bot.send_message(call.from_user.id,
                                   "Kurs hali tugamagan. Agar siz oldingi 4 kunni tugatgan bo'lsangiz, tugmani bosing 👉🏅",
                                   reply_markup=uz_inline_buttons.uz_day_five_yes())

    # ---Если нажал "Не готова"---
    elif call.data == 'uz_no':
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, day_three_no_message_uz)
        await bot.send_chat_action(chat_id=user_id, action=types.ChatActions.TYPING)
        await asyncio.sleep(3)
        await bot.send_message(call.from_user.id, discount_text_uz)


# ----------------------------------------------------------------------
    # Узб поток
@dp.message_handler(state=Uz_Settings.uz_set_name)
async def change_name_db(message, state=Uz_Settings.uz_set_name):
    user_answer = message.text

    await state.update_data(name=user_answer)

    ch_name = await state.get_data()
    user_id = message.from_user.id
    database.change_name(user_id, ch_name)
    await state.finish()
    await message.answer("Ism muvaffaqiyatli o'zgartirildi",
                         reply_markup=uzbtns.uz_settings_kb())


@dp.message_handler(state=Uz_Settings.uz_set_number)
async def change_number_db(message, state=Uz_Settings.uz_set_number):
    user_answer = message.text

    await state.update_data(phone_number=user_answer)

    ch_number = await state.get_data()
    user_id = message.from_user.id
    database.change_number(user_id, ch_number)
    await state.finish()
    await message.answer("Raqam muvaffaqiyatli o'zgartirildi",
                         reply_markup=uzbtns.uz_settings_kb())

@dp.message_handler(state=Uz_Settings.uz_set_setting, content_types=["text"])
async def set_name(message):
    user_answer = message.text
    user_id = message.from_user.id

    if user_answer == "Ismni o'zgratirish":
        await message.answer("Ism yuboring")
        await Uz_Settings.uz_set_name.set()

    elif user_answer == "Raqamni o'zgratirish":
        await message.answer("Telefon raqam yuboring")
        await Uz_Settings.uz_set_number.set()

    elif user_answer == 'Ortgа qaytish':
        await message.answer("Вы вернулись в раздел НАСТРОЙКИ",
                             reply_markup=uzbtns.uz_settings_kb())
        await dp.current_state(user=user_id).finish()





#https://www.youtube.com/channel/UCY9jGnDyqNCUUktm2ry-SFw

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
