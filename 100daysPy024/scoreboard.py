from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")
COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HIGH Score {self.high_score}", False, ALIGNMENT, FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over.", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0