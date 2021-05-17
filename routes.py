from flask_login import login_required, logout_user, current_user
from bookcatalog import app, db
from flask import render_template, redirect,url_for, flash
import forms
from models import Book
from datetime import datetime
import json
from urllib.request import urlopen
from auth import *


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
@login_required
def index():
    username = current_user.username
    catalog = Book.query.filter_by(user_id = current_user.id)
    return render_template('dashboard.html', catalog=catalog, current_user=username)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddBookForm()
    if form.validate_on_submit():

        user_id = current_user.id
                
        api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
        isbn_10 = form.isbn_10.data
        resp = urlopen(api + isbn_10)
        book_data = json.load(resp)
        
        volume_info = book_data["items"][0]["volumeInfo"]
        title = volume_info['title']
        try:
            author = volume_info["authors"][0]
        except:
            author = 'Author unavailable'
        try:
            page_count = volume_info['pageCount']
        except:
            page_count = 'Page count unavailable'
        try:
            publication_date = volume_info['publishedDate']
        except:
            publication_date = 'Publication date unavailable'
        try: 
            rating = volume_info['averageRating']
        except:
            rating = 'Rating unavilable'
        try:
            image_url = volume_info['imageLinks']['smallThumbnail']
        except:
            image_url = ''

        b = Book(isbn_10=form.isbn_10.data, title=title, author=author, page_count=page_count, publication_date=publication_date, rating=rating, image_url=image_url, user_id=user_id, date_added_to_catalog=datetime.utcnow())
        db.session.add(b)
        db.session.commit()
        flash('Book added to catalog')

        return redirect(url_for('index'))
    return render_template('add.html', form=form, current_user=current_user)


@app.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete(book_id):
    getbook = Book.query.get(book_id)
    form = forms.DeleteBookForm()
    if getbook:
        if form.validate_on_submit():
            db.session.delete(getbook)
            db.session.commit()
            flash('Book deleted')
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, book_id=book_id, title=getbook.title)
    else:
        flash('Book not found')
    return redirect(url_for('index'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))