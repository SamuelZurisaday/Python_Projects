import turtle
import time
import random

posponer = 0.1  # Tiempo de la ventana

# Configuracion de la ventana
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeza de la Serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()  # comando para quitar el rastro
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()  # comando para quitar el rastro
comida.goto(0, 100)

# Segmentos/Cuerpo de la serpiente
segmentos = []

# Funciones Direcciones
def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

# Teclado
wn.listen()  # para que la pantalla este atenta a los eventos del teclado
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

# Funciones Direcciones Coordenadas
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)


while True:
    wn.update()

    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento) #Con esta línea se agregan los elementos la lista segmentos


    #Mover el cuerpo de la serpiente
    totalSegmentos = len(segmentos)
    for index in range(totalSegmentos -1, 0, -1):



    mov()
    time.sleep(posponer)
