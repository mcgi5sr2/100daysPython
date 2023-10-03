from turtle import Turtle


MOVE_DISTANCE = 15
UP = 90
DOWN = 270
COLOR = "white"

RIGHT_STARTING_POSITION = (350, 0)
LEFT_STARTING_POSITION = (-350, 0)


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        if position == "right":
            self.create_paddle(RIGHT_STARTING_POSITION)
        else:
            self.create_paddle(LEFT_STARTING_POSITION)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
