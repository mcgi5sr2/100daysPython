from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title = "Bet Input", prompt="which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.setposition(x=-230, y=0)

all_turtles = []

for index, turtle_colour in enumerate(colours):
    new_turtle = Turtle(shape="turtle", )
    new_turtle.penup()
    new_turtle.speed("fastest")
    new_turtle.pencolor(turtle_colour)
    new_turtle.color(turtle_colour)
    ypos = (index*40)-100
    new_turtle.goto(x=-230, y=ypos)
    new_turtle.pendown()
    new_turtle.pensize(5)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"you've won! The {winning_colour} turtle is the winner")
            else:
                print(f"You've lose, the winning turtle was {winning_colour}")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
        turtle.setheading(turtle.heading() - randint(-10,10))

screen.exitonclick()
