from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_callback_btns(
        *,
        btns: dict[str, str],
        sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()

    for text, data in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))

    return keyboard.adjust(*sizes).as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Меню", callback_data='menu'),
            InlineKeyboardButton(text="О нас", callback_data='about'),
        ],
        [
            InlineKeyboardButton(text="Варианты игр", callback_data='game options'),
            InlineKeyboardButton(text="Прочее", callback_data='other'),
        ]
    ],
)

games_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Игра 1", callback_data='game_1'),
            InlineKeyboardButton(text="Игра 2", callback_data='game_2'),
        ],
        [
            InlineKeyboardButton(text="Игра 3", callback_data='game_3'),
            InlineKeyboardButton(text="Назад", callback_data='back_1'),
        ]
    ],
)

# games = ['Игра 1', 'Игра 2', 'Игра 3', 'Назад']
#
#
# async def inline_games():
#     keyboard = InlineKeyboardBuilder()
#     for game in games:
#         keyboard.add(InlineKeyboardButton(text=game, callback_data=f'{games}'))
#     return keyboard.adjust(2).as_markup()


other_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Мои ссылки", callback_data='my_urls'),
            InlineKeyboardButton(text="Погода", callback_data='weather'),
        ],
        [
            InlineKeyboardButton(text="Биография", callback_data='bio'),
            InlineKeyboardButton(text="Назад", callback_data='back_3'),
        ]
    ],
)

back_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='back_2'),
        ]
    ],
)

game_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data='1'),
            InlineKeyboardButton(text="2", callback_data='2'),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='back_3'),
            InlineKeyboardButton(text="Отмена", callback_data='cancel'),
        ]
    ],
)

again_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Еще', callback_data='again'),
        ]
    ],
)

url_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/channel/UCzrWoM2WyVSDCMQzNBic25A"),
            InlineKeyboardButton(text="Telegram", url="t.me/nenocok")
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back_5')
        ]
    ]
)
