import json
import requests
from bs4 import BeautifulSoup


HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'}
url = f'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.find_all('div', class_='serp-item')

vacancies = {}

for value in data:
    s = value.find('span', class_='bloko-header-section-3')
    if s is not None and 'USD' in s:
        salary = value.find('span', class_='bloko-header-section-3').text.replace(r'\u202f', ' ')
        title = value.find('a', class_='serp-item__title').text
        employer = value.find('a', class_='bloko-link bloko-link_kind-tertiary').text
        city = value.find('div', attrs={'data-qa': 'vacancy-serp__vacancy-address'}).text
        url_vacancy = value.find('a', class_='serp-item__title').get('href')

        r = requests.get(url_vacancy,headers=HEADERS)
        s = BeautifulSoup(r.text, 'lxml')

        description = s.find('div', class_='g-user-content').text.strip()
        if 'django' in description.lower() and 'flask' in description.lower():
            vacancies[title] = {
                'url': url_vacancy,
                'salary': salary,
                'employer': employer,
                'city': city
            }

with open('vacancies.json', 'w') as filename:
    json.dump(vacancies, filename)