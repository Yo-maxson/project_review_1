from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    clothes_id = HiddenField('ID товара', validators=[DataRequired()])
    comment_text = StringField('Текст комментария',validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})