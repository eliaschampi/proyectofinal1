from book.Book import Book
from termcolor import colored
from book.app import showMenu, callAction


def showWelcome() -> None:
    print(colored("Bienvenido a tu programa", "blue"))
    print("****" * 5)


def showGoodBye() -> None:
    print(colored("Hasta pronto!", "blue"))
    exit()


def main(bookinstance: Book) -> bool:

    if callAction(showMenu(), bookinstance):
        msg = colored("Volver al menu (si/no) por omision (si) => ", "yellow")
        return (input(msg) or "si") == "si"

    return False


if __name__ == "__main__":

    # show welcome message
    showWelcome()

    # start book instance
    bookinstance: Book = Book()

    willBeContinue = True

    while willBeContinue:

        willBeContinue = main(bookinstance)

    else:

        showGoodBye()
