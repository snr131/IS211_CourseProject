from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookcatalog.db'


db = SQLAlchemy(app)
login_manager = LoginManager(app)


from routes import *


if __name__ == '__main__':
    app.run(debug=True)