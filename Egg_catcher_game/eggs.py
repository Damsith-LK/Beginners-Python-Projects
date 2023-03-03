from turtle import Turtle
from random import randint


class Egg(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.eggs = []

    def create_eggs(self):

        new_egg = Turtle()
        new_egg.speed('fastest')
        new_egg.shape('circle')
        new_egg.color('white')
        new_egg.shapesize(0.75)
        new_egg.penup()
        new_egg.goto(randint(-270, 270), 280)
        self.eggs.append(new_egg)

    def egg_fall(self):
        for egg in self.eggs:
            egg.speed('normal')
            egg.sety(egg.ycor() - 10)
