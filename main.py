import turtle
from ducks import Ducks
from limit import Limit
from dog import Dog
from owner import Owner
import random

turtle.Screen().setup(1400, 1000)  # устанавливаем размер окна приложения
turtle.screensize(350, 650)
height = turtle.screensize()[0]
width = turtle.screensize()[1]


def shoot():
    dog.sound = "Бабах"
    if random.randint(0, 10) < 7:
        dog.sound = "Кря"
        ducks.was_shoot()
        dog.deadDuckPosition = ducks.deadDuck.position()


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('green')

    limit = Limit(height, width)
    owner = Owner(height, width)
    dog = Dog(owner.owner.position())
    ducks = Ducks(height, width)
    window.onkey(shoot, "space")
    window.listen()
    ducks.move_ducks()
    while True:
        print(dog.status)
        if not ducks.ducksStatus:
            window.onkey(None, "space")
        else:
            window.onkey(shoot, "space")
        ducks.move_ducks()
        dog.states(ducks, owner)

    window.mainloop()
