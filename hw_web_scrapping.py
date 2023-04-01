#  1. Необходимо парсить страницу со свежими вакансиями
#  с поиском 'Python'и города "Москва" и "Санкт-Петербург".
#  Эти параметры задаются по ссылке.
#  2. Нужно выбрать те вакансии, у которых в описании
#  есть ключевые слова "Django" и "Flask".
#  3. Записать в json информацию о каждой вакансии
#  - ссылка,вилка зп, название компании и город.

#  доп.: получать вакансии только с зп в долларах

import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint


url = 'https://api.hh.ru/vacancies'
params = {
    'text': 'python',
    'area': [1, 2]
}

response = requests.get(url, params=params)
data = response.json()
tag = ['Django', 'Flask']
vacancies = {}
vacancies['vacancy'] = []

for value in data['items']:
    if value['salary'] is not None and value['salary']['currency'] == 'USD':
        vacancies['vacancy'].append(
            {
                'name': value['name'],
                'url': value['alternate_url'],
                'salary': {'from': value['salary']['from'],
                           'to':value['salary']['to']},
                'employer': value['employer']['name'],
                'city': value['area']['name']
            })
    pprint(vacancies['vacancy'])
# with open('data.json', 'w') as filename:
#     json.dump(vacancies, filename)