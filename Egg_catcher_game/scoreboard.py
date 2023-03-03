from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed('fastest')
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)
        self.create_score()

    def create_score(self):
        self.write(arg=f'Score: {self.score}', align='center', move=False, font=('Ariel', 25, 'bold'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', move=False, font=('Ariel', 25, 'bold'))