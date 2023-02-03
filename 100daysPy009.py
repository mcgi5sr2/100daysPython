# # # Day 9 of 100 Dictionaries in Python
# # # You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

# # # Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

# # # DO NOT modify lines 1-7 to change the existing student_scores dictionary.

# # # DO NOT write any print statements.

# # # This is the scoring criteria:

# # # Scores 91 - 100: Grade = "Outstanding"

# # # Scores 81 - 90: Grade = "Exceeds Expectations"

# # # Scores 71 - 80: Grade = "Acceptable"

# # # Scores 70 or lower: Grade = "Fail"

# # # Expected Output
# # # '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'

# # # student_scores = {
# # #   "Harry": 81,
# # #   "Ron": 78,
# # #   "Hermione": 99, 
# # #   "Draco": 74,
# # #   "Neville": 62,
# # # }
# # # # 🚨 Don't change the code above 👆

# # # #TODO-1: Create an empty dictionary called student_grades.
# # # student_grades = {}

# # # #TODO-2: Write your code below to add the grades to student_grades.👇
# # # for keys in student_scores:
# # #     if student_scores[keys] < 70:
# # #         student_grades[keys] = "Fail"
# # #     elif student_scores[keys] < 80:
# # #         student_grades[keys] = "Acceptable"
# # #     elif student_scores[keys] < 90:
# # #         student_grades[keys] = "Exceeds Expectations"
# # #     else:
# # #         student_grades[keys] = "Outstanding"

# # # # 🚨 Don't change the code below 👇
# # # print(student_grades)

# # ##### Nesting
# # # Nest multiple lists and dictionaries into a dictioanry
# # Capitals = {
# #     "France": "Paris",
# #     "Germany": "Berlin",
# # }

# # # Nesting a list in a Dictionary
# # travel_log = {
# #     "France": ["Paris", "Lille", "Dijon"],
# #     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# # }

# # # Nesting a Dictionary in a Dictionary
# # travel_log = {
# #     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
# #     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# # }

# # # Nesting a Disctionary in a List
# # travel_log = [
# #     {
# #         "country": "France",
# #         "cities_visited": ["Paris", "Lille", "Dijon"],
# #         "total_visits": 12
# #     },
# #     {
# #         "country": "Germany",
# #         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
# #         "total_visits": 5
# #     },
# # ]

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

import auction_logo
import os

from auction_logo import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    # ("Angela": 123, "James": 321,)
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("are there anymore bidders? Type `yes` or `no`:\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('clear')

## clear screen windows
# os.system('cls')
## clear screen macOS
# os.system('clear')
