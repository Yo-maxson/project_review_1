import requests

from webapp.db import db
from webapp.clothes.models import Clothes


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
'accept': '*/*'} #чтобы не блокировал сайт
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        '#если все ок, то результат страницы тут'
        return result.text
    except(requests.RequestException, ValueError):
        print('Error')
        return False


def save_clothes(items, url, price, size, clothes_img):
    Clothes_exists = Clothes.query.filter(Clothes.url == url).count()
    # проверка есть ли вещь с таким url
    if not Clothes_exists:
        '#создание объекта и передача значение полей'
        clothes_clothes = Clothes(items=items, url=url, price=price, size=size, clothes_img=clothes_img)
        db.session.add(clothes_clothes)
        db.session.commit()
