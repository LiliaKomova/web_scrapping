#  1. Необходимо парсить страницу со свежими вакансиями
#       с поиском 'Python', города: "Москва" и "Санкт-Петербург".
#  2. Нужно выбрать те вакансии, у которых в описании
#        есть ключевые слова "Django" и "Flask".
#  3. Записать в json информацию о каждой вакансии:
#        ссылка, вилка зп, название компании и город.
import json

#  доп.: получать вакансии только с зп в долларах


"""import json
import requests
from bs4 import BeautifulSoup
from time import sleep

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0)'
                         ' Gecko/20100101 Firefox/103.0'}


def get_url():
    url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')
    card_vacancy = soup.find_all('div', class_='serp-item')

    for value in card_vacancy:
        url_vacancy = value.find('a', class_='serp-item__title').get('href')
        yield url_vacancy


vacancies = {}

for url_vacancy in get_url():
    res = requests.get(url_vacancy, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'lxml')

    data = soup.find('div', class_='row-content')
    salary = data.find('span', class_="bloko-header-section-2 "
                                      "bloko-header-section-2_lite")
    if salary is not None and 'USD' in salary:
        salary = data.find('span', class_="bloko-header-section-2 bloko-header"
                                          "-section-2_lite").text.replace('\n', '')
        title = data.find('h1', class_='bloko-header-section-1').text.replace('\n', '')
        employer = data.find('a', class_='bloko-link'
                                         ' bloko-link_kind-tertiary').text.replace('\n', '')
        city = data.find('span', attrs={
            'data-qa': 'vacancy-view-raw-address'}).text.replace('\n', '')
        description = data.find('div', class_='vacancy-description').text
        if 'django' in description.lower() \
                and 'flask' in description.lower():
            vacancies[title] = {
                'url': url_vacancy,
                'salary': salary,
                'employer': employer,
                'city': city
            }


with open('vacancies.json', 'w') as filename:
    json.dump(vacancies, filename)
"""


import json
import requests
from bs4 import BeautifulSoup


def get_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'}
    # url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


# get_url('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2')
data = get_url('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2').find_all('div', class_='serp-item')

for value in data:
    s = value.find('span', class_='bloko-header-section-3')
    if s is not None and 'USD' in s:
        url_vacancy = value.find('a', class_='serp-item__title').get('href')
        # get_url(url_vacancy)
        d = get_url(url_vacancy).find('div', class_='row-content')
        description = d.find('div', class_='g-user-content').text
        if 'django' in description.lower() and 'flask' in description.lower():
            title = d.find('div', class_='bloko-header-section-1')
            salary = d.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').text
            employer = d.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').text
            city = d.find('p', attrs={'data-qa': 'vacancy-view-location'}).text
            print(title)
            print(url_vacancy)
            print(salary)
            print(employer)
            print(city)
            print()
#             
# vacancies[title] = {
#     'url': url_vacancy,
#     'salary': salary, 
#     'employer': employer,
#     'city': city
# }
# with open('vacancies.json', 'w') as filename:
#     json.dump(vacancies, filename)

