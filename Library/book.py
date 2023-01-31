class Book:

    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self) -> None:
        return self.__name

    def __str__(self) -> str:
        return f"book-name: {self.name}"
