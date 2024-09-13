class Rentals:

    def __init__(self, book, name):
        self.book = book
        self.name = name

    def rent_book(self, book, name):
        new_rental = {"book" = book, "name" = name}
        self.library_management.rentals.append(new_rental)

    def return_book(self, book, name):
        pass