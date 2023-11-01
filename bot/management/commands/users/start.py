from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.models import User
from ..loader import dp, bot
from .. import texts, buttons

from asgiref.sync import sync_to_async
import asyncio

from dotenv import load_dotenv
import os

load_dotenv()

@sync_to_async
def incr_ref(ref_id):
    user = User.objects.filter(user_id=ref_id).values()
    if bool(user):
        ref_amount = int(os.getenv('REF_AMOUNT'))
        user.referal_money = user.referal_money + ref_amount
        user.save()

@dp.message_handler(state="*", commands=['start'])
async def send_welcome(message: types.Message, state: FSMContext=None):

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    users = await User.objects.async_filter(user_id=user_id)
    
    user = users.values()
    refid = message.get_args()   
    
    left_chanel_list = []
    for i in ("@itkentuz", "@OrginalCoder"):
        user_status = await bot.get_chat_member(chat_id=i, user_id=user_id)
        if user_status['status'] == "left":
            left_chanel_list.append(
                [InlineKeyboardButton(i.replace('@', ''), url="https://t.me/{}".format(i.replace('@', '')))]
            )
            
    if bool(left_chanel_list):
        left_chanel_list.append(
            [InlineKeyboardButton("✅ Tekshirish", callback_data="check-chanel")]
        )
        button = InlineKeyboardMarkup(inline_keyboard=left_chanel_list)
        await message.answer(
            text=texts.obuna,
            reply_markup=button
        )
        return        
    
    if not bool(user):
        if bool(refid):
            await bot.send_message(chat_id=refid, text=texts.ref_succes.format(first_name))

        await User.objects.async_create(
            user_id=user_id,
            first_name=first_name,
            money=0,
            referal_money=0
        )

    await message.answer(
        text=texts.start.format(first_name),
        reply_markup=buttons.start
    )