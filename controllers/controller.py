from flask import render_template, request, redirect
from app import app
from models.book_list import books, add_new_book_to_library, delete_book_from_library_by_index
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', title='Library', books=books)


@app.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    checked_out = True if 'checked out' in request.form else False
    new_book = Book(title, author, genre, checked_out)
    add_new_book_to_library(new_book)
    return redirect('/books')
    
@app.route('/books/delete/<index>', methods=['POST'])
def delete_book(index):
    delete_book_from_library_by_index(int(index))
    return redirect('/books')

@app.route('/books/<index>', methods= ['GET'])
def book (index):
    return render_template('book.html', title="Book Details", book=books[int(index)])
