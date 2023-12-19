from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ..loader import dp, bot
from .. import texts, buttons
from ..states import UserSatate

import asyncio

async def set_region_task(callback_query: types.CallbackQuery, state: FSMContext=None):
    callbac_data =  callback_query.data
    state_data = await state.get_data()
    state_data['organizations'] = callbac_data

    await state.set_data(state_data)

    await callback_query.message.edit_text(
        text=texts.organization,
        reply_markup=buttons.position
    )
    await UserSatate.position.set()
    
@dp.callback_query_handler(state=UserSatate.organization)
async def func(callback_query: types.CallbackQuery, state: FSMContext=None):
    asyncio.create_task(set_region_task(callback_query, state))