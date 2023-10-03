from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_PARK = -320
CAR_START = 310
CAR_SPACING = 20
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.create_cars()

    def create_cars(self):
        # sets up cars and adds them to a list to be reused
        self.hideturtle()
        for cars in range(30):
            self.create_car_list()
        print(self.cars_list)

    def create_car_list(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(320, random.randrange(-200, 200, CAR_SPACING))
        self.cars_list.append(new_car)

    def cars_move(self):
        self.cars_list[random.randrange(0, len(self.cars_list))].forward(10)
        # self.car_start()
        for index, item in enumerate(self.cars_list):
            # car arrives off screen, starts new random location
            if self.cars_list[index].xcor() <= CAR_PARK:
                self.cars_list[index].forward(0)
                self.cars_list[index].goto(CAR_START, random.randrange(-200, 200, CAR_SPACING))
            # whilst between car park and car start, move along at steady speed
            elif CAR_PARK < self.cars_list[index].xcor() < CAR_START:
                self.cars_list[index].forward(STARTING_MOVE_DISTANCE)

    # def car_start(self):
    #     for index, item in enumerate(self.cars_list):
    #         if self.cars_list[index].xcor() == 320:
    #             self.cars_list[random.randrange(0, len(self.cars_list))].goto(CAR_START,
    #                                                                           random.randrange(-200, 200, 10))

    def car_stop(self):
        for index, item in enumerate(self.cars_list):
            self.cars_list[index].forward(0)
