from getpass import getpass #скрывает напечатанные данные
import sys #модуль взаимодействия с сист ф-ми

from webapp import create_app
from webapp.db import db
from webapp.clothes.models import User

app = create_app()

with app.app_context():
    username = input('Введите имя пользователя:')

    if User.query.filter(User.username == username).count():
        print('Такой пользователь уже есть')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')

    if not password == password2:
        print('Пароли не одинаковые')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с id={}'.format(new_user.id))