import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from btns import *

TOKEN = ("8809466266:AAGRfkX8dpRDiu88fqH1zAHmOddJehNcmXA")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=menu_btns)


@dp.message(F.text)
async def get_info(message: Message):
    matn = message.text.lower()
    if "menu" in matn:
        await message.answer(f"""
    👋 Assalomu alaykum! Botimizga xush kelibsiz!

📋 **Menu bo‘limi**

Quyidagi bo‘limlardan o‘zingizga keraklisini tanlang:

🔹 🏠 Bosh sahifa
🔹 ℹ️ Biz haqimizda
🔹 📞 Bog‘lanish
🔹 ❓ Yordam
🔹 ⚙️ Sozlamalar

Kerakli bo‘lim nomini yozing yoki menyudan tanlang. 😊

✨ Sizga yordam berishdan mamnunmiz!
""")
    elif "help" in matn:
        await message.answer(f"""
👋 **Yordam bo‘limiga xush kelibsiz!**

🤖 Botdan foydalanish bo‘yicha qisqacha qo‘llanma:

📋 **Menu** — bot menyusini ko‘rish.
ℹ️ **Info** — bot haqida ma’lumot olish.
❓ **Help** — yordam va ko‘rsatmalar olish.
📞 **Contact** — administrator bilan bog‘lanish.

💡 Agar botdan foydalanishda muammoga duch kelsangiz, administratorga murojaat qiling.

✅ Botimizdan foydalanganingiz uchun rahmat!
""")
    elif "contact" in matn:
        await message.answer(f"""
📞 **Biz bilan bog‘lanish**

Assalomu alaykum! 😊

Agar savollaringiz bo‘lsa yoki yordam kerak bo‘lsa, biz bilan bog‘lanishingiz mumkin.

📩 **Administrator:** @username

💬 Taklif va murojaatlaringizni bizga yuboring. Sizga imkon qadar tezroq javob beramiz!

🤝 Bizni tanlaganingiz uchun rahmat!
""")
    elif "about" in matn:
        await message.answer(f"""ℹ️ **Bot haqida**

Assalomu alaykum! 👋 Botimizga xush kelibsiz!

🤖 Ushbu bot foydalanuvchilarga qulay va tezkor xizmat ko‘rsatish uchun yaratilgan.

✨ **Bot imkoniyatlari:**
📋 Menu — asosiy menyuni ko‘rish.
❓ Help — yordam olish.
📞 Contact — administrator bilan bog‘lanish.
ℹ️ About — bot haqida ma’lumot olish.

🎯 Maqsadimiz — sizga qulay va sifatli xizmat ko‘rsatish!

❤️ Botimizdan foydalanganingiz uchun rahmat!
""")
    else:
        await message.answer(f"Kechirasiz bunday xizmat mavjud emas!!!")
    

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

print("working...")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())