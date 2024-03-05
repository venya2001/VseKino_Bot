import asyncio
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import token_bot
from app.handlers.user import start
from app.handlers.admin import start_admin, channels, statistic, newsletter, permissions
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")


TOKEN = token_bot
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher()

dp.include_routers(start.router,
                   channels.pub_router,
                   channels.form_router,
                   start_admin.adm_router,
                   statistic.stat_router,
                   newsletter.post_router,
                   permissions.per_router)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())