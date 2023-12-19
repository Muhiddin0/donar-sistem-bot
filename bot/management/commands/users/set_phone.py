from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ..loader import dp, bot
from .. import texts, buttons
from ..states import UserSatate

import asyncio

async def set_phone_task(message: types.Message, state: FSMContext=None):
    phone = message.contact.phone_number

    state_data = await state.get_data()
    state_data['phone'] = phone
    
    await state.set_data(state_data)
    
    await message.answer(
        text=texts.select_region,
        reply_markup=buttons.regions
    )
    
    await UserSatate.region.set()
    
@dp.message_handler(content_types=types.ContentType.CONTACT, state=UserSatate.phone)
async def func(message, state):
    asyncio.create_task(set_phone_task(message, state))