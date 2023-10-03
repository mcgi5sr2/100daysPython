from turtle import Screen, Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Current level is: {self.score}", False, "center", FONT)

    def score_increment(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER \n SCORE {self.score}", False, "center", FONT)