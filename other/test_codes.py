
# @dp.callback_query_handler(text='paysub')
# async def buy(call: types.CallbackQuery):
#     await bot.delete_message(call.from_user.id, call.message.message_id)
#     PRICE = types.LabeledPrice(label="Подписка на 1 месяц", amount=500 * 100)
#     if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
#
#         await bot.send_invoice(chat_id=call.from_user.id,
#                                title="Подписка на бота",
#                                description="Активация подписки на бота на 1 месяц",
#                                provider_token=config.PAYMENTS_TOKEN,
#                                currency="rub",
#                                photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
#                                photo_width=416,
#                                photo_height=234,
#                                photo_size=416,
#                                is_flexible=False,
#                                prices=[PRICE],
#                                start_parameter="one-month-subscription",
#                                payload="test-invoice-payload")
#
#
# @dp.pre_checkout_query_handler(lambda query: True)
# async def pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
#
#
# @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
# async def successful_payment(message):
#
#     amount_sub = message.successful_payment.total_amount
#     user_id = message.from_user.id
#
#     print(amount_sub)
#     if message.successful_payment.invoice_payload == 'test-invoice-payload':
#         await bot.send_message(message.chat.id,
#                                f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!", reply_markup=btns.check_pay_kb())


# @dp.callback_query_handler(lambda call: call.data in ["info", 'start'])
# async def some(call: types.CallbackQuery):
#     user_id = call.from_user.id
#     status =
#     update_status = database.update_status(user_id, status)
#
#     if call.data == 'info':
#
#         await bot.send_message(call.from_user.id, 'Что-то')
#
#     elif call.data == 'start':
#
#         await bot.send_message(call.from_user.id, 'Ёще что-то')


# @dp.callback_query_handler(lambda call: call.data in ['info', 'start', 'next, exit'])


# @dp.message_handler(state=UserRegistration.getting_phone_number, content_types=["contact"])
# async def get_number(message, state=UserRegistration.getting_phone_number):
#     user_answer = message.contact.phone_number
#
#     await state.update_data(number=user_answer)
#     await message.answer("Номер сохранил! Вы прошли регистрацию\n\nВыберите раздел.",
#                          reply_markup=btns.main_menu_kb())
#
#
#     all_info = await state.get_data()
#     user_id = message.from_user.id
#     name = all_info.get("name")
#     phone_number = all_info.get("number")
#     times = all_info.get("time_sub")
#     end_subb = all_info.get("end_sub")
#     gender = user_answer
#     user_status = all_info.get("status")
#     price = all_info.get("amount_sub")
#     database.add_user(user_id, name, phone_number, times, end_subb, gender, user_status, price)
#
#     await state.finish()



# @dp.message_handler(state=Subscription.check_subscription)
# async def user_sub(message, state=Subscription.check_subscription):
#     user_answer = message.text
#
#     if user_answer == "📝Obuna bo'lish":
#         await message.answer("Процесс оформления подписки",
#                              reply_markup=course.sub_inline())
#         await state.finish()


# @dp.callback_query_handler(text="paysub")
# async def buy(call: types.CallbackQuery):
#     await bot.delete_message(call.from_user.id, call.message.message_id)
#     price = types.LabeledPrice(label="premium", amount=2000000)
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
#             prices=[price])
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
#             reply_markup=btns.main_menu_kb())
#
#         database.set_sub_end(user_id)
#         database.add_payment_amount(amount_sub, user_id, True)

# elif user_answer == "✅ПРОВЕРИТЬ ПОДПИСКУ":
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

