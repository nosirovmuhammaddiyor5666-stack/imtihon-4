
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

async def start_bottons():
    markab = ReplyKeyboardMarkup(
        keyboard= [
            [
                KeyboardButton(text="Kurslar"),
                KeyboardButton(text="Kursga yozilish")
            ],
            [
                KeyboardButton(text="Markaz haqida"),
                KeyboardButton(text="Aloqa")
            ],
            [
                KeyboardButton(text="Bekor qilish")
            ]

        ],
        resize_keyboard=True
    )
    return markab

async def Contact_yu():
    markab = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Contact yuborish",request_contact=True),
                KeyboardButton(text="Bekor qilish")
            ]
        ],
        resize_keyboard=True
    )
    return markab


async def Kurslar_buttons():
    I_markab = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Python",callback_data="Pyt"),
                InlineKeyboardButton(text="Web dasturlash",callback_data="Web")
            ],
            [
                InlineKeyboardButton(text="Frontend",callback_data="Fron"),
                InlineKeyboardButton(text="Grafik dizayn",callback_data="Grafik")
            ],

        ]
    )
    return I_markab


async def Kurslar_buttons2():
    I_markab = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Python",callback_data="Python"),
                InlineKeyboardButton(text="Web dasturlash",callback_data="Web dasturlash")
            ],
            [
                InlineKeyboardButton(text="Frontend",callback_data="Frontend"),
                InlineKeyboardButton(text="Grafik dizayn",callback_data="Grafik dizayn")
            ],

        ]
    )
    return I_markab

async def Back():
    markab = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Bekor qilish")
            ]
        ],
        resize_keyboard=True
    )
    return markab

