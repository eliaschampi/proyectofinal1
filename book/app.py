
from termcolor import colored
from utils import constants, validation, decorators


def showMenu() -> str:

    print(colored("MENU DEL PROGRAMA", "green"))

    options = constants.BOOK_OPTIONS

    for key, value in options.items():
        print(key, " => ", value)

    return validation.validateMenuOptions(options.keys(), "")


def callAction(option: str, bookinstance) -> bool:

    if option == "1":
        omision = colored(f"Por omisión ({constants.BOOK_DB})", "blue")
        path = input(f"Ruta del base de datos: {omision} => ")
        bookinstance.loadBooks(path or constants.BOOK_DB)
        print(colored("Correctamente cargado", "green"))
        return True

    elif option == "2":
        books = bookinstance.getAll()
        decorators.printAsTableForm(books)
        return True

    elif option == "3":
        #addbook
        return True

    return False
