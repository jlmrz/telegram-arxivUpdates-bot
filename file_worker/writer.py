import csv
import logging

import pandas as pd


FIELDNAMES = ['id', 'subject', 'branch', 'area']
CSV_FILE_NAME = './data/users_data.csv'
ERROR_MESSAGE = 'Something went wrong. Please try again later.'


def save_user_choice(user_id: int, branch: str, area: str = None) -> str:
    if check_uniqueness(user_id):
        msg = save_data(user_id, branch=branch, areas=area)
    else:
        msg = 'You have saved your choice before, but it will be updated. \n\n<b>Result:</b>\n'
        update_data_(user_id, branch, name='branch')
        msg += update_data_(user_id, area, name='area')
    return msg


def save_data(user_id: int, branch: str, areas: str = None) -> str:
    try:
        with open(CSV_FILE_NAME, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writerow({
                'id': user_id,
                'subject': 'Physics',
                'branch': branch,
                'areas': areas
            })
            return 'Your choice is saved.'
    except IOError as e:
        logging.exception(f'Error occurred while writing to file: {e}')
        return ERROR_MESSAGE


def update_data_(user_id: int, new_data: str, name: str) -> str:
    try:
        users_df = pd.read_csv(CSV_FILE_NAME, index_col='id')
        users_df.at[user_id, name] = new_data
        users_df.to_csv(CSV_FILE_NAME)
        return 'Your data is successfully updated.'
    except Exception as e:
        logging.exception(f'Error occurred while writing to file: {e}')
        return ERROR_MESSAGE


def check_uniqueness(id_to_check: int) -> bool:
    """
    Method checks if there is user with given id in the file.
    id_to_check: user's id
    returns: True if there is NO user with given id, False otherwise.
    """
    users_id = pd.read_csv(CSV_FILE_NAME, usecols=['id'])
    return not (id_to_check in users_id.values)


def get_data(user_id: int) -> dict[str, str]:
    users_df = pd.read_csv(CSV_FILE_NAME, index_col='id')
    user_data = users_df.loc[[user_id]]
    return user_data.to_dict(orient='index')[user_id]
