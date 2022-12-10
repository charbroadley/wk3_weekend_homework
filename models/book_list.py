from models.book import *

book_1 = Book("The Hair-Carpet Weavers", "Andreas Eschbach", "Sci-fi", True)
book_2 = Book("Before and After", "Andrew Shanahan", "Sci-fi", False)
book_3 = Book("Consider Phlebas", "Iain M Banks", "Sci-fi", False)
book_4 = Book("Lakewood", "Megan Giddings", "Dystopian Fiction", False)
book_5 = Book("The New Wilderness", "Diane Cook", "Dystopian Fiction", True)
book_6 = Book("Water Shall Refuse Them", "Lucie McKnight Hardy", "Horror", True)
book_7 = Book("Starve Acre", "Andrew Michall Hurley", "Folk Horror", False)
book_8 = Book("The Last Thing to Burn", "Will Dean", "Thriller", False)
book_9 = Book("Independent People", "Halldór Laxness", "Literary Fiction", True)
book_10 = Book("Stonehenge", "Bernard Cornwell", "Historical Fiction", False)
book_11 = Book("My Year of Rest and Relaxation", "Ottessa Moshfegh", "Fiction", False)
book_12 = Book("I Who Have Never Know Men", "Jaqueline Harpman", "Dystopian Fiction", True)
book_13 = Book("Tender is the Flesh", "Augustina Bazterrica", "Dystopian Fiction", True)

books = [book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8, book_9, book_10, book_11,book_12, book_13]

def add_new_book_to_library(book):
    books.append(book)

def delete_book_from_library_by_index(index):
    books.pop(index)