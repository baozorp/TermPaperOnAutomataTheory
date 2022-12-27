import turtle
from ducks import Ducks
from limit import Limit
from dog import Dog
from owner import Owner
from mole import  Mole
import random

turtle.Screen().setup(1400, 1000)
turtle.screensize(350, 650)
height = turtle.screensize()[0]
width = turtle.screensize()[1]


def shoot():
    limit.sound = "Бабах"
    print(limit.sound)
    if dog.status == "isRunAfterMole":
        ducks.all_normal()
    if dog.status == "isWaiting":
        if random.randint(0, 10) < 7:
            limit.sound = "Кря"
            ducks.was_shoot()
            dog.deadDuckPosition = ducks.deadDuck.position()


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('green')

    limit = Limit(height, width)
    owner = Owner(height, width)
    dog = Dog(owner.owner.position())
    ducks = Ducks(height, width)
    mole = Mole(height, width)
    window.onkey(shoot, "space")
    window.listen()
    ducks.move_ducks()
    while True:
        print(dog.status)
        if dog.status == "isWaiting" or dog.status == "isRunAfterMole":
            window.onkey(shoot, "space")
        else:
            window.onkey(None, "space")


        if dog.voice == "woof" or dog.status == "isRunAfterMole":
            limit.button1.showturtle()
            limit.button2.showturtle()
        else:
            limit.button1.hideturtle()
            limit.button2.hideturtle()




        ducks.move_ducks()
        dog.states(ducks, owner, mole, limit)

    window.mainloop()
