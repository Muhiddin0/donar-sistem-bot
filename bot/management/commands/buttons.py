
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 🙍🏻‍♂️📞⏳🎉❗️❌👋🏻⚠️💸ℹ️

start = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('📩 Ovoz berish', callback_data='start-voice'),
        InlineKeyboardButton('🖇 Havolam', callback_data='referal'),
    ],
    [
        InlineKeyboardButton('📞 Aloqa', callback_data='get-contact')
    ]
])

cancel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('❌ Bekor qilish', callback_data='cancel'),
    ]
])

monney_transfer = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('💸 Pulni chiqarish', callback_data='transer-monney'),
    ]
])

share = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='👥 Ulashish', switch_inline_query='shu botga kirib ovoz bering 100% pul to\'lar ekan  ')
    ]
])