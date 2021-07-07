from flask import Flask, render_template

from webapp.forms import LoginForm
from webapp.model import db, Clothes
from webapp.weather import weather_by_city


def create_app():
    app = Flask(__name__)
    '#Используем файл конфигурации'
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    # функция передачи данных в шаблон html
    def index():
        title = 'Как носится?'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        clothes_list = Clothes.query.all()
        '#.order_by(Clothes.items.desc()).all()'
        return render_template('index.html', page_title=title, weather=weather, clothes_list=clothes_list)

    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app


#запуск сервера:
# в терминале export FLASK_APP=__init__.py
# set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run