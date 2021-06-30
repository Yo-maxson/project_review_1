from flask import Flask, render_template

from webapp.model import db
from webapp.parser_creamshop import get_parser_clothes
from webapp.weather import weather_by_city

def create_app():
    app = Flask(__name__)
    #Используем файл конфигурации
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index(): # функция передачи данных в шаблон html
        title = 'Как носится?'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        clothes_list = get_parser_clothes()
        return render_template('index.html', page_title=title, weather=weather, clothes_list = clothes_list)

    return app
    

#запуск сервера:
# в терминале export FLASK_APP=__init__.py
# set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run