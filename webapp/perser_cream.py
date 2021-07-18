import requests
from bs4 import BeautifulSoup
import csv

URL = "https://creamshop.ru/store/clothing/?SHOWALL_1=1"
ALL_PAGES = "?SHOWALL_1=1"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
'accept': '*/*'} #чтобы не блокировал сайт
HOST= 'https://creamshop.ru' #для создания ссылки на товар
FILE = 'clothes.csv'


def get_html(url, params=None): #принимает два аргумента, params нужны для перехода по всем страницам
    search = requests.get(url, headers=HEADERS, params=params)
    return search


def get_pages_count(html):# определение количества страниц 
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('div', class_='modern-page-navigation').find_all("a") #попытка пагинации :(
    print('size', len(pagination))
    if len(pagination) > 1:
        return len(pagination) - 1    
    else:
        return 1


def get_content(html): #создаем объект и работаем в этой ф-ии с которой будем работать
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='products-list__item') # поиск нужной карточки объекта

    clothes = []
    for item in items:
        #информация о вещи
        clothes.append({
            #добавление карточек товаров
            'items': item.find('a', class_='name').get_text(strip=True),
            'link': HOST + item.find('a', class_='name').get('href'),
            'price': item.find('span', class_='current-price').get_text(strip=True),
            'size':  item.find('div', class_='option-set').get_text(strip=True),###не разделяет размеры!
            'clothes_img': item.find('div', class_='image').find('img').get('src')
        })

    print(clothes)


def save_file(items, path): #создание упорчдоченного списка exel
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Наименование', 'Ссылка', 'Цена', 'Размер', 'Изображение']) 
        for item in items:
               writer.writerow([item['items'], item['link'], item['price'], item['size'], item['clothes_img']])


def parse(): #основная ф-я
    html = get_html(URL)
    if html.status_code == 200: #проверка на работоспособность
        clothes = []
        pages_count = get_pages_count(html.text) #тут должно быть количество страниц товаров
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} in {pages_count}...' )# прогресс парсинга страниц
            html = get_html(URL, params={'?PAGEN_1': page})# контент для каждой страницы
            clothes.extend(get_content(html.text))
            save_file(clothes, FILE)
        print(f'Имеется {len(clothes)} товаров')
    else:
        print('Error')


parse()
