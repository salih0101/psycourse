TOKEN = "6655022114:AAEMmZeWNL13luUoluk81KUlL7m4maD-FFA"
# PAYMENTS_TOKEN = "381764678:TEST:58218"
# PAYMENTS_TOKEN = "398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"
CHANNEL_ID = '@psychofemme'

# if call.data == 'day_two':
#     await bot.send_message(call.from_user.id, 'Ожидай 24 часа')
#     await asyncio.sleep(5)
#     # await asyncio.sleep(1440)
#
#     await bot.send_message(call.from_user.id, day_two)
#     await bot.send_message(call.from_user.id, 'Чтобы получить аудио, Жми кнопку', reply_markup=inline_buttons.send_audio())
#
# elif call.data == 'send_audio':
#
#     audio_path = 'List_of_courses/1.ogg'
#     audio_path1 = 'List_of_courses/2.ogg'
#
#     if os.path.exists(audio_path) and os.path.exists(audio_path1):
#
#         with open(audio_path, 'rb') as audio_file:
#
#             await bot.send_audio(call.from_user.id, audio_file, caption='Ознакомления')
#             await asyncio.sleep(0.5)
#
#         with open(audio_path1, 'rb') as audio_file1:
#
#             await bot.send_audio(call.from_user.id, audio_file1, 'Задание')
#
#     await bot.send_message(call.from_user.id, 'Тестовый', reply_markup=inline_buttons.send_audio())


# --------------------------------------


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
#         await message.answer(f"Бесплатный курс \nДействует до: \n\n{dpp}",
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
#                 case 'Курс "Новая Я"':
#                     await bot.send_photo(photo=open(photo_path, 'rb'), chat_id=user_id, caption=course_info, reply_markup=course.some_kb())
#                     # time.sleep(5)
#                     # await message.answer('Выберите одну из кнопок')
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


# case "✅ПРОВЕРИТЬ ПОДПИСКУ":
#     if user_answer == "✅ПРОВЕРИТЬ ПОДПИСКУ":
#         if check_sub:
#
#             check = "Подписка действует до:\n\n"
#             date_format = datetime.fromisoformat(check_sub)
#             date_to_user = date_format.strftime("%d/%m/%Y")
#
#             check += f"Дата {date_to_user}\n"
#             check += "Спасибо за подписку"
#
#             await message.answer(check,
#                                  reply_markup=btns.ReplyKeyboardMarkup())
#         else:
#             await message.answer("У вас нет активной подписки.")
