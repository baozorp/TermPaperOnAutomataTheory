import turtle
import random


class Mole:


    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.mole = turtle.Turtle(visible=False)
        self.mole.up()
        self.mole.speed(0)
        turtle.register_shape("sources/mole.gif")
        self.mole.shape("sources/mole.gif")
        x = random.randint(-width + 20, width - 20)
        y = random.randint(-height + 20, height - 20)
        self.mole.goto(x, y)
        self.mole.speed(7)

    def move(self):
        if not self.mole.isvisible():
            self.mole.showturtle()
        x = random.randint(-self.width + 20, self.width - 20)
        y = random.randint(-self.height + 20, self.height - 20)
        self.mole.goto(x, y)
