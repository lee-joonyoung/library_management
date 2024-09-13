from Members import Members
from Books import Books
from Rentals import Rentals

class LibraryManagement:

    def __init__(self, library_name = "my_library"):
        self.library_name = library_name
        self.members = []
        self.books = []
        self.rentals = []

    def add_book(self, title, author, pub_year, isbn):
        new_book = Books(title, author, pub_year, isbn)
        self.books.append(new_book)

    def add_member(self, name):
        new_member = Members(name)
        self.members.append(new_member)

    def print_books(self):
        print("도서 목록:")
        for book in self.books:
            print(f'{book.title} ({book.author}, 출판년도: {book.pub_year})')
 
    def rent_book(self, isbn, name):
        new_rental = {self.books.isbn: self.name}
        self.rentals.append(new_rental)

    def return_book(self, isbn, name):
        if self.isbn in self.rentals:
            print("반납완료")

library = LibraryManagement()