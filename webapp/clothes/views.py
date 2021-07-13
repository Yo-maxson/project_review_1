from flask import abort, Blueprint, current_app, render_template

from webapp.clothes.models import Clothes
from webapp.weather import weather_by_city

blueprint = Blueprint('clothes', __name__)

@blueprint.route('/')
    # функция передачи данных в шаблон html
def index():
    title = 'Как носится?'
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    clothes_list = Clothes.query.filter(Clothes.text.isnot(None)).all()
    '#.order_by(Clothes.items.desc()).all()'
    return render_template('clothes/index.html', page_title=title, weather=weather, clothes_list=clothes_list)

@blueprint.route('/clothes/<int:clothes_id>')
def single_clothes(clothes_id):
    my_clothes = Clothes.query.filter(Clothes.id == clothes_id).first()
    if not my_clothes:
        abort(404)
    return render_template('clothes/single_clothes.html', page_title=my_clothes.items, clothes=my_clothes)