from turtle import Screen, Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")
COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(0, 270)
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score} ", False, ALIGNMENT, FONT)

    def score(self, position):
        if position == "l":
            self.l_score += 1
        else:
            self.r_score += 1
        self.update_scoreboard()