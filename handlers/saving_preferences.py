from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from filters.areas_filter import AreasFilter
from keyboards.kb_subjects import make_reply_keyboard
from file_worker.writer import save_user_choice, get_data
from webscraper.website_data import FIELDS

AVAILABLE_BRANCHES_PH = [
    'Astrophysics',
    'Condensed Matter',
    'Quantum Physics',
    'General Relativity and Quantum Cosmology',
    'High Energy Physics - Experiment',
    'Mathematical Physics',
    'Nonlinear Sciences',
    'Physics',
    'Nuclear Theory'
]

router = Router()


class SetPreferences(StatesGroup):
    subject = State()
    branch = State()
    areas = State()


@router.message(Command('set'))
async def start_setting(message: Message, state: FSMContext) -> None:
    reply_markup = make_reply_keyboard(AVAILABLE_BRANCHES_PH)
    await message.answer('Please, choose branch of Physics:', reply_markup=reply_markup)
    await state.set_state(SetPreferences.branch)


@router.message(SetPreferences.branch, F.text.in_(AVAILABLE_BRANCHES_PH))
async def save_branch_choice(message: Message,  state: FSMContext) -> None:
    branch_choice = message.text
    await state.update_data(branch=branch_choice)

    if branch_choice in FIELDS.keys():
        await state.set_state(SetPreferences.areas)
        reply_markup = make_reply_keyboard(FIELDS[branch_choice].keys())
        msg = get_area_message(branch_choice)
        await message.answer(text=msg, reply_markup=reply_markup)
    else:
        if_succeed = save_user_choice(message.from_user.id, branch=branch_choice)
        await message.answer(text=if_succeed, reply_markup=ReplyKeyboardRemove())
        await state.clear()


@router.message(SetPreferences.branch)
async def can_not_save_branch(message: Message) -> None:
    reply_markup = make_reply_keyboard(AVAILABLE_BRANCHES_PH)
    available_branches = ',\n'.join(AVAILABLE_BRANCHES_PH)
    await message.answer('The specified branch is not in the list of available branches. ' +
                         'Please choose from <b>following branches</b>:\n\n' +
                         available_branches, reply_markup=reply_markup)


@router.message(SetPreferences.areas, AreasFilter())
async def save_areas_choice(message: Message, state: FSMContext) -> None:
    branch_choice = await state.get_data()
    await state.clear()

    info_message = save_user_choice(message.from_user.id, branch=branch_choice['branch'], area=message.text)
    await message.answer(info_message, reply_markup=ReplyKeyboardRemove())

    new_data = get_data(message.from_user.id)
    info_message = '\n'.join([f'{key}: {data}' for key, data in new_data.items()])
    await message.answer('Please check correctness of new data:\n' + info_message.replace('nan', '-'))


@router.message(SetPreferences.areas)
async def can_not_save_areas(message: Message, state: FSMContext) -> None:
    branch_choice = await state.get_data()
    branch_choice = branch_choice['branch']

    available_areas = ',\n'.join([key for key in FIELDS[branch_choice].values()])
    msg = 'The specified areas are not in the list of available areas.\n ' +\
          'Please choose from:\n\n ' + available_areas

    reply_markup = make_reply_keyboard(AVAILABLE_BRANCHES_PH)
    await message.answer(msg, reply_markup=reply_markup)


def get_area_message(category: str) -> str:
    areas = '\n'.join([f'{area}' for area in FIELDS[category].keys()])
    return (
        'This area of physics is very broad. '
        'Please specify your own areas of interest.\n\n'
        f'<b>Available areas of {category}</b>:\n\n{areas}\n'
    )
