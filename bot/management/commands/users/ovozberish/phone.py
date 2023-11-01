from aiogram import types
from aiogram.dispatcher import FSMContext

from ...loader import dp
from bot.models import User
from ...states import Form
from ... import texts, buttons
from OpenBudjet import OpenBudjet

import base64

@dp.message_handler(content_types='text')
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer("⏳")
    text = message.text
    if text.isdigit() and len(text) == 9:
        data = OpenBudjet().getVoice()
        if data['ok'] == False:
            await message.answer(
                text=texts.get_robot_error
            )
        await message.answer_photo(
            photo=base64.b64decode(data['img']),
            caption="Misol javobini kiriting",
                reply_markup=buttons.cancel
        )
        await state.set_data(
            data={
                "captchaKey":data['captchaKey'],
                'phone':text,
            }
        )
        await Form.robot.set()
        return
    
    await message.answer(
        text=texts.error_phone
    )