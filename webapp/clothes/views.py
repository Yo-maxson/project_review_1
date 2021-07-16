from flask import abort, Blueprint, current_app, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required

from webapp.db import db
from webapp.clothes.forms import CommentForm
from webapp.clothes.models import Comment, Clothes
from webapp.weather import weather_by_city
from webapp.utils import get_redirect_target

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
    comment_form = CommentForm(clothes_id=my_clothes.id)
    return render_template('clothes/single_clothes.html', page_title=my_clothes.items, clothes=my_clothes, comment_form=comment_form)


@blueprint.route('/clothes/comment', methods=['POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.comment_text.data, clothes_id=form.clothes_id.data, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий успешно добавлен')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в заполнении поля "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
    return redirect(get_redirect_target())
