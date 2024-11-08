from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text='Рассчитать')
btn2 = KeyboardButton(text='Информация')
btn3 = KeyboardButton(text='Купить')
kb.row(btn1, btn2)
kb.add(btn3)

il_kb = InlineKeyboardMarkup()
btn3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
btn4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
il_kb.row(btn3, btn4)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Витамин A', callback_data='product_buying'),
        InlineKeyboardButton(text='Витамин B', callback_data='product_buying'),
        InlineKeyboardButton(text='Витамин C', callback_data='product_buying'),
        InlineKeyboardButton(text='Витамин D', callback_data='product_buying')]
    ]
)


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=il_kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 х рост (см) - 5 х возраст (лет) + 5')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (лет):', reply_markup=ReplyKeyboardRemove())
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * float(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Вам необходимо потреблять {calories} ккал в сутки.', reply_markup=kb)
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('Files/A.png', 'rb') as img:
        await message.answer('Название: Витамин A | Описание: описание 1 | Цена: 100', reply_markup=ReplyKeyboardRemove())
        await message.answer_photo(img)
    with open('Files/B.png', 'rb') as img:
        await message.answer('Название: Витамин B | Описание: описание 2 | Цена: 200')
        await message.answer_photo(img)
    with open('Files/C.png', 'rb') as img:
        await message.answer('Название: Витамин C | Описание: описание 3 | Цена: 300')
        await message.answer_photo(img)
    with open('Files/D.png', 'rb') as img:
        await message.answer('Название: Витамин D | Описание: описание 4 | Цена: 400')
        await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=buy_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!', reply_markup=kb)
    await call.answer()



@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
