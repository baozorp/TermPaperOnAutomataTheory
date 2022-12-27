import turtle
import random


class Ducks:
    height = 0
    width = 0
    ducksCount = 0
    ducksArray = []
    ducksStatus = True
    deadDuck = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.ducksCount = random.randint(7, 10)
        for i in range(self.ducksCount):
            duck = turtle.Turtle(visible=False)
            duck.speed(0)
            turtle.register_shape("sources/duck.gif")
            turtle.register_shape("sources/dead.gif")
            duck.shape("sources/duck.gif")
            duck.up()
            x = -self.width - 100
            y = random.randint(-self.height + 20, self.height - 20)
            duck.goto(x, y)
            duck.speed(10)
            self.ducksArray.append(duck)
        for duck in self.ducksArray:
            duck.showturtle()
        self.deadDuck = self.ducksArray[0]

    def was_shoot(self):
        self.ducksStatus = False
        self.deadDuck = self.ducksArray.pop(random.randint(0, len(self.ducksArray)-1))
        self.deadDuck.shape("sources/dead.gif")
        for duck in self.ducksArray:
            duck.speed(0)
            duck.goto(1000, 1000)
            duck.hideturtle()

    def all_normal(self):
        self.deadDuck.hideturtle()
        self.deadDuck.shape("sources/duck.gif")
        self.ducksArray.append(self.deadDuck)
        self.deadDuck = self.ducksArray[0]
        self.ducksStatus = True
        for duck in self.ducksArray:
            x = -self.width - 150
            y = random.randint(-self.height + 20, self.height - 20)
            duck.goto(x, y)
            duck.speed(10)
        for duck in self.ducksArray:
            duck.showturtle()




    def move_ducks(self):
        if self.ducksStatus:
            for duck in self.ducksArray:
                position = duck.position()
                if position[0] > self.width or position[1] < -self.height or position[1] > self.height:
                    duck.hideturtle()
                    duck.speed(0)
                    if duck.position()[0] > self.width:
                        x = -self.width
                        y = duck.position()[1]
                    elif duck.position()[1] < -self.height:
                        x = duck.position()[0]
                        y = self.height
                    elif duck.position()[1] > self.height:
                        x = duck.position()[0]
                        y = -self.height

                    duck.goto(x, y)
                    duck.speed(10)
                    duck.showturtle()
                x = random.randint(0, 50)
                y = random.randint(-50, 50)
                position = duck.position()
                duck.goto(position[0] + x, position[1] + y)