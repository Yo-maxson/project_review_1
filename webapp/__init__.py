from flask import Flask, blueprints, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required
from flask_migrate import Migrate

from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.clothes.views import blueprint as clothes_blueprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.weather import weather_by_city


def create_app():
    app = Flask(__name__)
    '#Используем файл конфигурации'
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(clothes_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app

# запуск сервера:
# в терминале --> export FLASK_APP=__init__.py
# set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

# pip freeze покажет что установлено
# pip freeze > requirements.txt перезапись в файл

# export FLASK_APP=webapp && flask db init создание папки миграций

# move webapp.db webapp.db.old переименовывание webapp

# set FLASK_APP=webapp && flask db migrate -m "users and clothes tables" миграция

# ./run.bat запуск приложения

#cygwin остановить команду
