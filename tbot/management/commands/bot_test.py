import asyncio
import random
import signal
import sys
from django.core.management.base import BaseCommand
from bot.management.commands.users.start import send_welcome
from datetime import datetime

def bot_test():

    random_user_id = random.randint(111111111, 999999999)

    message= {
        "message_id": 6813,
        "from": {
            "id": random_user_id,
            "is_bot": False,
            "first_name": "Muhiddin",
            "username": "muhiddin_kabraliev_coder",
            "language_code": "en"
            },
        "chat": {
            "id": random_user_id, "first_name": "Muhiddin", "username": "muhiddin_kabraliev_coder", "type": "private"}, "date": 1690493166, "text": "/start", "entities": [{"type": "bot_command", "offset": 0, "length": 6}]}

    user = asyncio.run(send_welcome(message=message))
    print(user)


class Command(BaseCommand):
    help = "salom"
    global task_count
    global start_time
    task_count = 0
    start_time = datetime.now().strftime("%H:%M:%S")
    
    def exit_test(signal, frame):
        end_time = datetime.now().strftime("%H:%M:%S")
        print("counts:", task_count)
        print("start:", start_time)
        print("end:",end_time)
    
        sys.exit(0)
    
    signal.signal(signal.SIGINT, exit_test)

    while True:
        bot_test()
        task_count += 1