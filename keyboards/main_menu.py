from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💅 Услуги и цены"), KeyboardButton(text="📅 Записаться")],
        [KeyboardButton(text="📍 Контакты"), KeyboardButton(text="💎 О салоне")]
    ],
    resize_keyboard=True
)