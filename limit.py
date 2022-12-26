import turtle


class Limit:
    height = 0
    width = 0

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.draw_limits()

    def draw_limits(self):
        limit = turtle.Turtle()
        limit.speed(0)
        limit.up()
        limit.hideturtle()
        limit.pensize(5)
        limit.color('black')
        limit.goto(self.width, self.height)
        limit.down()
        limit.goto(self.width, -self.height)
        limit.goto(-self.width, -self.height)
        limit.goto(-self.width, self.height)
        limit.goto(self.width, self.height)
