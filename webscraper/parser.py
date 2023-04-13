import requests
import logging
from bs4 import BeautifulSoup

from .website_data import FIELDS, AVAILABLE_BRANCHES_PH
from pandas import isna


def get_articles(branch: str, field=None) -> str:

    if not isna(field) and (field is not None):
        field = FIELDS[branch][field]

    branch = AVAILABLE_BRANCHES_PH[branch]
    branch = branch + '.' + field

    base_url = 'https://arxiv.org/list/'

    url = base_url + branch + '/new'
    headers = {'User-Agent': 'Generic user agent'}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    try:
        articles = soup.find_all('div', class_='meta')
        output = []

        for article in articles:
            title = article.find('div', class_='list-title mathjax').get_text().strip().removeprefix('Title: ')
            authors = article.find('div', class_='list-authors').get_text().removeprefix('\nAuthors:\n').strip()

            string = ' '.join(['<b>Title:</b> ' + title, '\n Authors:',   '<i>' + authors.replace('\n', ' ') + '</i>'])
            output.append(string)

        message_text = '\n\n'.join(output)
        return message_text
    except Exception as e:
        info = 'Something went wrong. Please try again later.'
        logging.exception(f'Error occurred while parsing data: {e}')
        return info
