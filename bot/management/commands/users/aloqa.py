from aiogram import types
from aiogram.dispatcher import FSMContext
from ..loader import dp
from .. import texts

@dp.callback_query_handler(state="*", text_contains='get-contact')
async def chek_subscribe_chanel(context: types.CallbackQuery, state: FSMContext):
    await context.message.answer(
        text=texts.aloqa
    )