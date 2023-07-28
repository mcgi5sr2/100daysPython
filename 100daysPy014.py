### 100daysPy014
## Higher Lower Game

# Import gameData & art
import Py014gameData
import Py014art
from Py014gameData import data
from Py014art import logo, vs
from random import randint
print(logo)


# choose a random dictionary item from the list
def compare(): 
    compare = data[randint(0,len(data))]
    print(f"Compare A: {compare['name']}, {compare['description']}, {compare['country']}")
    return compare['follower_count']

first = compare()
print(first)
print(vs)
second = compare()
print(second)
userChoice = input(print(f"Who has more followers? Type 'A' or 'B': "))

# print the info from this dictionary item EXCEPT the follower count
# store the follower count as a variable
#print vs

# choose a random new dictionary item from the list
# print the info from this dictioanry item EXCEPT the follower count
# store the follower count as a new variable

# User input higher or lower
# if higher followercountA > followercountB
# if lower followercountA < followercountB