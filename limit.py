import turtle



class Limit:
    height = 0
    width = 0
    button1 = None
    button2 = None
    sound = ""



    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.draw_limits()
        self.draw_buttons()


    def action1(self, x, y):
        self.sound = "Ко мне"

    def action2(self, x, y):
        self.sound = "Голос"

    def action3(self, x, y):
        print(1)

    def draw_buttons(self):
        CURSOR_SIZE = 20
        FONT_SIZE = 12
        FONT = ('Arial', FONT_SIZE, 'bold')
        self.button1 = turtle.Turtle()
        self.button1.hideturtle()
        self.button1.penup()
        self.button1.goto(-120, self.height + 10)
        self.button1.write("Ко мне", align='right', font=FONT)
        self.button1.goto(-100, self.height + 20)
        self.button1.shape('square')
        self.button1.fillcolor('red')
        self.button1.onclick(self.action1)
        self.button2 = turtle.Turtle()
        self.button2.hideturtle()
        self.button2.penup()
        self.button2.goto(100, self.height + 10)
        self.button2.write("Голос", align='right', font=FONT)
        self.button2.goto(120, self.height + 20)
        self.button2.shape('square')
        self.button2.fillcolor('red')
        self.button2.onclick(self.action2)

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
