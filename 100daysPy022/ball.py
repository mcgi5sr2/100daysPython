from turtle import Turtle
import random

MOVE_DISTANCE = 15
INITIAL_HEADING = random.randint(-45, 45)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(INITIAL_HEADING)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def wall_bounce(self):
        self.setheading(-self.heading())

    def paddle_bounce(self, paddle):
        global MOVE_DISTANCE
        self.setheading(-self.heading()+180+self.distance(paddle))
        MOVE_DISTANCE += 10

    def reset(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE = 15
        self.goto(0,0)
        self.setheading(-self.heading()+180)



