from turtle import Turtle


class Catcher(Turtle):

    def __init__(self):
        super().__init__()
        self.color('cyan')
        self.speed('fastest')
        self.shape('triangle')
        self.right(90)
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.speed('fastest')
        self.goto(0, -280)

    def go_left(self):
        self.setx(self.xcor() - 30)

    def go_right(self):
        self.setx(self.xcor() + 30)
