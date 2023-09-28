# ### 100daysPy014
# ## Higher Lower Game

# # Import gameData & art
# import Py014gameData
# import Py014art
# from Py014gameData import data
# from Py014art import logo, vs
# from random import randint
# print(logo)


# # choose a random dictionary item from the list
# def compare(letter): 
#     # choose a random new dictionary item from the list
#     compare = data[randint(0,len(data))]
#     # print the info from this dictionary item EXCEPT the follower count
#     print(f"Compare {letter}: {compare['name']}, {compare['description']}, {compare['country']}")
#     return compare['follower_count']

# score = 0 

# def score(score):
#     return (score +1)

# # store the follower count as a new variable
# followercountA = compare("A")
# print(followercountA)
# #print vs
# print(vs)
# # store the follower count as a new variable
# followercountB = compare("B")
# print(followercountB)
# # User input higher or lower
# userChoice = input(print(f"Who has more followers? Type 'A' or 'B': "))

# if userChoice == "A" & followercountA > followercountB:
#     score = score()
#     print(f"Your right! current score: {score}.")
# else:
#     print(f"you lose!")

# if

# # if higher followercountA > followercountB
# # if lower followercountA < followercountB


###Udemy answer
from Py014art import logo, vs
from Py014gameData import data
import random
from os import system


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """ Format the account data into a printable format """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """"Take the users guess and follower counts of an and b, and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    # Display art
    print(logo)
    score = 0
    game_should_continue = True
    # Generate a random account from the game data
    account_b = get_random_account()

    while game_should_continue:
        # Switch account B to account B
        account_a = account_b
        # Generate a random account from the game data
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        # Ask user for a guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check if user is correct
        # Get follower count of each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        # Use if statement to check if user is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear the screen
        system('clear')
        print(logo)

        # Give user feedback on their guess
        # Score keeping
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"You're wrong! Final score: {score}")


game()
