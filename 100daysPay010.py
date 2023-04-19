# # # # # # Day 10 of 100 Dictionaries in Python
# # # # # Functions with outputs, make a calulcator
# # # # def myfunction():
# # # #     result = 2*3
# # # #     return result
# # # ## or
# # # # def myfunction():
# # # #     return 2*3

# # # # def format_name(f_name,l_name):
# # # #     # print(f_name.title())
# # # #     # print(l_name.title())
# # # #     # formatted_f_name = f_name.title()
# # # #     # formatted_l_name = l_name.title()
# # # #     # print(f"{formatted_f_name} {formatted_l_name}")
# # # #     return f"{f_name.title()} {l_name.title()}"

# # # # print(format_name("angela", "YU"))

# # # def format_name(f_name, l_name):
# # #     if f_name == "" or l_name == ""
# # #         return
# # #     formatted_f_name = f_name.title()
# # #     formatted_l_name = l_name.title()
# # #     return f"{f_name.title()} {l_name.title()}"

# # # print(format_name("angela", "YU"))
# # # input("What is your last name?")

# # def is_leap(year):
# #   if year % 4 == 0:
# #     if year % 100 == 0:
# #       if year % 400 == 0:
# #         return True
# #       else:
# #         return False
# #     else:
# #       return True
# #   else:
# #     return False

# # def days_in_month(year, month):
# #   """Take a first and last name and format it o return the title case version of the name"""
# #   if month > 12 or month < 1:
# #     return "Invalid Month"
# #   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# #   is_leap_year = False  
# #   if is_leap(year) is True and month == 2:
# #     return 28
# #   else:
# #     return month_days[month-1]
  
# # #🚨 Do NOT change any of the code below 
# # year = int(input("Enter a year: "))
# # month = int(input("Enter a month: "))
# # days = days_in_month(year, month)
# # print(days)

# #"""DocStrings God here, immediately after the functionline"""

# # Calculator
# import calculator_art

# # add
# def add(n1, n2):
#     return n1 + n2

# #subtract
# def subtract(n1, n2):
#     return n1 - n2

# # multiply
# def multiply(n1, n2):
#     return n1 * n2

# # divide
# def divide(n1, n2):
#     return n1/n2

# operations = {
#     "+":add,
#     "-":subtract,
#     "*":multiply,
#     "/":divide
# }

# num1 = int(input("whats the first number?: "))
# print("Which operator do you want to use?")
# for operands in operations:
#     print(f"{operands} ", end="")
# print()
# operational_symbol = input("Pick an operation from the line above: ")
# num2 = int(input("whats the second number?: "))

# calculation_function = operations[operational_symbol]
# first_answer = calculation_function(num1, num2)

# print(f"{num1} {operational_symbol} {num2} = {answer}")

# operational_symbol = input("Pick aother operation from the line above: ")
# num3 = int(input("What's the next number?: "))
# calculation_function = operations[operational_symbol]
# second_answer = calculation_function(calculation_function(num1,num2), num3)

# print(f"{first_answer} {operational_symbol} {num3} = {second_answer}")


# Calculator II
import calculator_art

from calculator_art import logo

# add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    print(logo)
    num1 = float(input("whats the first number?: "))
    print("Which operator do you want to use?")
    for operands in operations:
        print(f"{operands} ", end="")
    print()

    should_continue = True
    while should_continue:
        operational_symbol = input("Pick an operation: ")
        num2 = float(input("whats the next number?: "))
        calculation_function = operations[operational_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operational_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calcualtion: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
