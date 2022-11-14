# ### Heads or Tails
# import random

# randomSide = random.randint(0, 1)
# if randomSide == 1:
#     print("Heads")
# else:
#     print("Tails")

### Lists
# fruits = [item1, item2] ...
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
# print(states_of_america[-1])
# states_of_america.append("Happyland") ## appends Happyland to the end of list
# states_of_america.extend([SadLand, BlueLand, RedLand, GreenLand]) ## extends the list by another list

### Banker Roulette
# Who will pay the bill
# input a list of names separated by a ,
# then choose one of the names to pay the bill
# new cplit example str = "Hello,from,AskPython"    op = str.split(",")     print(op) >>>> then prints a List of strings ["Hello", "from" "AskPython"]
# import random
# namesToChoose = input("Please input the number of people as a list of comma separated names")
# listNames = namesToChoose.split(",")
# numberOfNames = len(listNames)
# chosenName = listNames[random.randint(0, numberOfNames - 1)]
# print(f"The person who will pay today is {chosenName}")

# # Nested Lists
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
# #### This prints the second list, [0] would print the first list fruits[]
# print(dirty_dozen[1])
# #### This prints the second object in the second list so vegetables[1]
# print(dirty_dozen[1][1])

# ##### Treasure Map
# row1= ["■","■","■"]
# row2= ["■","■","■"]
# row3= ["■","■","■"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# #position = input("Where do you want to put the treasure? ")

# ### input should be colum followed by row, so column2 and row 3 would be 23
# treasureLocation = input("please input column number then row number")
# map[int(treasureLocation[0])-1][int(treasureLocation[1])-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

### Rock Paper Scissors Game
# What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
## Computer response must be random.randint(0,2)
## If commands will dictate who wins
## 0 beats 2 (rock beats scissors)
## 1 beats 0 (paper beats rock)
## 2 beats 1 (scissors beats rock)
## else draw

import random
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computerChoice = random.randint(0,2)

## Print out choices
rpsList = ["Rock", "Paper", "Scissors"]
print(f"\nYou chose {rpsList[userChoice]}\n")
print(f"\nComputer chose {rpsList[computerChoice]}\n")

### Winning choices
if userChoice == 0 and computerChoice == 2:
    print("Rocks beats Scissors\n")
    print("You Win")
elif userChoice == 1 and computerChoice == 0:
    print("Paper beats Rock\n")
    print("You Win")
elif userChoice == 2 and computerChoice == 1:
    print("Scissors beats Rock\n")
    print("You Win")
## Add in draw comparison
elif userChoice == computerChoice:
    print(f"{rpsList[userChoice]} meets {rpsList[computerChoice]}")
    print("Dead Heat")
else:
    print("Computer outsmarts you\n")
    print("You Lose")