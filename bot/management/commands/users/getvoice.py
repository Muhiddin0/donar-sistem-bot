from aiogram import types
from aiogram.dispatcher import FSMContext
from ..loader import dp
from .. import texts
from bot.models import User


@dp.callback_query_handler(state="*", text_contains='start-voice')
async def chek_subscribe_chanel(context: types.CallbackQuery, state: FSMContext):
    user_id = context.message.from_user.id
    await context.message.answer(
        text=texts.start_voice
    )