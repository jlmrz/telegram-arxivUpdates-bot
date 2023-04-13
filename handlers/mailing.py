from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from file_worker.writer import get_data
from webscraper import get_articles

router = Router()


@router.message(Command('send_update'))
async def send_update(message: Message) -> None:
    user_data = get_data(message.from_user.id)
    articles = get_articles(branch=user_data['branch'], field=user_data['area'])
    await message.answer('Here is an update on chosen area.')
    for article in articles.split('\n\n'):
        await message.answer(article)
    await message.answer('That\'s all for today. ')
