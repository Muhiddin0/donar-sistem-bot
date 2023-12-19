from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from user.models import TempUser
from ..loader import dp
from ..states import UserSatate
from .. import texts, buttons

import asyncio


async def set_register_task(message: types.Message, state: FSMContext=None):
    user_id = message.from_user.id
    user = await sync_to_async(TempUser.objects.filter)(user_id=user_id)

    if user:
        if user.first().reject:
            await message.answer(texts.reject_user)
            return
            
        await message.answer(texts.temp_user)
        return

    await message.answer(texts.greeat, reply_markup=buttons.remove)
    await message.answer(texts.fullname, reply_markup=buttons.cancel)
    await UserSatate.fullname.set()
    
@dp.message_handler(text="👨‍💻 Ro'yxatdan o'tish")
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_register_task(message, state))