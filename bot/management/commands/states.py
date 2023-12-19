from aiogram.dispatcher.filters.state import StatesGroup, State

class UserSatate(StatesGroup):
    fullname = State()
    phone = State()
    region = State()
    organization = State()
    position = State()