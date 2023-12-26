from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from project_fun import *
from project_text import *

bot = Bot(token='6006582578:AAEVLSXuuRFPbBIrBW5kqiSgKvbPdjjV91I')
dp = Dispatcher(bot, storage=MemoryStorage())


class Calcul(StatesGroup):
    num1 = State()
    num2 = State()
    num3 = State()
    num4 = State()
    num5 = State()
    num6 = State()
    num7 = State()
    num8 = State()
    num9 = State()
    num10 = State()


ikb1 = InlineKeyboardMarkup(row_width=2)
i1 = InlineKeyboardButton(text='Информация',
                          callback_data='info')
i2 = InlineKeyboardButton(text='Парсер валют',
                          callback_data='parse')
i3 = InlineKeyboardButton(text='Поддержка',
                          callback_data='support')
i4 = InlineKeyboardButton(text='Калькулятор валют',
                          callback_data='calc')
ikb1.add(i3, i1, i2, i4)

ikb2 = InlineKeyboardMarkup()
ii1 = InlineKeyboardButton(text='USD🇺🇸',
                           callback_data='USDp')
ii2 = InlineKeyboardButton(text='EUR🇪🇺',
                           callback_data='EURp')
ii3 = InlineKeyboardButton(text='BRL🇧🇷',
                           callback_data='BRLp')
ii4 = InlineKeyboardButton(text='KRW🇰🇷',
                           callback_data='KRWp')
ii5 = InlineKeyboardButton(text='HKD🇭🇰',
                           callback_data='HKDp')
ii6 = InlineKeyboardButton(text='AED🇦🇪',
                           callback_data='AEDp')
ii7 = InlineKeyboardButton(text='INR🇮🇳',
                           callback_data='INRp')
ii8 = InlineKeyboardButton(text='CNY🇨🇳',
                           callback_data='CNYp')
ii9 = InlineKeyboardButton(text='GBP🇬🇧',
                           callback_data='GBPp')
ii10 = InlineKeyboardButton(text='JPY🇯🇵',
                            callback_data='JPYp')
ikb2.add(ii1, ii2, ii3, ii4, ii5, ii6, ii7, ii8, ii9, ii10)

ikb3 = InlineKeyboardMarkup()
ik1 = InlineKeyboardButton(text='USD🇺🇸',
                           callback_data='USDc')
ik2 = InlineKeyboardButton(text='EUR🇪🇺',
                           callback_data='EURc')
ik3 = InlineKeyboardButton(text='BRL🇧🇷',
                           callback_data='BRLc')
ik4 = InlineKeyboardButton(text='KRW🇰🇷',
                           callback_data='KRWc')
ik5 = InlineKeyboardButton(text='HKD🇭🇰',
                           callback_data='HKDc')
ik6 = InlineKeyboardButton(text='AED🇦🇪',
                           callback_data='AEDc')
ik7 = InlineKeyboardButton(text='INR🇮🇳',
                           callback_data='INRc')
ik8 = InlineKeyboardButton(text='CNY🇨🇳',
                           callback_data='CNYc')
ik9 = InlineKeyboardButton(text='GBP🇬🇧',
                           callback_data='GBPc')
ik10 = InlineKeyboardButton(text='JPY🇯🇵',
                            callback_data='JPYc')
ikb3.add(ik1, ik2, ik3, ik4, ik5, ik6, ik7, ik8, ik9, ik10)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(start_text,
                         reply_markup=ikb1)


@dp.message_handler(commands=['info'])
async def info_command(message: types.Message):
    await message.answer(info_text)


@dp.message_handler(commands=['parse'])
async def parse_command(message: types.Message):
    await message.answer('Выбери нужную валюту: 💰',
                         reply_markup=ikb2)


@dp.message_handler(commands=['support'])
async def info_command(message: types.Message):
    await message.answer(support_text)


@dp.message_handler(commands=['calc'])
async def calc_command(message: types.Message):
    await message.answer('Выбери нужную валюту: 💰',
                         reply_markup=ikb3)


@dp.callback_query_handler(text='calc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Выбери нужную валюту: 💰',
                                        reply_markup=ikb3)


@dp.callback_query_handler(text='USDc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введите число:')
    await callback_query.message.answer('Вводите только целые числа без каких-либо знаков')
    await Calcul.num1.set()


@dp.message_handler(state=Calcul.num1)
async def calc_command(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Было введено некоректное значение\nВведите еще раз')
        return
    await state.update_data(n1=float(message.text))
    data = await state.get_data()
    curs = round(float(f'{data["n1"]}') * USD(), 4)
    await message.answer(f'{data["n1"]} USD🇺🇸\n{curs} RUB🇷🇺')
    await state.finish()
    await message.answer('Выбери что тебе нужно👇',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='EURc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введите число:')
    await callback_query.message.answer('Вводите только целые числа без каких-либо знаков')
    await Calcul.num2.set()


@dp.message_handler(state=Calcul.num2)
async def calc_command(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Было введено некоректное значение\nВведите еще раз')
        return
    await state.update_data(n2=float(message.text))
    data = await state.get_data()
    curs = round(float(f'{data["n2"]}') * EUR(), 4)
    await message.answer(f'{data["n2"]} EUR🇪🇺\n{curs} RUB🇷🇺')
    await state.finish()
    await message.answer('Выбери что тебе нужно👇',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='BRLc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введите число:')
    await callback_query.message.answer('Вводите только целые числа без каких-либо знаков')
    await Calcul.num3.set()


@dp.message_handler(state=Calcul.num3)
async def calc_command(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Было введено некоректное значение\nВведите еще раз')
        return
    await state.update_data(n3=float(message.text))
    data = await state.get_data()
    curs = round(float(f'{data["n3"]}') * BRL(), 4)
    await message.answer(f'{data["n3"]} BRL🇧🇷\n{curs} RUB🇷🇺')
    await state.finish()
    await message.answer('Выбери что тебе нужно👇',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='KRWc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введите число:')
    await callback_query.message.answer('Вводите только целые числа без каких-либо знаков')
    await Calcul.num4.set()


@dp.message_handler(state=Calcul.num4)
async def calc_command(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Было введено некоректное значение\nВведите еще раз')
        return
    await state.update_data(n4=float(message.text))
    data = await state.get_data()
    curs = round((float(f'{data["n4"]}') * KRW()) / 1000, 7)
    await message.answer(f'{data["n4"]} KRW🇰🇷\n{curs} RUB🇷🇺')
    await state.finish()
    await message.answer('Выбери что тебе нужно👇',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='HKDc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введите число:')
    await callback_query.message.answer('Вводите только целые числа без каких-либо знаков')
    await Calcul.num5.set()


@dp.message_handler(state=Calcul.num5)
async def calc_command(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Было введено некоректное значение\nВведите еще раз')
        return
    await state.update_data(n5=float(message.text))
    data = await state.get_data()
    curs = round(float(f'{data["n5"]}') * HKD(), 4)
    await message.answer(f'{data["n5"]} HKD🇭🇰\n{curs} RUB🇷🇺')
    await state.finish()
    await message.answer('Выбери что тебе нужно👇',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='AEDc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введите число:')
    await callback_query.message.answer('Вводите только целые числа без каких-либо знаков')
    await Calcul.num6.set()


@dp.message_handler(state=Calcul.num6)
async def calc_command(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Было введено некоректное значение\nВведите еще раз')
        return
    await state.update_data(n6=float(message.text))
    data = await state.get_data()
    curs = round(float(f'{data["n6"]}') * AED(), 4)
    await message.answer(f'{data["n6"]} AED🇦🇪\n{curs} RUB🇷🇺')
    await state.finish()
    await message.answer('Выбери что тебе нужно👇',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='INRc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введите число:')
    await callback_query.message.answer('Вводите только целые числа без каких-либо знаков')
    await Calcul.num7.set()


@dp.message_handler(state=Calcul.num7)
async def calc_command(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Было введено некоректное значение\nВведите еще раз')
        return
    await state.update_data(n7=float(message.text))
    data = await state.get_data()
    curs = round((float(f'{data["n7"]}') * INR()) / 10, 5)
    await message.answer(f'{data["n7"]} INR🇮🇳\n{curs} RUB🇷🇺')
    await state.finish()
    await message.answer('Выбери что тебе нужно👇',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='CNYc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введите число:')
    await callback_query.message.answer('Вводите только целые числа без каких-либо знаков')
    await Calcul.num8.set()


@dp.message_handler(state=Calcul.num8)
async def calc_command(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Было введено некоректное значение\nВведите еще раз')
        return
    await state.update_data(n8=float(message.text))
    data = await state.get_data()
    curs = round(float(f'{data["n8"]}') * CNY(), 4)
    await message.answer(f'{data["n8"]} CNY🇨🇳\n{curs} RUB🇷🇺')
    await state.finish()
    await message.answer('Выбери что тебе нужно👇',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='GBPc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введите число:')
    await callback_query.message.answer('Вводите только целые числа без каких-либо знаков')
    await Calcul.num9.set()


@dp.message_handler(state=Calcul.num9)
async def calc_command(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Было введено некоректное значение\nВведите еще раз')
        return
    await state.update_data(n9=float(message.text))
    data = await state.get_data()
    curs = round(float(f'{data["n9"]}') * GBP(), 4)
    await message.answer(f'{data["n9"]} GBP🇬🇧\n{curs} RUB🇷🇺')
    await state.finish()
    await message.answer('Выбери что тебе нужно👇',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='JPYc')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Введите число:')
    await callback_query.message.answer('Вводите только целые числа без каких-либо знаков')
    await Calcul.num10.set()


@dp.message_handler(state=Calcul.num10)
async def calc_command(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Было введено некоректное значение\nВведите еще раз')
        return
    await state.update_data(n10=float(message.text))
    data = await state.get_data()
    curs = round((float(f'{data["n10"]}') * JPY()) / 100, 6)
    await message.answer(f'{data["n10"]} JPY🇯🇵\n{curs} RUB🇷🇺')
    await state.finish()
    await message.answer('Выбери что тебе нужно👇',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='info')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(info_text)


@dp.callback_query_handler(text='support')
async def process_callback_info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(support_text)


@dp.callback_query_handler(text='parse')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('Выбери нужную валюту: 💰',
                                        reply_markup=ikb2)


@dp.callback_query_handler(text='USDp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Доллар США\nЕдиниц: 1\nКурс ЦБ РФ: {USD()}')
    await message_to_delete.delete()


@dp.callback_query_handler(text='EURp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Евро\nЕдиниц: 1\nКурс ЦБ РФ: {EUR()}')
    await message_to_delete.delete()


@dp.callback_query_handler(text='BRLp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Бразильский реал\nЕдиниц: 1\nКурс ЦБ РФ: {BRL()}')
    await message_to_delete.delete()


@dp.callback_query_handler(text='KRWp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Вона Республики Корея\nЕдиниц: 1000\nКурс ЦБ РФ: {KRW()}')
    await message_to_delete.delete()


@dp.callback_query_handler(text='HKDp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Гонконгский доллар\nЕдиниц: 1\nКурс ЦБ РФ: {HKD()}')
    await message_to_delete.delete()


@dp.callback_query_handler(text='AEDp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Дирхам (ОАЭ)\nЕдиниц: 1\nКурс ЦБ РФ: {AED()}')
    await message_to_delete.delete()


@dp.callback_query_handler(text='INRp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Индийская рупия\nЕдиниц: 10\nКурс ЦБ РФ: {INR()}')
    await message_to_delete.delete()


@dp.callback_query_handler(text='CNYp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Китайский юань\nЕдиниц: 1\nКурс ЦБ РФ: {CNY()}')
    await message_to_delete.delete()


@dp.callback_query_handler(text='GBPp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Фунт стерлингов Соединенного королевства\nЕдиниц: 1\nКурс ЦБ РФ: {GBP()}')
    await message_to_delete.delete()


@dp.callback_query_handler(text='JPYp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    await callback_query.message.answer(f'Японская иена\nЕдиниц: 100\nКурс ЦБ РФ: {JPY()}')
    await message_to_delete.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
