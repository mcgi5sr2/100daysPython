from turtle import Screen
import time
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball


# Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.title("<< P O N G >>")
screen.tracer(0)

scoreboard = Scoreboard()


r_paddle = Paddle("right")
l_paddle = Paddle("left")
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # detect collision on top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect collision for paddles
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50:
        ball.paddle_bounce(r_paddle)

    if ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.paddle_bounce(l_paddle)

    # detect collision left right walls
    if ball.xcor() > 400:
        time.sleep(0.5)
        ball.reset()
        scoreboard.score("l")
        time.sleep(0.5)

    if ball.xcor() < -400:
        time.sleep(0.5)
        ball.reset()
        scoreboard.score("r")
        time.sleep(0.5)



screen.exitonclick()