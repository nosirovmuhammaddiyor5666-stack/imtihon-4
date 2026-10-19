from aiogram.fsm.state import State,StatesGroup

class RegistrState(StatesGroup):
    name = State()
    phone = State()
    kurs_tanlash = State()