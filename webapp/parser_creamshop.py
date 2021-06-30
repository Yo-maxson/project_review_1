
import requests
from bs4 import BeautifulSoup

from webapp.model import db, Clothes

HOST= 'https://creamshop.ru' #для создания ссылки на товар

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text #если все ок, то результат страницы тут
    except(requests.RequestException, ValueError):
        return False



def get_parser_clothes():
    html = get_html("https://creamshop.ru/store/clothing/?SHOWALL_1=1")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='products-list__item') # поиск нужной карточки объекта
        #clothes = []
        for item in items:
            items = item.find('a', class_='name').get_text(strip=True)
            url = HOST + item.find('a', class_='name').get('href')
            price = item.find('span', class_='current-price').get_text(strip=True)
            size = item.find('div', class_='option-set').get_text(strip=True).split("/")
            clothes_img = HOST + item.find('div', class_='image').find('img').get('src')
            save_clothes(items,url,price,size,clothes_img)

def save_clothes(items, url, price, size, clothes_img):
    clothes_clothes = Clothes(items=items, url=url, price=price,size=size, clothes_img=clothes_img)#создание объекта и передача значение полей
    db.session.add(clothes_clothes)
    db.session.commit()
  











#Проверка создается ли список
# def get_parser_clothes(html):


#         soup = BeautifulSoup(html, 'html.parser')
#         items = soup.find_all('div', class_='products-list__item') # поиск нужной карточки объекта

#         clothes = []
#         for item in items:
#             clothes.append({ #добавление карточек товаров
#                 'items': item.find('a', class_='name').get_text(strip=True),
#                 'url': HOST + item.find('a', class_='name').get('href'),
#                 'price': item.find('span', class_='current-price').get_text(strip=True),
#                 'size':  item.find('div', class_='option-set').get_text(strip=True).split("/"),###не разделяет размеры!
#                 'clothes_img': item.find('div', class_='image').find('img').get('src')
#             })
            
#         return clothes
# if __name__=="__main__":
#         html = get_html("https://creamshop.ru/store/clothing/?SHOWALL_1=1")
#         if html:
#             n = get_parser_clothes(html)
#             print(n)
