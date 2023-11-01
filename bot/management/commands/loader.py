import logging
from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from django.conf import settings

from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=storage)