from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




inline_btnss = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="menu", callback_data="menu"), InlineKeyboardButton(text="info", callback_data="info")],
            [InlineKeyboardButton(text="contact", callback_data="contact")]
        ]
    )