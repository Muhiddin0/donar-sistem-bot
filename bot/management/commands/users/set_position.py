from aiogram import types
from aiogram.dispatcher import FSMContext

from asgiref.sync import sync_to_async
from user.models import TempUser
from ..loader import dp
from .. import texts, buttons
from ..states import UserSatate

import asyncio

async def set_region_task(callback_query: types.CallbackQuery, state: FSMContext=None):
    user_id = callback_query.from_user.id
    callbac_data =  callback_query.data
    state_data = await state.get_data()
    state_data['position'] = callbac_data

    await state.set_data(state_data)
    print(state_data)

    await callback_query.message.delete()

    await callback_query.message.answer(
        text=texts.succes_form,
        reply_markup=buttons.remove
    )

    await sync_to_async(TempUser.objects.create)(
        name=state_data['fullname'],
        phone=state_data['phone'],
        region=state_data['region'],
        organizations=state_data['organizations'],
        position=state_data['position'],
        user_id=user_id
    )

    await state.finish()
    
@dp.callback_query_handler(state=UserSatate.position)
async def func(callback_query: types.CallbackQuery, state: FSMContext=None):
    asyncio.create_task(set_region_task(callback_query, state))