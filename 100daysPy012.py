# # # # 100daysPy012.py

# # # game_level = 3
# # # def create_enemy():
# # #     enemies = ["Skeleton", "Zombie", "Alien"]
# # #     if game_level < 5:
# # #         new_enemy = enemies[0]

# # #     print(new_enemy)

# # # # Modifying Global Scope

# # enemies = 1

# # def increase_enemies():
# #     print(f"enemies inside function: {enemies}")
# #     return enemies + 1

# # enemies = increase_enemies()
# # print(f"enemies outside function: {enemies}")

# #Global Constants
# # Always make them upper case so I know not to change their values

# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@yu_angela"

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# ## Number Game
# import random
# import numberGame_art
# import os
# def cls():
#     os.system('cls' if os.name=='nt' else 'clear')

# from numberGame_art import logo
# print(logo)

# numGuess = 10

# def playGame(numGuess):
#     comNumber = random.randint(1, 100)
#     usrNumber = 0
#     while numGuess > 0:
#             usrNumber = int(input(f"You have {numGuess} attempts to guess the number between 1-100."))
#             if usrNumber < comNumber:
#                 print("Too Low.")
#                 numGuess = numGuess -1
#             elif usrNumber > comNumber:
#                 print("Too high.")
#                 numGuess = numGuess -1
#             elif usrNumber == comNumber:
#                 print(f"You got it! The answer was {comNumber}")
#                 return
#             else:
#                 print(f"Invalid input please try again")

# while input("Do you want to play a  game? Type 'y' or 'n': ") == "y" :
#     cls()
#     gameType = input("Do you want to play a (h)ard or (e)asy game")
#     if gameType == "h":
#         numGuess = 10
#     else:
#         numGuess = 100
#     playGame(numGuess)


# Number Game (Full solution)
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check users guess against actual answer
def check_answer(guess, answer, turns):
    """Checks answer against gues. Returns number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns -1
    elif guess < answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer is {answer}")

#Make a function to set difficulty
def set_difficulty():
   level = input("Choose a difficulty easy or hard")
   if level == "easy":
       return EASY_LEVEL_TURNS
   else:
       return HARD_LEVEL_TURNS
#Choosing a random number between 1:100
def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1,100)

    turns = set_difficulty()

    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")
        #Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess!= answer:
            print("Guess Again")
        #Track the number of turns and reduce by one if they get it wrong
game()