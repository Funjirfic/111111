from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='6006582578:AAEVLSXuuRFPbBIrBW5kqiSgKvbPdjjV91I')
dp = Dispatcher(bot, storage=MemoryStorage())


class FilmState(StatesGroup):
    first = State()
    second = State()
    third = State()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Введи любимый жанр фильма')
    await FilmState.first.set()


@dp.message_handler(state=FilmState.first)
async def first_command(message: types.Message, state: FSMContext):
    await state.update_data(fir=message.text)
    await message.answer('Ещё один')
    await FilmState.next()              # await FilmState.'название статуса'.set() -- к конкретному статусу,
                                        # а не к следующему


@dp.message_handler(state=FilmState.second)
async def second_command(message: types.Message, state: FSMContext):
    await state.update_data(sec=message.text)
    await message.answer('И ещё один')
    await FilmState.next()


@dp.message_handler(state=FilmState.third)
async def third_command(message: types.Message, state: FSMContext):
    await state.update_data(thi=message.text)
    data = await state.get_data()
    await message.answer(f"Первый: {data['fir']}\n"
                         f"Второй: {data['sec']}\n"
                         f"Третий: {data['thi']}")
    await state.finish()

# И в конце концов мы всё завершаем методом - finish()
# await state.finish()
# Данный метод очищает все состояния пользователя, а также удаляет все ранее сохраненные данные.
# Если же вам надо сбросить только состояние, воспользуйтесь:
# await state.reset_state(with_data=False)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
