from LibraryManagement import LibraryManagement
from Books import Books
from Members import Members
from Rentals import Rentals


library = LibraryManagement()
library.add_book("1984", "조지 오웰", 1949, "978-0451524935")
library.add_book("앵무새 죽이기", "하퍼 리", 1960, "978-0446310789")
library.add_member("홍길동")


print("\n")
library.rent_book("978-0451524935", "홍길동")
print("\n")
library.print_books()
print("\n")
library.print_members()
print("\n")
library.return_book("978-0451524935", "홍길동")
print("\n")
library.print_members()
print("\n")