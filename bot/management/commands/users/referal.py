from aiogram import types
from aiogram.dispatcher import FSMContext
from ..loader import dp
from .. import texts, buttons
from dotenv import load_dotenv
import os

@dp.callback_query_handler(state="*", text_contains='referal')
async def referal(context: types.CallbackQuery, state: FSMContext):
    user_id = context.from_user.id
    await state.finish()
    await context.message.answer(
        text=texts.referalka.format(),
    )
    bot_username = os.getenv('BOT_USERNAME')
    referal = bot_username + "?start={}".format(user_id)
    await context.message.answer(
        text=texts.share_adds.format(referal),
        reply_markup=buttons.share
    )