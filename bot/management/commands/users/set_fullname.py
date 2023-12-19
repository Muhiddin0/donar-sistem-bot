from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ..loader import dp, bot
from .. import texts, buttons
from ..states import UserSatate

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    text =  message.text
    await state.set_data(
        {
            'fullname':text
        }
    )
    await message.answer(
        text=texts.phone,
        reply_markup=buttons.phone
    )
    await UserSatate.phone.set()
    
@dp.message_handler(state=UserSatate.fullname, content_types='text')
async def func(message, state):
    asyncio.create_task(set_name_task(message, state))