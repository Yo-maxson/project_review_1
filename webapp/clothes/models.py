from datetime import datetime

from sqlalchemy.orm import relationship

from webapp.db import db


class Clothes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    clothes_img = db.Column(db.String, unique=True, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def comments_count(self):
        return Comment.query.filter(Comment.clothes_id == self.id).count()

    def __repr__(self):
        return '<Clothes {} {}>'.format(self.items, self.url)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    clothes_id = db.Column(
        db.Integer,
        db.ForeignKey('clothes.id', ondelete='CASCADE'),
        index=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )
    clothes = relationship('Clothes', backref='comments')
    user = relationship('User', backref='comments')

    def __repr__(self):
        return '<Comment {}>'.format(self.id)
