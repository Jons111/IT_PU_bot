import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from keyboards.default.main import main_button, university_button, university_button_ru, main_button_ru
from keyboards.default.contact import contact_button, contact_button_ru
from keyboards.default.confirmation import confirmation_button, confirmation_button_ru
from keyboards.inline.language import inline_lang
from loader import dp, bot, base
from states.conditions import Form, Form_ru


@dp.callback_query_handler(text="Uzb")
async def bot_echo(report: CallbackQuery):
    user_id = report.from_user.id
    user = base.check_user(tg_id=user_id)

    if user[0] != 0:
        await bot.send_message(chat_id=user_id, text="Universitetimiz haqidagi ma'lumotlar",
                               reply_markup=university_button)

    else:
        await report.message.answer(text='Ismingizni kiriting', reply_markup=ReplyKeyboardRemove())
        await Form.for_name.set()


@dp.message_handler(state=Form.for_name)
async def bot_echo(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'name': name})
    await message.answer(text='Familyangizni kiriting')
    await Form.for_surname.set()


@dp.message_handler(state=Form.for_surname)
async def bot_echo(message: types.Message, state: FSMContext):
    surname = message.text
    await state.update_data({'surname': surname})
    index = 0
    keys = []
    j = 0
    regions = base.select_all_regions()
    for region in regions:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([InlineKeyboardButton(text=f'{region[1]}', callback_data=f'{region[1]}')])
        else:
            keys[index].append(InlineKeyboardButton(text=f'{region[1]}', callback_data=f"{region[1]}"))
        j += 1

    option_button = InlineKeyboardMarkup(inline_keyboard=keys)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Viloyatingizni tanlang", reply_markup=option_button)
    await Form.for_region.set()


@dp.callback_query_handler(state=Form.for_region)
async def bot_echo(message: CallbackQuery, state: FSMContext):
    region = message.data
    user_id = message.from_user.id
    await state.update_data({'region': region})
    await bot.send_message(chat_id=user_id, text=" Maktab nomi va raqamini kiriting")
    await Form.for_school.set()


@dp.message_handler(state=Form.for_school)
async def bot_echo(message: types.Message, state: FSMContext):
    school = message.text
    await state.update_data({'school': school})
    await message.answer(text='Telefon raqamingizni kiriting', reply_markup=contact_button)
    await Form.for_phone_number.set()


@dp.message_handler(state=Form.for_phone_number, content_types=ContentType.CONTACT)
async def bot_echo(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    await state.update_data({'phone': phone})

    informations = await state.get_data()
    name = informations.get('name')
    surname = informations.get('surname')
    school = informations.get('school')
    region = informations.get('region')
    phone_number = informations.get('phone')

    hhh = f"Ism: {name}\n" \
          f"Familiya: {surname}\n" \
          f"Maktab : {school}\n" \
          f"Viloyat : {region}\n" \
          f"Telefon raqam: {phone_number}\n"

    await message.answer(text=hhh, reply_markup=confirmation_button)
    await Form.confirmation.set()


@dp.message_handler(state=Form.for_phone_number)
async def bot_echo(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data({'phone': phone})

    informations = await state.get_data()
    name = informations.get('name')
    surname = informations.get('surname')
    school = informations.get('school')
    region = informations.get('region')
    phone_number = informations.get('phone')

    hhh = f"👨‍💼 Ism : {name}\n" \
          f"🧔‍♂ Familiya : {surname}\n" \
          f"🏫  Maktab : {school}\n" \
          f"🌐 Viloyat : {region}\n" \
          f"📞 Telefon raqam: {phone_number}\n"

    await message.answer(text=hhh, reply_markup=confirmation_button)
    await Form.confirmation.set()


@dp.message_handler(state=Form.confirmation, text='Ha')
async def bot_echo(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    informations = await state.get_data()
    name = informations.get('name')
    surname = informations.get('surname')
    school = informations.get('school')
    phone_number = informations.get('phone')
    number = base.count_registration()
    time = datetime.datetime.now()
    region = informations.get('region')

    hhh = f"👨‍💼 Ism : {name}\n" \
          f"🧔‍♂ Familiya : {surname}\n" \
          f"🏫  Maktab : {school}\n" \
          f"🌐 Viloyat : {region}\n" \
          f"📞 Telefon raqam: {phone_number}\n"

    idd = number[0] + 1
    try:
        base.add_registration(id=idd, tg_id=user_id, region=region, name=name, surname=surname, school=school,
                              phone_number=phone_number, date=time)
    except Exception as x:
        print(x)

    await bot.send_message(chat_id='5883029982', text=hhh)
    await bot.send_message(chat_id=user_id, text='Adminga yuborildi ✉️', reply_markup=main_button)
    await state.finish()


@dp.message_handler(state=Form.confirmation, text="Yo'q")
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Bekor qilindi ❌', reply_markup=inline_lang)
    await state.finish()


@dp.callback_query_handler(text="Rus")
async def bot_echo(report: CallbackQuery):
    user_id = report.from_user.id
    user = base.check_user(tg_id=user_id)

    if user[0] != 0:
        await bot.send_message(chat_id=user_id, text="Информация о нашем Университете",
                               reply_markup=university_button_ru)

    else:
        await report.message.answer(text='Введите имя', reply_markup=ReplyKeyboardRemove())
        await Form_ru.for_name.set()


@dp.message_handler(state=Form_ru.for_name)
async def bot_echo(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'name': name})
    await message.answer(text='Введите фамилию')
    await Form_ru.for_surname.set()


@dp.message_handler(state=Form_ru.for_surname)
async def bot_echo(message: types.Message, state: FSMContext):
    surname = message.text
    await state.update_data({'surname': surname})
    index = 0
    keys = []
    j = 0
    regions = base.select_all_regions_ru()
    print(regions,'ru-----------------')
    for region in regions:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([InlineKeyboardButton(text=f'{region[1]}', callback_data=f'{region[3]}')])
        else:
            keys[index].append(InlineKeyboardButton(text=f'{region[1]}', callback_data=f"{region[3]}"))
        j += 1

    option_button = InlineKeyboardMarkup(inline_keyboard=keys)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Выберите регион", reply_markup=option_button)
    await Form_ru.for_region.set()


@dp.callback_query_handler(state=Form_ru.for_region)
async def bot_echo(message: CallbackQuery, state: FSMContext):
    region = message.data
    user_id = message.from_user.id
    await state.update_data({'region': region})
    await bot.send_message(chat_id=user_id, text="Введите название школы или номер")
    await Form_ru.for_school.set()


@dp.message_handler(state=Form_ru.for_school)
async def bot_echo(message: types.Message, state: FSMContext):
    school = message.text
    await state.update_data({'school': school})
    await message.answer(text='Введите номер телефона', reply_markup=contact_button_ru)
    await Form_ru.for_phone_number.set()


@dp.message_handler(state=Form_ru.for_phone_number, content_types=ContentType.CONTACT)
async def bot_echo(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    await state.update_data({'phone': phone})

    informations = await state.get_data()
    name = informations.get('name')
    surname = informations.get('surname')
    school = informations.get('school')
    phone_number = informations.get('phone')
    region = informations.get('region')

    sss = f"👨‍💼 Имя: {name}\n" \
          f"🧔‍♂ Фамилия: {surname}\n" \
          f"🏫 Школа: {school}\n" \
          f"🌐 Регион: {region}\n" \
          f"📞 Номер телефона: {phone_number}\n"

    await message.answer(text=sss, reply_markup=confirmation_button_ru)
    await Form_ru.confirmation.set()


@dp.message_handler(state=Form_ru.for_phone_number)
async def bot_echo(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data({'phone': phone})

    informations = await state.get_data()
    name = informations.get('name')
    surname = informations.get('surname')
    school = informations.get('school')
    phone_number = informations.get('phone')
    region = informations.get('region')

    sss = f"👨‍💼 Имя: {name}\n" \
          f"🧔‍♂ Фамилия: {surname}\n" \
          f"🏫 Школа: {school}\n" \
          f"🌐 Регион: {region}\n" \
          f"📞 Номер телефона: {phone_number}\n"

    await message.answer(text=sss, reply_markup=confirmation_button_ru)
    await Form_ru.confirmation.set()


@dp.message_handler(state=Form_ru.confirmation, text='Да')
async def bot_echo(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    informations = await state.get_data()
    name = informations.get('name')
    surname = informations.get('surname')
    school = informations.get('school')
    phone_number = informations.get('phone')
    region = informations.get('region')
    number = base.count_registration()
    time = datetime.datetime.now()

    sss = f"👨‍💼 Имя: {name} ✔️\n" \
          f"🧔‍♂ Фамилия: {surname} ✔️\n" \
          f"🏫 Школа: {school} ✔️\n" \
          f"🌐 Регион: {region}  ✔  \n"  \
          f"📞 Номер телефона: {phone_number} ✔️\n"

    idd = number[0] + 1
    try:
        base.add_registration(id=idd, tg_id=user_id, name=name, region=region, surname=surname, school=school,
                              phone_number=phone_number, date=time)
    except Exception:
        pass

    await bot.send_message(chat_id='5883029982', text=sss)
    await bot.send_message(chat_id=user_id, text='Отправлено администратору ✉️', reply_markup=main_button_ru)
    await state.finish()


@dp.message_handler(state=Form_ru.confirmation, text="Нет")
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Отменен ❌', reply_markup=inline_lang)
    await state.finish()
