from loguru import logger

from pkg.db import create_database
from utils.set_bot_commands import set_default_commands


@logger.catch
async def on_startup(dp):
    await create_database()
    await set_default_commands(dp)


if __name__ == '__main__':
    logger.info('Начало работы бота')
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
