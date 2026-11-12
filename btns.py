from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_btns = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="menu")],
        [KeyboardButton(text="help")],
        [KeyboardButton(text="contact"), KeyboardButton(text="about")]
    ], resize_keyboard=True
)