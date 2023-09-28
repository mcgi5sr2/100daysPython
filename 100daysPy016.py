# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DeepPink")
#
# timmy.forward(100)
# timmy.speed(1)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


# from prettytable import PrettyTable
#
# table = PrettyTable()
# print(table)
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system
from time import sleep

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_maker_on = True
menu_item = MenuItem


def coffee_maker_off():
    print("Shutting down")
    sleep(5)
    exit(["GoodNight"])


while coffee_maker_on:
    user_input = input(print(f"What would you like? ({menu.get_items()})")).lower()

    if user_input == "off":
        coffee_maker_off()
        coffee_maker_on = False
    elif user_input == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif user_input in ("espresso", "latte", "cappuccino"):
        # Make an object that is the coffee order (name, cost, ingredients)
        coffee_order = menu.find_drink(user_input)
        # print(coffee_order)
        # Check resources
        enough_resources = coffee_maker.is_resource_sufficient(coffee_order)
        if enough_resources == 0:
            print("please refill the machine and start again")
        elif money_machine.make_payment(coffee_order.cost) == 1:
            coffee_maker.make_coffee(coffee_order)
    elif user_input != ("espresso", "latte", "cappuccino"):
        print("sorry please try again")
