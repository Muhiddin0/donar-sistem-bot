from aiogram import types
from aiogram.dispatcher import FSMContext

from ...loader import dp
from bot.models import User
from ...states import Form
from ... import texts, buttons
from OpenBudjet import OpenBudjet

from asgiref.sync import sync_to_async

from dotenv import load_dotenv
import os

load_dotenv()


@sync_to_async
def inncr_monney(user_id):
    AMOUNT = int(os.getenv('AMOUNT'))
    user = User.objects.get(user_id=user_id)
    user.money = user.money + AMOUNT
    user.save()

@dp.message_handler(state=Form.sms, content_types='text')
async def robot(message: types.Message, state: FSMContext):
    await message.answer("Tekshirilmoqda...")
    text = message.text
    user_id = message.from_user.id
    if text.isdigit() and len(text) == 6:
        state_data = await state.get_data()

        data = OpenBudjet().smsValid(
            otpKey=state_data['otpKey'],
            otpCode=text
        )

        if data.status_code != 200:
            await message.answer(text=texts.error_robot, reply_markup=buttons.cancel)
            return
        
        await inncr_monney(user_id=user_id)
        await message.answer(text=texts.sms_info, reply_markup=buttons.cancel)
        await state.finish()
        return
    
    await message.answer(
        text=texts.error_robot,
        reply_markup=buttons.cancel
    )