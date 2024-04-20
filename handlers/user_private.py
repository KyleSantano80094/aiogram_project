import random
import requests

from aiogram.filters import CommandStart, Command, or_f, StateFilter
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InputMediaPhoto, FSInputFile

from filters.chat_types import ChatTypeFilter
from kbds import inline

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private', 'group', 'supergroup']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    file_path = 'C:/Users/xxx/Downloads/games.jpg'
    await message.answer_photo(photo=FSInputFile(path=file_path),
                               caption='Привет, я виртуальный помощник', reply_markup=inline.links_kb)


@user_private_router.callback_query(F.data == 'menu')
async def menu_cmd(callback: types.CallbackQuery):
    await callback.answer('')
    photo_menu = InputMediaPhoto(
        media='https://t4.ftcdn.net/jpg/04/42/21/53/360_F_442215355_AjiR6ogucq3vPzjFAAEfwbPXYGqYVAap.jpg',
        caption='Лень доделывать 😢 (to be continue..)'
    )
    await callback.message.edit_media(media=photo_menu, reply_markup=inline.get_callback_btns(
        btns={
            "Назад": "back_7",
        },
        sizes=(1,)
    ))


@user_private_router.callback_query(F.data == "about")
async def about_cmd(callback: types.CallbackQuery):
    await callback.answer('')
    photo_0 = InputMediaPhoto(media='https://i.ibb.co/Zxk23Bp/IMG-20240415-182337-012.jpg',
                              caption='Универсальный бот со множество функциями')
    await callback.message.edit_media(media=photo_0, reply_markup=inline.back_kb)


@user_private_router.callback_query(F.data == "game options")
async def payment_cmd(callback: types.CallbackQuery):
    await callback.answer('')
    photo_1 = InputMediaPhoto(media='https://i.ibb.co/DgTc6ts/menu-game.jpg', caption='Выбери игру 🌈')
    await callback.message.edit_media(media=photo_1, reply_markup=inline.games_kb)


@user_private_router.callback_query(or_f(F.data == 'game_2', F.data == 'game_3'))
async def add_games(callback: types.CallbackQuery):
    await callback.answer('')
    photo_2 = InputMediaPhoto(media='https://i.ibb.co/0Ct1XVJ/soon.jpg', caption='В процессе 💬')
    await callback.message.edit_media(media=photo_2, reply_markup=inline.get_callback_btns(
        btns={
            "Назад": "back_4",
        },
        sizes=(1,)
    ))


@user_private_router.callback_query(F.data == 'other')
async def other_cmd(callback: types.CallbackQuery):
    await callback.answer('')
    photo_3 = InputMediaPhoto(media='https://i.ibb.co/3YsGgmT/other.jpg')
    await callback.message.edit_media(media=photo_3, reply_markup=inline.other_kb)


@user_private_router.callback_query(F.data == 'my_urls')
async def other_cmd(callback: types.CallbackQuery):
    await callback.answer('')
    photo_4 = InputMediaPhoto(media='https://i.ibb.co/3YsGgmT/other.jpg', caption='Выбери действие :)')
    await callback.message.edit_media(media=photo_4, reply_markup=inline.url_kb)


@user_private_router.callback_query(F.data == 'bio')
async def other_cmd(callback: types.CallbackQuery):
    await callback.answer('')
    photo_5 = InputMediaPhoto(media='https://i.ibb.co/3YsGgmT/other.jpg', caption='Чунга чанга ебаная 😎')
    await callback.message.edit_media(media=photo_5, reply_markup=inline.get_callback_btns(
        btns={
            "Назад": "back_5",
        },
        sizes=(1,)
    ))


@user_private_router.callback_query(F.data == 'weather')
async def other_cmd(callback: types.CallbackQuery):
    await callback.answer('')
    photo_6 = InputMediaPhoto(media='https://i.ibb.co/3YsGgmT/other.jpg', caption='Напиши свой город')
    await callback.message.edit_media(media=photo_6, reply_markup=inline.get_callback_btns(
        btns={
            'Назад': 'back_6',
        },
        sizes=(1,)
    ))


@user_private_router.message(F.text)
async def get_weather(message: types.Message):
    city = message.text
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
        weather_data = requests.get(url).json()

        temperature = weather_data['main']['temp']
        temperature_feels = weather_data['main']['feels_like']
        wind_speed = weather_data['wind']['speed']
        cloud_cover = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        await message.answer(f'Температура воздуха: {temperature}°C\n'
                             f'Ощущается как: {temperature_feels}°C\n'
                             f'Ветер: {wind_speed} м/с\n'
                             f'Облачность: {cloud_cover}\n'
                             f'Влажность: {humidity}%')
    except KeyError:
        await message.answer(f'Не удалось определить город: {city}')


@user_private_router.callback_query(or_f(F.data == 'back_1', F.data == 'back_2', F.data == 'back_3',
                                         F.data == 'back_7'))
async def back_menu(callback: types.CallbackQuery):
    photo_7 = InputMediaPhoto(
        media='https://t4.ftcdn.net/jpg/04/42/21/53/360_F_442215355_AjiR6ogucq3vPzjFAAEfwbPXYGqYVAap.jpg',
        caption='Вы вернулись в главное меню!')
    await callback.message.edit_media(media=photo_7, reply_markup=inline.links_kb)


@user_private_router.callback_query(F.data == 'back_4')
async def back_2_cmd(callback: types.CallbackQuery):
    await callback.answer('')
    photo_8 = InputMediaPhoto(media='https://i.ibb.co/DgTc6ts/menu-game.jpg', caption='Выбери игру 🌈')
    await callback.message.edit_media(media=photo_8, reply_markup=inline.games_kb)


@user_private_router.callback_query(or_f(F.data == 'back_5', F.data == 'back_6'))
async def other_cmd(callback: types.CallbackQuery):
    await callback.answer('')
    photo_9 = InputMediaPhoto(media='https://i.ibb.co/3YsGgmT/other.jpg')
    await callback.message.edit_media(media=photo_9, reply_markup=inline.other_kb)


# Код ниже для машины состояний (FSM)
class Games(StatesGroup):
    data_input = State()

    texts = {
        'Games:data_input': 'Введите число заново:',
    }


@user_private_router.callback_query(StateFilter(None),
                                    or_f(F.data == 'game_1', F.data == 'again'))
async def add_games(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer('')
    await callback.message.answer(
        'Угадай число от 1 до 2', reply_markup=inline.game_1)
    await state.set_state(Games.data_input)


# Хендлер отмены и сброса состояния должен быть всегда именно здесь,
# после того как только встали в состояние номер 1 (элементарная очередность фильтров)
@user_private_router.callback_query(StateFilter('*'), F.data == "cancel")
async def cancel_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.answer('')
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await callback.message.edit_text("Действия отменены")


# Вернутся на шаг назад (на прошлое состояние)
@user_private_router.message(StateFilter('*'), Command("назад"))
@user_private_router.message(StateFilter('*'), F.text.casefold() == "назад")
async def back_step_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()

    if current_state == Games.data_input:
        await message.answer('Предыдущего шага нет, или введите название товара или напишите "отмена"')
        return

    previous = None
    for step in Games.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f"Ок, вы вернулись к прошлому шагу \n {Games.texts[previous.state]}")
            return
        previous = step


@user_private_router.callback_query(Games.data_input, F.data)
async def add_data_output(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(data_input=callback.data)
    random_number = random.randint(1, 2)
    data = await state.get_data()
    # await message.answer(str(data))
    if int(data['data_input']) == random_number:
        await callback.message.edit_text('Вы угадали', reply_markup=inline.again_kb)
    else:
        await callback.message.edit_text("Вы не угадали :(")
        await callback.message.edit_text(f"Было загадано число {random_number}", reply_markup=inline.again_kb)

    await state.clear()
