from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def make_row_keyboard(cells: dict[str, str]) -> InlineKeyboardMarkup:
    """
    Creates inline-markup with row-buttons
    :param cells: dictionary of buttons descriptions as values and callback as keys
    :return: inline markup object
    """
    builder = InlineKeyboardBuilder()
    buttons = [
            InlineKeyboardButton(text=name, callback_data=call_back) for call_back, name in cells.items()
            ]
    builder.add(*buttons)
    builder.adjust(1, 1)
    return builder.as_markup()


def make_reply_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Creates reply-markup with row-buttons with cancel command
    :param items: list of buttons
    :return: reply markup object
    """
    builder = ReplyKeyboardBuilder()
    buttons = [KeyboardButton(text=item) for item in items]
    builder.add(*buttons)
    builder.add(KeyboardButton(text='cancel'))
    builder.adjust(1, 1)
    return builder.as_markup()

