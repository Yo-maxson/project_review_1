from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField  #импорт ввода данных
from wtforms.validators import DataRequired  # импорт валидатора


'#класс для данных авторизации'
class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})
