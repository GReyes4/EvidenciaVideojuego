"""
Tron Classic Arcade Game

Autores:
Roberto González Reyes A00833852
Adrian Gomez Castillo A00835254
Diego Rodriguez Orozco A00835032


"""

from time import sleep
from turtle import *

from freegames import square, vector

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()


def inside(head):
    """Return True if head inside screen."""
    return -200 < head.x < 200 and -200 < head.y < 200

def convcolor(numcolor):
    "Convertimos la opción a un color"
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
        return "gray"


def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if not inside(p1head) or p1head in p2body:
        print('Player 1 wins!')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player 2 wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, convcolor(p1color))
    square(p2xy.x, p2xy.y, 3, convcolor(p2color))
    update()
    ontimer(draw, 50)


print("Rojo = 1         Azúl = 2        Verde = 3\n")
print("Rosa = 4         Dorado = 5    Negro = 6\n")
p1color = input("Jugador 1 elige un color: ")
print("\nRojo = 1         Azúl = 2        Verde = 3\n")
print("Rosa = 4         Dorado = 5    Negro = 6\n")
p2color = input("Jugador 2 elige un color: ")
print("\n Empezando...\n")
setup(420, 420, 370, 0)
sleep(5)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(-90), 'l')
draw()
done()