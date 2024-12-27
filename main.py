from aiogram import Bot, Dispatcher
from complaint_bot.config import BOT_TOKEN
from complaint_bot.database import create_table
from complaint_bot import setup_routers

async def main():
   create_table()
   bot = Bot(token=BOT_TOKEN)
   dp = Dispatcher()
   dp.include_router(setup_routers())

   print("\nБот успешно запущен!")
   await dp.start_polling(bot)

if __name__ == "__main__":
   import asyncio
   asyncio.run(main())
