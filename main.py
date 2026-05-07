import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers.common import router as main_router

async def main():
    print(">>> БОТ ЗАПУСКАЕТСЯ ИЗ ПРАВИЛЬНОЙ ПАПКИ <<<")
    load_dotenv()
    
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        print("ОШИБКА: Токен не найден! Проверь файл .env")
        return

    bot = Bot(token=bot_token)
    dp = Dispatcher()
    
    # Подключаем роутер с кнопками
    dp.include_router(main_router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    print("🚀 БОТ ЗАПУЩЕН И ГОТОВ К РАБОТЕ")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())