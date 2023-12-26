from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher import filters
from aiogram.types import BotCommand, BotCommandScopeDefault, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import InputFile


bot = Bot(token='6006582578:AAEVLSXuuRFPbBIrBW5kqiSgKvbPdjjV91I')
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен')


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(commands=[BotCommand('start', 'Запуск и обновление бота'),
                                               BotCommand('help', 'Помощь'),
                                               BotCommand('lol', 'LOL'),
                                               BotCommand('inline', 'Инлайн клавиатура'),
                                               BotCommand('rm', 'Убрать клавиатуру'), ]
                                     , scope=BotCommandScopeDefault())


kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton('/lol')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/inline')
b4 = KeyboardButton('/location', request_location=True)
b5 = KeyboardButton('/rm')
kb.add(b1).insert(b2).insert(b3).insert(b4).insert(b5)

ikb = InlineKeyboardMarkup(row_width=2)
i1 = InlineKeyboardButton(text='YouTube',
                          url='https://www.youtube.com')
i2 = InlineKeyboardButton(text='Twitch',
                          url='https://www.twitch.tv')
i3 = InlineKeyboardButton(text='but1',
                          callback_data='button1')
ikb.add(i1, i2, i3)


@dp.message_handler(commands=['photoo'])
async def send_photo(message: types.Message):
    photo = InputFile('SCHProjct/haha.png')
    await message.answer_photo(photo)
    docum = InputFile('SCHProjct/dada.docx')
    await message.answer_document(docum)


    #photo = open('h1.png', 'rb')
    #await bot.send_photo(chat_id=message.chat.id, photo=photo)

    #photo = InputFile("PycharmProjects\Telegram_bot/12.png")
    #await bot.send_photo(chat_id=message.chat.id, photo=photo)         photo = open('photo.png', 'rb')  await call.answer_photo(photo, caption="caption")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Ты кто такой!?',
                         reply_markup=kb)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer('Крч я типа эхо бот')
    await message.delete()


@dp.message_handler(commands=['inline'])
async def process_help_command(message: types.Message):
    await message.answer('Полезные ссылочки',
                         reply_markup=ikb)


@dp.message_handler(commands=['location'])
async def message_for_start(message: types.Message):
    await message.answer('location')


@dp.callback_query_handler(text='button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Нажал кнопку')
    await callback_query.answer()


@dp.message_handler(commands=['lol'])
async def process_start_command(message: types.Message):
    await message.answer('lololololoolololoo')


@dp.message_handler(commands=['rm'])
async def process_start_command(message: types.Message):
    await message.answer('Клавиатура убрана',
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(filters.Text(contains='привет', ignore_case=True))
async def text_example(message: types.Message):
    await message.answer('Здаров')


@dp.message_handler(text='ку')
async def process_start_command(message: types.Message):
    await message.answer('<em>Ку</em>', parse_mode='HTML')


@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


@dp.message_handler(content_types=['photo'])
async def echo_message(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)


@dp.message_handler(content_types=['animation'])
async def echo_message(message: types.Message):
    await message.answer_animation(message.animation.file_id)


@dp.message_handler(content_types=['sticker'])
async def echo_message(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
