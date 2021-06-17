# Este es el juego de adivinar el número
import random

intentos = 0

print('¡Hola!, ¿Cómo te llamas?')
miNombre = input()

numero = random.randint(1, 20) #Esta función llamará a un número aleatorio.
print('Bueno, ' + miNombre + ', estoy pensando en un número entre el 1 y el 20.')

while intentos < 6:
    print('Intenta adivinar.')
    estimmacion = input()
    estimmacion = int(estimmacion) #Se convierte en entero para cuantificar los intentos.

    intentos = intentos + 1 #Se inicia en cero y de ahí se sumarán y validarán los 6 intentos.

    if estimmacion < numero:
            print('Tu estimación es muy baja.')

    if estimmacion > numero:
            print('Tu estimación es muy alta.')

    if estimmacion == numero:
        break

if estimmacion == numero:
    intentos = str(intentos)
    print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi numero en ' + intentos + ' intentos!')

if estimmacion != numero:
    numero = str(numero)
    print('Pues no. El número que estaba pensando era ' + numero)