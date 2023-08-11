# from aiogram import Bot
# from aiogram.types import Message, LabeledPrice
# from main import YOOTOKEN
#
# async def order(message: Message, bot, Bot):
#     await bot_send_invoice(
#         chat_id=message.from_user.id,
#         title='Оформления подписки',
#         description='Описание товара',
#         payload='course_sub',
#         provider_token=YOOTOKEN,
#         currency='Руб',
#         start_parameter='test_bot',
#         prices=[dict(label='Руб', amount=15000)])