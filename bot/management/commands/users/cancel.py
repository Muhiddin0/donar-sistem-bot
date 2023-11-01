from aiogram import types
from aiogram.dispatcher import FSMContext
from ..loader import dp
from .. import texts, buttons


@dp.callback_query_handler(state="*", text_contains='cancel')
async def chek_subscribe_chanel(context: types.CallbackQuery, state: FSMContext):
    first_name = context.from_user.first_name
    await state.finish()
    await context.message.answer(
        text=texts.start.format(first_name),
        reply_markup=buttons.start
    )