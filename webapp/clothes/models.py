from webapp.db import db


class Clothes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    clothes_img = db.Column(db.String, unique=True, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Clothes {} {}>'.format(self.items, self.url)