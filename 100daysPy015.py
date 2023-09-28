# PyCharm and local install of Python ZzzZZZzz
# Coffee Machine Project

# 3 hot flavours
# espresso, latte, cappuccino

# Coin operated
# penny $0.01, dime $0.10, nickel $0.05, quarter $0.25

# TODO: 1 Print report of all the coffee machine resources
# Must print report (resources left) water, milk, coffee, money
# TODO: 2 Check resources are sufficient to make coffee
# Check resources are sufficient to order the drink
# TODO: 3 process the coins (check sufficient, calculate change etc)
# Process coins
# Check transaction successful
# Make coffee (deduct resources)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

from os import system
from time import sleep

money = 0.00
coffeeMachineOn = True

print(MENU["espresso"]["ingredients"]["water"])


def coffee_machine_off():
    print("Shutting down")
    sleep(5)
    exit(["GoodNight"])


def print_report():
    print(f"Water {resources['water']}ml")
    print(f"Milk {resources['milk']}ml")
    print(f"Coffee {resources['coffee']}g")
    print(f"Money ${round(money, 2)}")


def check_resources(coffee_name):
    for index, item in enumerate(MENU[coffee_name]["ingredients"]):
        #print(MENU[coffee_name]["ingredients"][item])
        if MENU[coffee_name]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return 0


def process_coins(coffee_name):
    quarters = float(input(print("how many quarters?: "))) * 0.25
    dimes = float(input(print("how many dimes?: "))) * 0.1
    nickles = float(input(print("how many nickles?: "))) * 0.05
    pennies = float(input(print("how many pennies?: "))) * 0.01
    coin_total = quarters + dimes + nickles + pennies
    if coin_total < MENU[coffee_name]['cost']:
        print("Sorry that is not enough money. Money refunded")
    elif coin_total > MENU[coffee_name]['cost']:
        print(f"customer was charged {money}")
        print(f"Here is ${round(coin_total - MENU[coffee_name]['cost'], 2)} dollars in change")
        return MENU[coffee_name]['cost']
    else:
        print("Thanks for exact change")
        return MENU[coffee_name]['cost']

def make_coffee(coffee_name):
    for index, item in enumerate(MENU[coffee_name]["ingredients"]):
        # print(f"{coffee_name} {item} {MENU[coffee_name]['ingredients'][item]}")
        # print(f"{item} resources {resources[item]}")
        resources[item] = resources[item] - MENU[coffee_name]['ingredients'][item]
        # print(f"new {item} resources {resources[item]}")
    print(f"Here is your {coffee_name}. Enjoy!")

while coffeeMachineOn:
    user_input = input(print("“What would you like? (espresso/latte/cappuccino):”")).lower()

    if user_input == "off":
        coffee_machine_off()
        coffeeMachineOn = False
    elif user_input == "report":
        print_report()
    elif user_input in ("espresso", "latte", "cappuccino"):
        enough_resources = check_resources(user_input)
        if enough_resources == 0:
            print("Please refill the machine and start again")
        else:
            money += process_coins(user_input)
            make_coffee(user_input)
    elif user_input is not ("espresso", "latte", "cappuccino"):
        print("sorry please try again")


