from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.types.web_app_info import WebAppInfo
keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📱 Iltimos Telefon raqamni yuboring", request_contact=True)]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
menu_keys = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🛒 Buyurtma Berish"), KeyboardButton(text="🛍️ Mening buyurtmalarim")],
                [KeyboardButton(text="💰 Aksiyalar")],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )

location_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Lokatsiyamni yuborish", request_location=True)],
        [KeyboardButton(text="👈 Ortga")],

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

web_app_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Web app ni ochish", web_app=WebAppInfo(url="https://fastfood-lq3i.onrender.com/"))],
        [KeyboardButton(text="👈 Ortga")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
