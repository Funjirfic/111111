from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token='6006582578:AAEVLSXuuRFPbBIrBW5kqiSgKvbPdjjV91I')
dp = Dispatcher(bot)

ACTION = """
1 - 100р
2 - 1000р
3 - 500р
"""

MOO = """
1 - 100р
2 - 1000р
3 - 500р
"""

RPG = """
1 - 100р
2 - 1000р
3 - 500р
"""

DOS = """
Курьером - 300р
Машиной - 500р
Поездом - 1000р
Самолетом - 2000р
"""


ikb1 = InlineKeyboardMarkup(row_width=3)
i1 = InlineKeyboardButton(text='action',
                          callback_data='i1')
i2 = InlineKeyboardButton(text='mmo',
                          callback_data='i2')
i3 = InlineKeyboardButton(text='rpg',
                          callback_data='i3')
ikb1.add(i1, i2, i3)

ikb2 = InlineKeyboardMarkup(row_width=3)
in1 = InlineKeyboardButton(text='1',
                           callback_data='b1')
in2 = InlineKeyboardButton(text='2',
                           callback_data='b1')
in3 = InlineKeyboardButton(text='3',
                           callback_data='b1')
ikb2.add(in1, in2, in3)


ikb3 = InlineKeyboardMarkup(row_width=4)
inl1 = InlineKeyboardButton(text='Курьер',
                            callback_data='b2')
inl2 = InlineKeyboardButton(text='Машиной',
                            callback_data='b2')
inl3 = InlineKeyboardButton(text='Поездом',
                            callback_data='b2')
inl4 = InlineKeyboardButton(text='Самолетом',
                            callback_data='b2')
ikb3.add(inl1, inl2, inl3, inl4)


ikb4 = InlineKeyboardMarkup(row_width=1)
inli1 = InlineKeyboardButton(text='Оплатить',
                             callback_data='b3')
ikb4.add(inli1)

@dp.message_handler(commands=['start'])
async def start_com(message: types.Message):
    await message.answer('Привет, это бот продавец')
    await message.answer('Выбери жанр игры',
                         reply_markup=ikb1)


@dp.callback_query_handler(text='i1')
async def process(callback_query: types.CallbackQuery):
    await callback_query.message.answer(ACTION)
    await callback_query.message.answer('Выберите скин для покупки:',
                                        reply_markup=ikb2)


@dp.callback_query_handler(text='i2')
async def process(callback_query: types.CallbackQuery):
    await callback_query.message.answer(MOO)
    await callback_query.message.answer('Выберите скин для покупки:',
                                        reply_markup=ikb2)


@dp.callback_query_handler(text='i3')
async def process(callback_query: types.CallbackQuery):
    await callback_query.message.answer(RPG)
    await callback_query.message.answer('Выберите скин для покупки:',
                                        reply_markup=ikb2)


@dp.callback_query_handler(text='b1')
async def process(callback_query: types.CallbackQuery):
    await callback_query.message.answer(DOS)
    await callback_query.message.answer('Выберите способ доставки:',
                                        reply_markup=ikb3)


@dp.callback_query_handler(text='b2')
async def process(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Отлично, можете оплатить',
                                        reply_markup=ikb4)


@dp.callback_query_handler(text='b3')
async def process(callback_query: types.CallbackQuery):
    await callback_query.answer('Ошибка')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
