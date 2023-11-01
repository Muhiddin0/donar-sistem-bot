from aiogram import types
from aiogram.dispatcher import FSMContext
from ..loader import dp
from .. import texts, buttons
from bot.models import User


@dp.callback_query_handler(state="*", text_contains='my-profile')
async def chek_subscribe_chanel(context: types.CallbackQuery, state: FSMContext):
    user_id = context.from_user.id
    user = await User.objects.async_get(user_id=user_id)
    first_name = context.from_user.first_name
    
    await context.message.answer(
        text=texts.profile.format(first_name, user.money),
        reply_markup=buttons.monney_transfer
    )