import random
import turtle
from math import fabs


class Dog:

    status = "isWaiting"
    voice = ""
    smell = 0
    counterOfMoves = 0
    ownerPosition = [1, 2]
    tired = 0

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

    def finding(self, deadDuckPosition, mole):
        if random.randint(0, 100) >95:
            mole.mole.showturtle()
        self.counterOfMoves += 1
        position = self.dog.position()
        self.smell = (position[0] / deadDuckPosition[0] + (position[1] / deadDuckPosition[1])) / 2
        if position[0] > deadDuckPosition[0]:
            x = position[0] - fabs(deadDuckPosition[0] - position[0]) * self.counterOfMoves / 10
        else:
            x = position[0] + fabs(deadDuckPosition[0] - position[0]) * self.counterOfMoves / 10
        if position[1] > deadDuckPosition[1]:
            y = position[1] - fabs(deadDuckPosition[1] - position[1]) * self.counterOfMoves / 10
        else:
            y = position[1] + fabs(deadDuckPosition[1] - position[1]) * self.counterOfMoves / 10
        self.dog.goto(x, y)

    def backing(self, ducks, ownerPosition, mole):
        if random.randint(0, 100) > 95:
            mole.mole.showturtle()
        self.counterOfMoves += 1
        position = self.dog.position()
        self.smell = (position[0] / ownerPosition[0] + (position[1] / ownerPosition[1])) / 2
        if position[0] > ownerPosition[0]:
            x = position[0] - fabs(ownerPosition[0] - position[0]) * self.counterOfMoves / 10
        else:
            x = position[0] + fabs(ownerPosition[0] - position[0]) * self.counterOfMoves / 10
        if position[1] > ownerPosition[1]:
            y = position[1] - fabs(ownerPosition[1] - position[1]) * self.counterOfMoves / 10
        else:
            y = position[1] + fabs(ownerPosition[1] - position[1]) * self.counterOfMoves / 10
        self.dog.goto(x, y)
        ducks.deadDuck.speed(3)
        ducks.deadDuck.goto(x + 40, y - 20)
        if self.smell == 1:
            ducks.deadDuck.hideturtle()
            ducks.all_normal()

    def calling(self, ducks, owner, limit):
        owner.owner.goto(self.dog.position()[0], self.dog.position()[1])
        limit.sound = "Хороший мальчик"
        ducks.deadDuck.hideturtle()
        ducks.all_normal()

    def run_after_mole(self, mole):
        self.tired += 1
        mole.move()
        self.dog.goto(mole.mole.position()[0] / 2, mole.mole.position()[1] / 2)

    def states(self, ducks, owner, mole, limit):
        match self.status:
            case "isWaiting":
                if limit.sound == "Бабах":
                    self.status = "isWaiting"
                if limit.sound == "Кря":
                    self.status = "isFinding"
                if limit.sound == "Ко мне":
                    self.voice = ""
                    self.status = "isBacking"
                if limit.sound == "Голос":
                    self.voice = ""
                    self.status = "isCalling"
                return

            case "isFinding":
                limit.sound = ""
                self.dog.speed(3)
                if self.smell == 1:
                    self.smell = 0
                    self.counterOfMoves = 0
                    self.voice = "woof"
                    self.status = "isWaiting"
                else:
                    self.finding(ducks.deadDuck.position(), mole)
                    self.status = "isFinding"
                if mole.mole.isvisible():
                    self.status = "isRunAfterMole"
                    return

            case "isBacking":
                self.dog.speed(3)
                if self.smell == 1:
                    limit.sound = ""
                    self.smell = 0
                    self.counterOfMoves = 0
                    self.status = "isWaiting"
                else:
                    self.backing(ducks, owner.owner.position(), mole)
                    self.status = "isBacking"
                if mole.mole.isvisible():
                    limit.sound = ""
                    self.status = "isRunAfterMole"

            case "isCalling":
                if limit.sound != "Хороший мальчик":
                    self.calling(ducks, owner, limit)
                    self.status = "isWaiting"
                else:
                    self.status = "isCalling"

            case "isSleeping":
                if self.tired == 0:
                    self.status = "isRunAfterMole"
                else:
                    self.tired -= 1
                    self.status = "isSleeping"

            case "isRunAfterMole":
                if limit.sound != "":
                    mole.mole.hideturtle()
                if limit.sound == "Бабах":
                    self.status = "isWaiting"
                if limit.sound == "Ко мне":
                    self.status = "isFinding"
                if limit.sound == "Голос":
                    self.status = "isCalling"
                if limit.sound == "":
                    if self.tired < 5:
                        self.run_after_mole(mole)
                        self.status = "isRunAfterMole"
                    else:
                        self.status = "isSleeping"
