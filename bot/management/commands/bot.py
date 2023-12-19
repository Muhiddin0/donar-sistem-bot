from typing import Any, Optional
from aiogram import executor
from .loader import dp

from . import users

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Botni ishga tushirish"

    def handle(self, *args: Any, **options: Any):
        executor.start_polling(dp, skip_updates=True)
