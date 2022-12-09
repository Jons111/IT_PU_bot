import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from keyboards.inline.language import inline_pre
from states.conditions import QuizState
from loader import dp, base, bot
from keyboards.default.contact import next_button
from keyboards.default.main import main_button, university_button


# Echo bot
@dp.message_handler(text='ITPU')
async def bot_echo(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = base.check_user_quiz(tg_id=user_id)
    user_ru = base.check_user_quiz_ru(tg_id=user_id)
    if int(user[0]) == 0 and int(user_ru[0])==0:
        test_number = 1
        await state.update_data({'test_number': test_number})
        q = base.select_question(id=test_number)
        question_text = q[1]
        q_id = q[0]
        question = q[2:]
        index = 0
        keys = []

        for j in range(4):
            if j % 2 == 0 and j != 0:
                index += 1
            if j % 2 == 0:
                keys.append([InlineKeyboardButton(text=f'{question[j]}', callback_data=f'{q_id} {j + 1}')])
            else:
                keys[index].append(InlineKeyboardButton(text=f'{question[j]}', callback_data=f"{q_id} {j + 1}"))
            j += 1

        option_button = InlineKeyboardMarkup(inline_keyboard=keys)
        await message.answer(text=question_text, reply_markup=option_button)

        await QuizState.get_answer_state.set()
    else:
        user = base.select_player(tg_id=user_id)

        ball = user[7]
        await bot.send_message(chat_id=user_id,
                               text=f"Siz testni yechib bo'lgansiz va   {ball} ta ✅ testni topgansiz qayta yechish mumkin emas ",
                               reply_markup=university_button)


@dp.callback_query_handler(state=QuizState.get_answer_state)
async def bot_echo(report: CallbackQuery, state: FSMContext):
    data = report.data
    quiz = data.split(' ')
    user_id = report.from_user.id
    quiz_id = int(quiz[0])
    answer_id = (quiz[1])

    question = base.select_quiz(id=quiz_id)

    answer = "V" + answer_id
    correct_answer = question[6]
    tg_id = report.from_user.id
    name = report.from_user.first_name
    user_name = report.from_user.username
    time = datetime.datetime.now()
    message_id = report.message.message_id

    await bot.delete_message(chat_id=user_id, message_id=message_id)
    if correct_answer == answer:
        base.add_result(tg_id=tg_id, name=name, username=user_name, quiz=quiz_id,
                        answer_id=answer_id, answer=answer, time=time, result=True)
    else:
        base.add_result(tg_id=tg_id, name=name, username=user_name, quiz=quiz_id,
                        answer_id=answer_id, answer=answer, time=time, result=False)

    text = await state.get_data()
    quiz_number = int(base.count_question()[0])
    test_number = int(text.get('test_number')) + 1

    if quiz_number < test_number:

        await bot.send_message(chat_id=user_id, text="Ushbu prezintatsiyamiz yoqdimi ?", reply_markup=inline_pre)
        await QuizState.pre_state.set()

    else:
        await state.update_data({'test_number': test_number})
        q = base.select_question(id=test_number)
        question_text = q[1]
        q_id = q[0]
        question = q[2:]
        index = 0
        keys = []

        for j in range(4):
            if j % 2 == 0 and j != 0:
                index += 1
            if j % 2 == 0:
                keys.append([InlineKeyboardButton(text=f'{question[j]}', callback_data=f'{q_id} {j + 1}')])
            else:
                keys[index].append(InlineKeyboardButton(text=f'{question[j]}', callback_data=f"{q_id} {j + 1}"))
            j += 1

        option_button = InlineKeyboardMarkup(inline_keyboard=keys)
        await bot.send_message(chat_id=user_id, text=question_text, reply_markup=option_button)
        await QuizState.get_answer_state.set()

@dp.callback_query_handler(state=QuizState.pre_state)
async def bot_echo(report: CallbackQuery, state: FSMContext):
        data = report.data
        user_id = report.from_user.id
        if data == '1':
            base.update_registration_pre(presentation="Ha", tg_id=user_id)
        elif data == '2':
            base.update_registration_pre(presentation="Yo'q", tg_id=user_id)
        results = base.select_answers(tg_id=user_id)
        result = 0
        for i in results:
            result += int(i[0])
        base.update_registration(result, tg_id=user_id)

        user = base.select_player(tg_id=user_id)
        print(user)
        region_name = user[8]
        name = user[1]
        last_name = user[2]
        school = user[4]
        region = base.select_region(name=region_name)

        try:

            region_id = region[0]
            worker = base.select_worker(region_id=region_id)

            worker_id = worker[4]
            hhh = f"👨‍💼 Ism: {name}\n" \
                  f"🧔‍♂ Familya: {last_name}\n" \
                  f"🏫  Maktab : {school}\n " \
                  f"🏆  Natija : {result} ta to'g'ri javob topdi \n"

            await bot.send_message(chat_id=worker_id, text=hhh)
        except Exception as x:
           print(x)

        await bot.send_message(chat_id=user_id,
                               text=f"Test yakunlandi.\n Tabriklaymiz {result} ta ✅ savolga to'g'ri javob berdingiz ",
                               reply_markup=main_button)

        await state.finish()