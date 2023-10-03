from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLOR = "white"


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.segments[0].shape("turtle")

    def add_segment(self, position):
        new_segment = Turtle("turtle")
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].setheading(self.segments[seg_num - 1].heading())
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    #    self.segments[0].forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    #    self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    #    self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    #   self.segments[0].forward(MOVE_DISTANCE)
