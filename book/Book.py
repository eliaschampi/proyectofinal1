from utils.decorators import listToDict
from utils.constants import DB_SEPARATOR


class Book:

    __SEP = DB_SEPARATOR

    def __init__(self) -> None:
        self.books = []

    def __strToList(self, row: str) -> list:
        return row.split(self.__SEP)

    def loadBooks(self, db: str) -> None:

        books = []
        try:

            with open(db, "r") as lines:

                title = self.__strToList(next(lines))

                books = [listToDict(title, self.__strToList(row))
                         for row in lines]
        except:
            print("Ocurrión un error al cargar la base de datos local")
            exit()
        finally:
            self.books = books

    def test(self, ping: str):
        print("pong")

    def getAll(self) -> list:
        return self.books
