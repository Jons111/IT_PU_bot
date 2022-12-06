from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    for_name = State()
    for_surname = State()
    for_school = State()
    for_region = State()
    for_phone_number = State()
    confirmation = State()


class Form_ru(StatesGroup):
    for_name = State()
    for_surname = State()
    for_school = State()
    for_region = State()
    for_phone_number = State()
    confirmation = State()

class QuizState(StatesGroup):
    get_answer_state = State()
    finish_state = State()
    pre_state = State()
class QuizState_ru(StatesGroup):
    get_answer_state = State()
    finish_state = State()
    pre_state = State()