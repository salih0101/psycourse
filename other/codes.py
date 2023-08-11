# import time
# import types
# import config
# from settings import *
# from List_of_courses.list_course import *
#
# bot = Bot(config.TOKEN)
# dp = Dispatcher(bot, storage=MemoryStorage())
# logging.basicConfig(level=logging.INFO)
#
#
# @dp.message_handler(Command("start"))
# async def start_message(message):
#     user_id = message.from_user.id
#     checker = database.check_user(user_id)
#
#     if checker:
#
#         check_pay = database.check_pay(user_id)
#
#         if check_pay:
#             await message.answer("Приветствую. Добро пожаловать",
#                                  reply_markup=btns.check_pay_kb())
#
#         else:
#             await message.answer("Приветствуем вас Новый клиент!!!\n\nВыберите раздел",
#                                  reply_markup=btns.trial_time_kb())
#     else:
#         await message.answer(
#             "Добро пожаловать. Пожалуйста пройдите регистрацию\n\nОтправьте имя!",
#             reply_markup=btns.ReplyKeyboardMarkup())
#         await UserRegistration.getting_name_state.set()
#
#
# @dp.message_handler(state=UserRegistration.getting_name_state)
# async def get_name(message, state=UserRegistration.getting_name_state):
#     user_answer = message.text
#
#     await state.update_data(name=user_answer)
#     await message.answer("Имя сохранил!\n\nОтправьте номер телефона!",
#                          reply_markup=btns.phone_number_kb())
#
#     await UserRegistration.getting_phone_number.set()
#
#
# @dp.message_handler(state=UserRegistration.getting_phone_number, content_types=["contact"])
# async def get_number(message, state=UserRegistration.getting_phone_number):
#     user_answer = message.contact.phone_number
#
#     await state.update_data(number=user_answer)
#     await message.answer("Номер сохранил! Вы прошли регистрацию\n\nВыберите раздел.",
#                          reply_markup=btns.trial_time_kb())
#
#
#     all_info = await state.get_data()
#     user_id = message.from_user.id
#     name = all_info.get("name")
#     phone_number = all_info.get("number")
#     time = all_info.get("time_sub")
#     end_subb = all_info.get("end_sub")
#     gender = user_answer
#     user_status = all_info.get("status")
#     price = all_info.get("amount_sub")
#     database.add_user(user_id, name, phone_number, time, end_subb, gender, user_status, price)
#
#     await state.finish()
#
#
# @dp.message_handler(state=Settings.set_name)
# async def change_name_db(message, state=Settings.set_name):
#     user_answer = message.text
#
#     await state.update_data(name=user_answer)
#
#     ch_name = await state.get_data()
#     user_id = message.from_user.id
#     database.change_name(user_id, ch_name)
#     await state.finish()
#     await message.answer("Имя Успешно изменено",
#                          reply_markup=btns.settings_kb())
#
#
# @dp.message_handler(state=Settings.set_number)
# async def change_number_db(message, state=Settings.set_number):
#     user_answer = message.text
#
#     await state.update_data(phone_number=user_answer)
#
#     ch_number = await state.get_data()
#     user_id = message.from_user.id
#     database.change_number(user_id, ch_number)
#     await state.finish()
#     await message.answer("Номер успешно изменен",
#                          reply_markup=btns.settings_kb())
#
#
# @dp.message_handler(state=Settings.set_setting, content_types=["text"])
# async def set_name(message):
#     user_answer = message.text
#     user_id = message.from_user.id
#     try:
#         match user_answer:
#             case "Изменит имя":
#                 await message.answer("Отправьте имя!")
#                 await Settings.set_name.set()
#
#             case "Изменит номер":
#                 await message.answer("Отправьте номер телефона")
#                 await Settings.set_number.set()
#
#     except Exception as e:
#         print(e)
#         await message.answer("Неверный ввод")
#
#     try:
#         match user_answer:
#             case "Назадв":
#                 await message.answer("Вы вернулись в раздел НАСТРОЙКИ",
#                                      reply_markup=btns.settings_kb())
#                 await dp.current_state(user=user_id).finish()
#
#     except Exception as e:
#         print(e)
#         await message.answer("Неверный ввод")
#
#
# @dp.message_handler(content_types=["text"])
# async def main_menu(message):
#     user_answer = message.text
#     user_id = message.from_user.id
#
#     # Получить дедлайн пользователя
#     if message.text == "Вход в бот":
#
#         start = datetime.now()
#         end = start + timedelta(days=7)
#         dpp = end.strftime("%d/%m/%y, %H:%M:%S")
#         database.set_trial_sub(user_id, start, end)
#
#         await message.answer(f"Пробный период>> \nДействует до: \n\n{dpp}",
#                              reply_markup=btns.main_menu_kb(), parse_mode="HTML")
#         return
#
#     deadline = database.deadline(user_id)
#     check_sub = database.check_sub(user_id)
#     photo_path = 'List_of_courses/course_photo.jpg'
#
#     if datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S.%f") >= datetime.now():
#         try:
#             match message.text:
#
#                 case "📝ОФОРМИТЬ ПОДПИСКУ":
#                     await message.answer("Процесс 'Оформления подписки'",
#                                          reply_markup=course.sub_inline())
#
#                 case "📚КУРСЫ":
#                     # Проверка даты подписки
#                     await message.answer("Выберите одного из курсов",
#                                          reply_markup=course.list_courses())
#
#                 case "⚙️НАСТРОЙКА":
#                     await message.answer("Вы в разделе '⚙️НАСТРОЙКА'",
#                                          reply_markup=btns.settings_kb())
#
#                 case "👤ПОЛЬЗОВАТЕЛЬ":
#                     await message.answer("Выберите кнопку",
#                                          reply_markup=btns.change_data_kb())
#                     await states.Settings.set_setting.set()
#
#                 case "МАРАФОН ЖЕЛАНИЙ":
#                     await bot.send_photo(photo=open(photo_path, 'rb'), chat_id=user_id, caption=course_info)
#                     time.sleep(5)
#                     await message.answer('Выберите одну из кнопок', reply_markup=course.some_kb())
#
#                 case "✅ПРОВЕРИТЬ ПОДПИСКУ":
#                     if user_answer == "✅ПРОВЕРИТЬ ПОДПИСКУ":
#                         if check_sub:
#
#                             check = "Подписка действует до:\n\n"
#                             date_format = datetime.fromisoformat(check_sub)
#                             date_to_user = date_format.strftime("%d/%m/%Y")
#
#                             check += f"Дата {date_to_user}\n"
#                             check += "Спасибо за подписку"
#
#                             await message.answer(check,
#                                                  reply_markup=btns.ReplyKeyboardMarkup())
#                         else:
#                             await message.answer("У вас нет активной подписки.")
#
#                 case "НАЗАД":
#                     await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
#                                          reply_markup=btns.main_menu_kb())
#                     await dp.current_state(user=user_id).finish()
#
#                 case "Назaд":
#                     await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
#                                          reply_markup=btns.main_menu_kb())
#                     await dp.current_state(user=user_id).finish()
#
#                 case "Назадв":
#                     await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
#                                          reply_markup=btns.main_menu_kb())
#                     await dp.current_state(user=user_id).finish()
#
#                 case "Назад":
#                     await message.answer("Вы вернулись в ГЛАВНОЕ МЕНЮ",
#                                          reply_markup=btns.main_menu_kb())
#                     await dp.current_state(user=user_id).finish()
#
#
#         except Exception as e:
#             print(e)
#             await message.answer("Неверный ввод")
#
#
#     else:
#         await message.answer("Пробный период окончен. Оформите подписку",
#                              reply_markup=btns.course_order_kb())
#         await states.Subscription.check_subscription.set()
#
#
# @dp.message_handler(state=Subscription.check_subscription)
# async def user_sub(message, state=Subscription.check_subscription):
#     user_answer = message.text
#
#     if user_answer == "📝ОФОРМИТЬ ПОДПИСКУ":
#         await message.answer("Процесс оформления подписки",
#                              reply_markup=course.sub_inline())
#         await state.finish()
#
#
# @dp.callback_query_handler(text="paysub")
# async def buy(call: types.CallbackQuery):
#     await bot.delete_message(call.from_user.id, call.message.message_id)
#     PRICE = types.LabeledPrice(label="premium", amount=2000000)
#
#     if config.PAYMENTS_TOKEN.split(":")[1] == "TEST":
#         await bot.send_invoice(
#             chat_id=call.from_user.id,
#             title="Подписка на бота",
#             description="Активация подписки на бота на 1 месяц",
#             photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
#             payload="test-invoice-payload",
#             provider_token=config.PAYMENTS_TOKEN,
#             currency="UZS",
#             prices=[PRICE])
#
#
# @dp.pre_checkout_query_handler(lambda query: True)
# async def pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
#
#
# @dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
# async def successful_payment(message: types.Message):
#     amount_sub = message.successful_payment.total_amount
#     user_id = message.from_user.id
#
#     print(amount_sub)
#     if message.successful_payment.invoice_payload == "test-invoice-payload":
#         await bot.send_message(
#             message.chat.id,
#             f"Платеж на сумму {message.successful_payment.total_amount // 100}"
#             f" {message.successful_payment.currency} прошел успешно!!!",
#             reply_markup=btns.check_pay_kb())
#
#         database.set_sub_end(user_id)
#         database.add_payment_amount(amount_sub, user_id, True)
#
#
# @dp.callback_query_handler(lambda query: True)
# async def some(call: types.CallbackQuery):
#     user_id = call.from_user.id
#     photo_path = 'List_of_courses/course_photo1.jpg'
#
#     if call.data == "info":
#         await bot.send_message(call.from_user.id, "Информация о курсе")
#
#
#     elif call.data == "start":
#         status = 1
#         database.set_status(user_id, status)
#
#         await bot.delete_message(call.message.chat.id, call.message.message_id)
#         await bot.send_photo(photo=open(photo_path, 'rb'), chat_id=user_id, caption=welcome_msg, reply_markup=btns.ReplyKeyboardRemove())
#
#         time.sleep(3)
#
#         await bot.send_message(call.from_user.id, "Направления клиента", reply_markup=course.info_course())
#
#
#     elif call.data == "next":
#
#         await bot.delete_message(call.message.chat.id, call.message.message_id)
#         await bot.send_message(call.from_user.id, "Первая задание", reply_markup=course.start_course())
#
#         # database.update_status(user_id)  # Добавления к статусу +1
#
#
#
#
#
#
# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=False)
