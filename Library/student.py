from library import Library


class Student:

    def __init__(self, name: str, lastname: str, age: int) -> None:
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        self.__books = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def lastname(self) -> str:
        return self.__lastname

    @property
    def age(self) -> int:
        return self.__age

    @property
    def books(self) -> list:
        return self.__books

    def take_book(self, library: Library, book_name) -> None:
        if book_name not in library.books:
            print("Library does not have this book: ")

        elif library.books[book_name] == 0:
            print("This book is currently unavailable: ")

        else:
            if library.allow_to_take(self.__books, book_name):
                self.__books.append(book_name)
                library.pop_book(book_name)

            else:
                print("You already have this book. ")

    def return_book(self, library: Library, book_name: str) -> None:
        if book_name not in self.books:
            print("You do not have this book: ")

        elif book_name not in library.books:
            print("You did not get this book from here: ")

        else:
            library.books[book_name] += 1
            self.__books.remove(book_name)

    def __str__(self) -> str:
        return f"student-name: {self.name}, lastname: {self.lastname}, age: {self.age}, books: {self.__books}"