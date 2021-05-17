from bookcatalog import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn_10 = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text, nullable=False)
    page_count = db.Column(db.Text, nullable=False)
    publication_date = db.Column(db.TEXT, nullable=False)
    rating = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_added_to_catalog = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.title} added to catalog on {self.date_added_to_catalog}'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)



   