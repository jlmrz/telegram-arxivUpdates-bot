from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message) -> None:
    await message.answer(
        'Hello! This bot is designed to send updates from arxive.org.\n' +
        'Use /set command to set your preferences: Physics branch and area, if any. ' +
        'If you have already saved your preferences, use /send_update to get the latest articles in the selected area.'
    )


@router.message(Command('cancel'))
@router.message(Text(text='cancel'))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Action canceled.",
        reply_markup=ReplyKeyboardRemove()
    )
