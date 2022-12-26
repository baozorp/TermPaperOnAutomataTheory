import turtle
import random

class Owner:

    def __init__(self, height, width):
        self.owner = turtle.Turtle(visible=False)
        self.owner.up()
        self.owner.speed(0)
        x = random.randint(-width + 20, width - 20)
        y = random.randint(-height + 20, height - 20)
        self.owner.goto(x, y)
        turtle.register_shape("sources/owner.gif")
        self.owner.shape("sources/owner.gif")
        self.owner.showturtle()
        self.owner.speed(2)