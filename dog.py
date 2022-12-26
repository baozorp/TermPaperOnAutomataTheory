import random
import turtle
from math import fabs
from nis import match


class Dog:
    dog = turtle.Turtle()
    status = "isWaiting"
    isWaiting = True
    isFinding = False
    isBacking = False
    isCalling = False
    sound = ""
    smell = 0
    counterOfMoves = 0
    ownerPosition = [1, 2]

    def __init__(self, position):
        self.height = position[1] - 40
        self.width = position[0] - 40
        self.dog = turtle.Turtle()
        self.dog.hideturtle()
        self.dog.up()
        self.dog.speed(0)
        self.dog.goto(self.width, self.height)
        turtle.register_shape("sources/dog.gif")
        self.dog.shape("sources/dog.gif")
        self.dog.showturtle()
        self.dog.speed(2)

    def finding(self, deadDuckPosition):
        self.counterOfMoves += 1
        position = self.dog.position()
        self.smell = ((position[0] + deadDuckPosition[0]) / deadDuckPosition[0] + (
                    (position[1] + deadDuckPosition[1]) / deadDuckPosition[1])) / 4
        if position[0] > deadDuckPosition[0]:
            x = position[0] - fabs(deadDuckPosition[0] - position[0]) * self.counterOfMoves / 100
        else:
            x = position[0] + fabs(deadDuckPosition[0] - position[0]) * self.counterOfMoves / 100
        if position[1] > deadDuckPosition[1]:
            y = position[1] - fabs(deadDuckPosition[1] - position[1]) * self.counterOfMoves / 100
        else:
            y = position[1] + fabs(deadDuckPosition[1] - position[1]) * self.counterOfMoves / 100
        self.dog.goto(x, y)

    def backing(self, ducks, ownerPosition):
        self.counterOfMoves += 1
        position = self.dog.position()
        self.smell = (position[0]/ ownerPosition[0] + (position[1] / ownerPosition[1])) / 2
        if position[0] > ownerPosition[0]:
            x = position[0] - fabs(ownerPosition[0] - position[0]) * self.counterOfMoves / 100
        else:
            x = position[0] + fabs(ownerPosition[0] - position[0]) * self.counterOfMoves / 100
        if position[1] > ownerPosition[1]:
            y = position[1] - fabs(ownerPosition[1] - position[1]) * self.counterOfMoves / 100
        else:
            y = position[1] + fabs(ownerPosition[1] - position[1]) * self.counterOfMoves / 100
        self.dog.goto(x, y)
        ducks.deadDuck.speed(3)
        ducks.deadDuck.goto(x+40, y-20)
        if self.smell == 1:
            ducks.deadDuck.hideturtle()
            ducks.all_normal()

    def calling(self, ducks, owner):
        owner.owner.goto(self.dog.position()[0], self.dog.position()[1])
        self.sound = "Хороший мальчик"
        ducks.deadDuck.hideturtle()
        ducks.all_normal()






    def states(self, ducks, owner):
        match self.status:
            case "isWaiting":
                if self.sound == "Бабах":
                    self.status = "isWaiting"
                if self.sound == "Кря":
                    self.status = "isFinding"
                if self.sound == "Ко мне":
                    self.status = "isBacking"
                if self.sound == "Голос":
                    self.status = "isCalling"

            case "isFinding":
                self.dog.speed(3)
                if self.smell == 1:
                    self.smell = 0
                    if random.randint(0, 1):
                        self.sound = "Ко мне"
                    else:
                        self.sound = "Голос"
                    self.counterOfMoves = 0
                    self.status = "isWaiting"
                else:
                    self.finding(ducks.deadDuck.position())
                    self.status = "isFinding"

            case "isBacking":
                self.dog.speed(3)
                if self.smell == 1:
                    self.sound = ""
                    self.smell = 0
                    self.counterOfMoves = 0
                    self.status = "isWaiting"
                else:
                    self.backing(ducks, owner.owner.position())
                    self.isBacking = True

            case "isCalling":
                if self.sound != "Хороший мальчик":
                    self.calling(ducks, owner)
                    self.status = "isWaiting"
                else:
                    self.status = "isCalling"