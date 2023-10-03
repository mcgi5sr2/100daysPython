import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
game_tick_rate = 0.1
while game_is_on:
    time.sleep(game_tick_rate)
    screen.update()
    car_manager.cars_move()

    # detect collision with car
    for index, item in enumerate(car_manager.cars_list):
        if item.distance(player) < 15:
            car_manager.car_stop()
            scoreboard.game_over()
            game_is_on = False

    # detect collision with top of screen
    if player.ycor() > 260:
        scoreboard.score_increment()
        player.player_reset()
        game_tick_rate = game_tick_rate * 0.5



screen.update()

screen.exitonclick()


