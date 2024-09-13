class Books:

    def __init__(self, title, author, pub_year, isbn):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.isbn = isbn
        print(f'{self.title} (저자: {self.author}, 출판년도: {self.pub_year}) 도서가 추가되었습니다.')