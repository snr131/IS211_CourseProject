from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message='Select a password with 6 or more characters')])
    confirm = PasswordField('Confirm your password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Log in')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Passowrd', validators=[DataRequired()])
    submit = SubmitField('Log in')


class AddBookForm(FlaskForm):
    isbn_10 = StringField('ISBN_10', validators=[DataRequired()])
    submit = SubmitField('Search')


class DeleteBookForm(FlaskForm):
    submit = SubmitField('Delete')