from aiogram.dispatcher.filters.state import StatesGroup, State

class Form(StatesGroup):
    robot = State()
    sms = State()