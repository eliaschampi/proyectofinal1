from utils.decorators import listToDict

class Book:

    __SEP = "|"

    def __init__(self) -> None:
        self.books = []

    def strToList(self, row: str) -> list:
        return row.split(self.__SEP)

    def loadBooks(self, db) -> None:

        books = []
        with open(db, "r") as lines:

            title = self.strToList(next(lines))

            for row in lines:
                books.append(listToDict(title, self.strToList(row)))
        self.books = books

    def test(self, ping):
        print("pong")

    def getAll(self) -> list:
        return self.books