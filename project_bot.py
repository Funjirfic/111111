from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from project_fun import *
from project_text import *
import time

bot = Bot(token='6156201703:AAFbJVvYks4EfX3UiyoIcdioHIfz6JUILQw', parse_mode='HTML')
dp = Dispatcher(bot)

ikb1 = InlineKeyboardMarkup(row_width=2)
i1 = InlineKeyboardButton(text='Информация',
                          callback_data='info')
i2 = InlineKeyboardButton(text='Парсер валют',
                          callback_data='parse')
i3 = InlineKeyboardButton(text='Поддержка',
                          callback_data='support')
ikb1.add(i3, i1, i2)

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
ii9 = InlineKeyboardButton(text='GBR🇬🇧',
                           callback_data='GBRp')
ii10 = InlineKeyboardButton(text='JPY🇯🇵',
                            callback_data='JPYp')
ikb2.add(ii1, ii2, ii3, ii4, ii5, ii6, ii7, ii8, ii9, ii10)


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
    time.sleep(1)
    await message_to_delete.delete()
    await callback_query.message.answer(f'Единиц: 1\nКурс ЦБ РФ: {USD()}')


@dp.callback_query_handler(text='EURp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    time.sleep(1)
    await message_to_delete.delete()
    await callback_query.message.answer(f'Единиц: 1\nКурс ЦБ РФ: {EUR()}')


@dp.callback_query_handler(text='BRLp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    time.sleep(1)
    await message_to_delete.delete()
    await callback_query.message.answer(f'Единиц: 1\nКурс ЦБ РФ: {BRL()}')


@dp.callback_query_handler(text='KRWp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    time.sleep(1)
    await message_to_delete.delete()
    await callback_query.message.answer(f'Единиц: 1000\nКурс ЦБ РФ: {KRW()}')


@dp.callback_query_handler(text='HKDp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    time.sleep(1)
    await message_to_delete.delete()
    await callback_query.message.answer(f'Единиц: 1\nКурс ЦБ РФ: {HKD()}')


@dp.callback_query_handler(text='AEDp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    time.sleep(1)
    await message_to_delete.delete()
    await callback_query.message.answer(f'Единиц: 1\nКурс ЦБ РФ: {AED()}')


@dp.callback_query_handler(text='INRp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    time.sleep(1)
    await message_to_delete.delete()
    await callback_query.message.answer(f'Единиц: 10\nКурс ЦБ РФ: {INR()}')


@dp.callback_query_handler(text='CNYp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    time.sleep(1)
    await message_to_delete.delete()
    await callback_query.message.answer(f'Единиц: 1\nКурс ЦБ РФ: {CNY()}')


@dp.callback_query_handler(text='GBRp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    time.sleep(1)
    await message_to_delete.delete()
    await callback_query.message.answer(f'Единиц: 1\nКурс ЦБ РФ: {GBR()}')


@dp.callback_query_handler(text='JPYp')
async def process_callback_parse(callback_query: types.CallbackQuery):
    await callback_query.answer()
    message_to_delete = await callback_query.message.answer('Загрузка...')
    time.sleep(1)
    await message_to_delete.delete()
    await callback_query.message.answer(f'Единиц: 100\nКурс ЦБ РФ: {JPY()}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
