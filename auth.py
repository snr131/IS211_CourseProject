from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user
from forms import SignupForm, LoginForm
from models import db, User
from bookcatalog import app, login_manager


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username password combination')
        return redirect(url_for('login'))
    return render_template('login.html', form=form, title='Log in', template='login', body='Log in with your user account')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user is None:
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('index'))
        flash('That username is taken')
    return render_template('signup.html', title='Create an account', form=form, template='signup', body='Sign up for a user account')


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to view that page')
    return redirect(url_for('login'))
