import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

# Вставь свой токен бота
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def handle_message(message: Message):
    # Игнорируем сообщения от ботов
    if message.from_user.is_bot:
        return

    # Игнорируем команды
    if message.text.startswith("/"):
        return

    # Преобразуем сообщение в список слов (в нижнем регистре)
    words = message.text.lower().split()

    # Проверяем наличие отдельного слова "да"
    if "да" in words:
        await message.reply("пизда")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
