from book.Book import Book
from termcolor import colored
from utils import constants, validation

def showWelcome():
    print("Bienvenido a tus [name]")
    print("****" * 5)


def showMenu():

    print(colored("MENU DEL PROGRAMA", "green"))

    options = constants.BOOK_OPTIONS

    for key, value in options.items():
        print(key, " => ", value)

    return validation.validateMenuOptions(options.keys(), "")


def callAction(option, bookinstance: Book):
    
    if option == "1":
        path = input(f"Ruta del base de datos: Por defecto ({constants.BOOK_DB}) =>")
        bookinstance.loadBooks(path or constants.BOOK_DB)
        print(colored("Correctamente cargado", "green"))
    else if option == "2"
        books = bookinstance.getAll()
        print(books)


if __name__ == "__main__":
    book = Book()
 
    showWelcome()
    option = showMenu()
    callAction(option, book)

    #books = book.getAll()
    #print(books)
