def palindromo(palabra):
    palabra = palabra.replace(' ', '') #En esta linea, se remplaza el espacio por el espacio nulo
    palabra = palabra.lower() #En esta linea se convierte la palabra en minusculas
    palabra_invertida = palabra[::-1] #Significa que irá desde el final hasta el princicio de un espacio a espacio
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es paliíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':    #Esta es la manera mas correcta de correr un programa
    run()