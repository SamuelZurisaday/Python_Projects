import random


def generar_password():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z",]
    simbolos = ["@", "!", "*", "#", "%", "&", "$"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


    caracteres = simbolos + mayusculas + minusculas + numeros


    password = []


    for i in range(16):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)


    password = ''.join(password)
    return password


def run():
    password = generar_password()
    print("Tu nuevo password es: " + password)


if __name__ == "__main__":
    run()