import string
import os
import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/'

num = int(input())
rate = input()

for i in range(1, num + 1):
    page = f'page-{i}.html'
    response = requests.get(url + page)

    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    saved_books = []
    directory = f'Page_{i}'
    os.makedirs(directory, exist_ok=True)
    os.chdir(directory)
    for book in books:
        rating = book.find('p').get('class')[1]
        if rating != rate:
            continue
        book_info = book.find('h3').find('a')

        title = book_info.get('title')
        for punc in string.punctuation:
            title = title.replace(punc, '')
        title = title.replace(' ', '_') + ".txt"

        link = book_info.get('href')
        response_description = requests.get(url + link)
        response_description.encoding = 'utf-8'
        soup = BeautifulSoup(response_description.text, 'html.parser')

        description = soup.find('div', id='product_description').find_next_sibling().get_text(strip=True)

        with open(title, 'w', encoding='utf-8') as f:
            f.write(description)
            saved_books.append(title)
    os.chdir('..')

print('Saved all books.')