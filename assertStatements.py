def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = (input("Ingresa un número: "))
    #assert nos permite asegurar que si no es un numero lo que se ingresa, arroje mensaje de falso
    assert num.isnumeric(), "Debes de ingresar un número"
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()