import turtle
from turtle import Turtle, Screen
from random import randrange, randint

# Setup the turtle
tim = Turtle()
tim.shape("turtle")
tim.color("pink")
turtle.colormode(255)

# Move Turtle
# # Draw a Square
# def forward(turtle, distance):
#     turtle.forward(distance)
#
#
# def turn(turtle, angle):
#     turtle.right(angle)
#
#
# forward(tim, 100)
# turn(tim, 90)
# forward(tim, 100)
# turn(tim, 90)
# forward(tim, 100)
# turn(tim, 90)
# forward(tim, 100)
# turn(tim, 90)

# # Draw a dashed line
# index = 0
# while index < 19:
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     index += 1
#
# for _ in range (15):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)


# Draw shapes
# def random_colour():
#     return int(randrange(255))
# def draw_shape(num_sides):
#     tim.pencolor((random_colour(), random_colour(), random_colour()))
#     print(tim.pencolor())
#     angle = 360 / num_sides
#     # now draw the shape
#     for _ in range(0, num_sides):
#         tim.forward(100)
#         tim.right(angle)
#     # tim.right(angle)
#
# for i in range(3, 9):
#     draw_shape(i)

# # random walk
# def random_colour():
#     rgb = int(randrange(255)), int(randrange(255)), int(randrange(255))
#     return rgb
#
# def random_walk():
#     tim.pencolor(random_colour())
#     angle = 90 * randint(0,3)
#     tim.setheading(angle)
#     tim.forward(20)
#
# tim.pensize(20)
# tim.speed(10)
# for i in range(0, 255):
#     random_walk()

# # Colour circles
# tim.pensize(20)
# tim.speed(10)
# def random_colour():
#     rgb = int(randrange(255)), int(randrange(255)), int(randrange(255))
#     return rgb
#
# r = 100
# num_circles = 25
# rotate = 360/num_circles
#
# for i in range(0,num_circles):
#     tim.pencolor(random_colour())
#     tim.circle(r)
#     tim.right(rotate)

# Hirst Spot Painting
import colorgram
from math import isclose
refined_colours = []

# Extract 6 colors from an image.
colours = colorgram.extract('image.jpg', 30)
print(f"length {len(colours)} \n {colours}")
for index, item in enumerate(colours):
    colours[index] = colours[index].rgb
    # cull any background colours ie whites, greys
    if (isclose(colours[index][0], 255, abs_tol=30) and isclose(colours[index][1], 255, abs_tol=30)
            and isclose(colours[index][2], 255, abs_tol=30)) is True:
        pass
    else:
        refined_colours.append(colours[index])

colours = refined_colours

# start tim in the bottom corner, and set 50 x 50 user grid
turtle.setworldcoordinates(-10, -10, 10, 10)
turtle.colormode(255)
# setup tim
tim = Turtle()
tim.shape("turtle")
tim.color("pink")
tim.pensize(10)
tim.speed("fastest")
tim.hideturtle()
tim.penup()


def random_color():
    rand_color = colours[randint(0, len(colours)-1)]
    return rand_color

#
for i in range(21):
    distance = (i)
    for j in range(2):
        for k in range(distance):
            tim.dot(20, random_color())
            tim.forward(1)
        tim.right(90)

## Setup the screen and exit condition
screen = Screen()
screen.colormode(255)
screen.exitonclick()
