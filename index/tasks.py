from bot.management.commands.loader import bot
from config.settings import (
    ADMIN,
    BOT_TOKEN as bot_token,
    API_ID as api_id, API_HASH as api_hash
    )
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.models import User

async def send_message(**kwargs):

    # Inline buttons
    inline_buttons = []
    for i in kwargs['btns']:inline_buttons.append([InlineKeyboardButton(text=i['title'], url=i['url'])])
    reply_markup = InlineKeyboardMarkup(inline_buttons)

    if bool(kwargs['btns']) == False:
        reply_markup = None

    # Message Body
    async with Client('bot_session', api_hash=api_hash, api_id=api_id, bot_token=bot_token) as app:
        if kwargs['content-type'] == 'text':    #TEXT
            message = await app.send_message(chat_id=ADMIN, text=kwargs['text'], reply_markup=  reply_markup)
        elif kwargs['content-type'] == 'image': # PHOTO
            message = await app.send_photo(chat_id=ADMIN, photo=kwargs['file'], caption=kwargs['text'], reply_markup=reply_markup)
        elif kwargs['content-type'] == 'video': # VIDEO
            message = await app.send_video(chat_id=ADMIN, file_name=kwargs['file-name'], video=kwargs['file'], reply_markup=reply_markup)
        elif kwargs['content-type'] == 'audio': # AUDIO 
            message = await app.send_audio(chat_id=ADMIN, file_name=kwargs['file-name'], audio=kwargs['file'], reply_markup=reply_markup)

    # send All users
    users = User.objects.all().values()
    for i in users:
        async with Client('bot_session', api_hash=api_hash, api_id=api_id, bot_token=bot_token) as app:
            await app.forward_messages(
                chat_id=i['user_id'],
                from_chat_id=message.chat.id,
                message_ids=message.id
            )