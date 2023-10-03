from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")
COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", False, ALIGNMENT, FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", False, ALIGNMENT, FONT)
