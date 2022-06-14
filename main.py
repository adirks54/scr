import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
url = 'https://habr.com/ru/all/'

HEADERS = Headers(os="win", headers=True).generate()
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

req = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(req.text, 'html.parser')
arts = soup.find_all('article', class_='tm-articles-list__item')

for art in arts:
    date = art.find('time').text
    title = art.find('a', class_='tm-article-snippet__title-link').find('span').text
    urls = art.find('a', class_='tm-article-snippet__title-link').attrs.get('href')
    prev_text =art.find('div', class_='tm-article-body tm-article-snippet__lead').text

    for key in KEYWORDS:
        if (key.lower() in title.lower()) or (key.lower() in prev_text.lower()):
            print(f'Дата: {date} - Заголовок: {title} - Ссылка: {url}')



