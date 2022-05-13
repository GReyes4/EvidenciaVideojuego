"""
Tron Classic Arcade Game

Autores:
Roberto González Reyes A00833852
Adrian Gomez Castillo A00835254
Diego Rodriguez Orozco A00835032


"""
'Importamos librerias necesarias'
from time import sleep
from turtle import *

from freegames import square, vector

'Declaramos vectores para movimiento y dirección de jugadores'
p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

'Declaramos limites para el espacio jugable'
'Nos sirve para que los jugadores pierdan si salen del área'
def inside(head):
    """Sera verdadero siempre y cuando la cabeza se encuentre en espacio jugable"""
    return -240 < head.x < 240 and -240 < head.y < 240


'Cambiamos la entrada del menú al color equivalente para que turtle lo entienda'
def convcolor(numcolor):

    if numcolor == '1':
        return "red"
    elif numcolor == '2':
        return "blue"
    elif numcolor == '3':
        return "green"
    elif numcolor == '4':
        return "hot pink"
    elif numcolor == '5':
        return "gold"
    elif numcolor == '6':
        return "black"
    else:
        'Como Easter Egg si no eliges un valor valido tu color sera gris'
        return "gray"


def draw():
    """Dibujamos el juego y movemos a los jugadores"""
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    'Establecemos condiciones de victoria por choque o salir del área'
    if not inside(p1head) or p1head in p2body:
        print('Player 1 wins!')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player 2 wins!')
        return

    'Guardamos el recorrido de ambos jugadores'
    p1body.add(p1head)
    p2body.add(p2head)

    'Dibujamos cada cuadro conforme se da el movimiento'
    square(p1xy.x, p1xy.y, 3, convcolor(p1color))
    square(p2xy.x, p2xy.y, 3, convcolor(p2color))
    update()
    ontimer(draw, 50)

'Imprimimos menú de elección de colores'
print("Rojo = 1         Azúl = 2        Verde = 3\n")
print("Rosa = 4         Dorado = 5    Negro = 6\n")
p1color = input("Jugador 1 elige un color: ")
print("\nRojo = 1         Azúl = 2        Verde = 3\n")
print("Rosa = 4         Dorado = 5    Negro = 6\n")
p2color = input("Jugador 2 elige un color: ")
print("\n Empezando...\n")
setup(420, 420, 370, 0)
'Esperamos 5 segundos para evitar un inicio desagradable o apresurado'
sleep(2)
hideturtle()
tracer(False)
'Establecemos controles'
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(-90), 'l')
draw()
done()