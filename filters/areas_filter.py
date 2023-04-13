from aiogram.filters import BaseFilter
from aiogram.types import Message
from webscraper.website_data import FIELDS


class AreasFilter(BaseFilter):
    def __init__(self) -> None:
        self.available_areas = [val for out_key in FIELDS.keys() for val in FIELDS[out_key].keys()]

    async def __call__(self, message: Message) -> bool:
        choice = message.text
        return choice in self.available_areas
