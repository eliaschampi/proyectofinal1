from utils import constants

def validateMenuOptions(options: list, userinput):

    counter = 0
    limit = constants.LIMIT_TRIES
    while userinput not in options and counter < limit:
        userinput = input("Ingresa una opción: => ")
        counter += 1
    else: 
        if userinput in options:
            return userinput
        else:
            print(f"Ingresaste una opción incorrecta {counter} veces. Adios")
            exit()