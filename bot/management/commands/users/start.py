from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ..loader import dp, bot
from .. import texts, buttons

import asyncio

async def start_task(message: types.Message, state: FSMContext=None):
    await message.answer(texts.start.format(message.from_user.first_name), reply_markup=buttons.start_register)
    
@dp.message_handler(state="*", commands=['start'])
async def send_welcome(message: types.Message, state: FSMContext=None):
    asyncio.create_task(start_task(message, state))