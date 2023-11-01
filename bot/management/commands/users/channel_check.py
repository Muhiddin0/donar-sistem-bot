from aiogram import types
from aiogram.dispatcher import FSMContext
from ..loader import dp, bot
from .. import texts, buttons
from bot.models import User
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@dp.callback_query_handler(state="*", text_contains='check-chanel')
async def chanel_validate(context: types.CallbackQuery, state: FSMContext):
    user_id = context.from_user.id
    left_chanel_list = []
    for i in ("@itkentuz", "@OrginalCoder"):
        user_status = await bot.get_chat_member(chat_id=i, user_id=user_id)
        if user_status['status'] == "left":
            left_chanel_list.append(
                [InlineKeyboardButton(i.replace('@', ''), url="https://t.me/{}".format(i.replace('@', '')))]
            )
            
    if bool(left_chanel_list):
        left_chanel_list.append(
            [InlineKeyboardButton("✅ Tekshirish", callback_data="check-chanel")]
        )
        button = InlineKeyboardMarkup(inline_keyboard=left_chanel_list)
        await context.message.edit_text(
            text=texts.obuna,
            reply_markup=button
        )
        return
    await context.message.edit_text(
            text=texts.start,
            reply_markup=buttons.start
        )