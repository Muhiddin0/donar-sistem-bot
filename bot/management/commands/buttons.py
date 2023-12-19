
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from base import organizators_list

start_register = ReplyKeyboardMarkup([["👨‍💻 Ro'yxatdan o'tish"]], resize_keyboard=True)

cancel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('❌ Bekor qilish', callback_data='cancel')
    ]
])

phone = ReplyKeyboardMarkup([[KeyboardButton(text="📞 Jo'natish", request_contact=True)]], resize_keyboard=True)

regions = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton("Tashkent Region", callback_data="1:toshkent")],
    [InlineKeyboardButton("Andijan Region", callback_data="2:andijon")],
    [InlineKeyboardButton("Bukhara Region", callback_data="3:buxoro")],
    [InlineKeyboardButton("Fergana Region", callback_data="4:fargona")],
    [InlineKeyboardButton("Jizzakh Region", callback_data="5:jizzax")],
    [InlineKeyboardButton("Namangan Region", callback_data="6:namangan")],
    [InlineKeyboardButton("Samarqand Region", callback_data="7:samarqand")],
    [InlineKeyboardButton("Sirdaryo Region", callback_data="8:sirdaryo")],
    [InlineKeyboardButton("Qashqadaryo Region", callback_data="9:qashqadaryo")],
    [InlineKeyboardButton("Surxondaryo Region", callback_data="10:surxondaryo")],
    [InlineKeyboardButton("Xorazm Region", callback_data="11:xorazim")],
    [InlineKeyboardButton("Republic of Karakalpakstan", callback_data="12:qoraqalpoq")],
    [InlineKeyboardButton('❌ Bekor qilish', callback_data='cancel')]
])

def organizators(index):
    replay_markup = InlineKeyboardMarkup(row_width=1)
    for i in organizators_list[index]:
        replay_markup.add(InlineKeyboardButton(i["value"], callback_data=i["id"]))

    return replay_markup

position = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton("Rahbar", callback_data="1")],
    [InlineKeyboardButton("Rahbar o'rinbosari", callback_data="2")],
    [InlineKeyboardButton("Boshqa", callback_data="3")]
])

remove = ReplyKeyboardRemove()