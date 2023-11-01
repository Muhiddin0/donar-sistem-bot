import asyncio
from pyrogram import Client

from config.settings import (
    ADMIN,
    BOT_TOKEN as bot_token,
    API_ID as api_id, API_HASH as api_hash
    )

app = Client("bot_session", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
app.run()