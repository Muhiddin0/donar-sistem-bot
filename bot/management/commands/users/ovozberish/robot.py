from aiogram import types
from aiogram.dispatcher import FSMContext

from ...loader import dp
from bot.models import User
from ...states import Form
from ... import texts, buttons
from OpenBudjet import OpenBudjet

import base64

@dp.message_handler(state=Form.robot, content_types='text')
async def robot(message: types.Message, state: FSMContext):
    await message.answer("Tekshirilmoqda...")
    text = message.text
    if text.isdigit():
        state_data = await state.get_data()
        data = OpenBudjet().robotValid(
            robotResult=text,
            captchaKey=state_data['captchaKey'],
            phone=state_data['phone']
        )
        
        if data.status_code != 200:
            await message.answer(
                text=texts.error_robot,
                reply_markup=buttons.cancel
                )
            return
        
        data = data.json()

        state_data['otpKey'] = data['otpKey']
        await state.set_data(data=state_data)

        await message.answer(
            text=texts.sms_info,
            reply_markup=buttons.cancel
            )
        await Form.sms.set()
        return

    await message.answer(
        text=texts.error_robot
    )