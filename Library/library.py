from book import Book


class Library:

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__books = {}

    @property
    def name(self):
        return self.__name

    @property
    def books(self) -> dict:
        return self.__books

    def add_book(self, book: Book) -> None:
        self.__books[book.name] = 2

    def pop_book(self, book: Book) -> None:
        if book in self.__books:
            self.__books[book] -= 1

    @staticmethod
    def allow_to_take(book: list, student) -> bool:
        if student not in book:
            return True

        return False

    def __str__(self):
        return f"library-name: {self.name}, books: {self.__books}"