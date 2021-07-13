from webapp.clothes.models import Clothes
from bs4 import BeautifulSoup

from webapp.db import db
from webapp.clothes.models import Clothes
from webapp.clothes.parsers.utils import get_html, save_clothes

HOST = 'https://creamshop.ru'


def get_clothes_snippets():
    html = get_html("https://creamshop.ru/store/clothing/?SHOWALL_1=1")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        '# поиск нужной карточки объекта'
        items = soup.find_all('div', class_='products-list__item')
        '#clothes = []'
        for item in items:
            items = item.find('a', class_='name').get_text(strip=True)
            url = HOST + item.find('a', class_='name').get('href')
            price = item.find('span', class_='current-price').get_text(strip=True)
            all_sizes = item.find('div', class_='option-set').find_all('label')
            size_list = []
            for size in all_sizes:
                size = size.get_text(strip=True)
                size_list.append(size)
            size = " ".join(size_list)
            clothes_img = HOST + item.find('div', class_='image').find('img').get('src')
            save_clothes(items, url, price, size, clothes_img)


def get_clothes_discription():
    clothes_without_text = Clothes.query.filter(Clothes.text.is_(None))
    for clothes in clothes_without_text:
        html = get_html(clothes.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            clothe_discription = soup.find('div', class_='product-tabs-content').decode_contents()
            print(clothe_discription)
            if clothe_discription:
                clothes.text = clothe_discription
                db.session.add(clothes)
                db.session.commit()
