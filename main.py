import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import token_bot
from app.handlers.user import start
from app.handlers.admin import (start_admin,
                                channels,
                                statistic,
                                newsletter,
                                permissions)
from app.utils import search_film
from app.handlers.user import category
from aiogram.client.default import DefaultBotProperties

TOKEN = token_bot
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

dp.include_routers(start.router,
                   start_admin.adm_router,
                   permissions.per_router,
                   statistic.stat_router,
                   channels.pub_router,
                   channels.form_router,
                   newsletter.post_router,
                   search_film.cdn_rou,
                   category.category_router)


async def main() -> None:
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

