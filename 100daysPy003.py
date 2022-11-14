# #### 100 days Python 003
# # # RollerCoaster Rider
# print("Welcome to the rollercoaster!")
# height = int(input("what is your height in cm? "))
# if height >= 120:
#     age = int(input("what is your age? "))
#     if age <= 12:
#         print("Child ickets are $5")
#         bill = 5
#     elif age > 12 and age <18:
#         print("Youth tickets are $7")
#         bill = 7
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         print("Adult tickets are $12")
#         bill = 12

#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your final bill is {bill}")
# #     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# ## Odd or Even
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("Number is Even")
# else:
#      print("Number is Odd")

# ## BMI indicator v2.0
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # BMI is weight/height^2
# BMI = round(weight/height**2)
# print(f"Your BMI is {int(BMI)} you are ", end="")
# if BMI <= 18.5:
#     print("Underweight")
# elif BMI <= 25:
#     print("Normal Weight")
# elif BMI <= 30:
#     print("Overweight")
# elif BMI <= 35:
#     print("Obese")
# else:
#     print("Clinically obese")

# ### Leap Year Calculator
# year = int(input("Which year do you want to check? "))
# ## On every year that is divisible by 4
# ### except every year that is evenly divisible by 100
# #### unless the year is also evenly divisibly by 400
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 != 0:
#             print("This is not a leap year")
#         else:
#             print("This is a leap year")
#     else: 
#         print("This is a leap year")    
# else:
#     print("This is not a leap year")

# #### Love Calcualtor
# print("Wlcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# ### Take both peoples names and check for the number of times the letters in the word TRUE occures. Then heck for the number of times the leteers in the work LOVE ocurs. Then combine these numbers to make a two digit number.
# ## for each name:
# ## += 1 for each TRUEcount (tens)
# ## += 1 for each LOVEcount (units)
# ## use .lower() function
# ## use the .count() function to give the number of times a letter occurs in a string
# ## IF score <10 or >90 "Your score is x, you go together like coke and mentos."
# ## IF score >40 and <50 "Your score is y, you are alright together."
# names = name1.lower() + name2.lower()
# tens = names.count("t") + names.count("r") + names.count("u") + names.count("e")
# units = names.count("l") + names.count("o") + names.count("v") + names.count("e")
# print(f"TRUE letters occur {tens} times")
# print(f"LOVE letters occur {units} times")
# score = str(tens) + str(units)
# print(f"The score is {score}")
# if int(score) < 10 or int(score) > 90:
#         print(f"Your score is {score}, you go together like coke and mentos!")
# elif int(score) > 40 and int(score) < 50:
#         print(f"Your score is {score}, you are alright together.")
# else:
#         print(f"Your score is {score}")

### recurring function
N = 0
int(input(N))
def star_print(number):
    if number >=1:
        print("*" * number)
        return star_print (number - 1)
    #print()
star_print(N)

# ## Treasure Island
# print(```
#   ` : | | | |:  ||  :     `  :  |  |+|: | : : :|   .        `              .
#       ` : | :|  ||  |:  :    `  |  | :| : | : |:   |  .                    :
#          .' ':  ||  |:  |  '       ` || | : | |: : |   .  `           .   :.
#                 `'  ||  |  ' |   *    ` : | | :| |*|  :   :               :|
#         *    *       `  |  : :  |  .      ` ' :| | :| . : :         *   :.||
#              .`            | |  |  : .:|       ` | || | : |: |          | ||
#       '          .         + `  |  :  .: .         '| | : :| :    .   |:| ||
#          .                 .    ` *|  || :       `    | | :| | :      |:| |
#  .                .          .        || |.: *          | || : :     :|||
#         .            .   . *    .   .  ` |||.  +        + '| |||  .  ||`
#      .             *              .     +:`|!             . ||||  :.||`
#  +                      .                ..!|*          . | :`||+ |||`
#      .                         +      : |||`        .| :| | | |.| ||`     .
#        *     +   '               +  :|| |`     :.+. || || | |:`|| `
#                             .      .||` .    ..|| | |: '` `| | |`  +
#   .       +++                      ||        !|!: `       :| |
#               +         .      .    | .      `|||.:      .||    .      .    `
#           '                           `|.   .  `:|||   + ||'     `
#   __    +      *                         `'       `'|.    `:
# "'  `---"""----....____,..^---`^``----.,.___          `.    `.  .    ____,.,-
#     ___,--'""`---"'   ^  ^ ^        ^       """'---,..___ __,..---""'
# --"'                           ^                         ``--..,_____________
# ```)
# print("\nWelcome to Treasure Island.\n")
# print("Your mision is to find the treasure\n")
# decisionOne = input("You arrive at a mysterious junction, do you want to go Left, or Right? \n").lower()
# if decisionOne == "right":
#     print("You wander down the road for so long, you forget who you are, and what you were after...\n")
#     print("GameOver")
# elif decisionOne == "left":
#     decisionTwo = input("You arrive at a dark pier do you Wait or Swim? \n").lower()
#     if decisionTwo == "wwim":
#         print("You swim out into the docks, only to feel something reach up from the darkness and drag you under\n")
#         print("GameOver")
#     elif decisionTwo == "wait":
#         print("You wait long enough to see a giant otter offer you a lift down the river, after some great conversation he drops you off at a waterfall\n")
#         decisionThree = input("The waterfall has a Yellow door to the left, a Blue door in the middle, and a Red door on the right, which color door do you take?\n").lower()
#         if decisionThree == "yellow":
#             print("You find a wide array of dandelions, you have never experienced true happiness before this point in you life!\n")
#             print("YouWin!\n")
#         elif decisionThree == "blue":
#             print("The door opens, and more water pours forth filling your nostrils in a most unpleasant fashion\n")
#             print("GameOver")
#         elif decisionThree == "red":
#             print("The door explodes open, its a backdraft, if 90s film has taught me anything, this is probably fatal...\n")
#             print("GameOver")
#         else: 
#             print("Who knows what you wrote but it wasn't a color, maybe try just the color....\n")
#             print("GameOver")
#     else:
#         print("You spend so long the docks, you pick up work and start unloading boats... \n")
#         print("GameOver")
# else:
#     print("You get bored and go home without and dinner\n")
#     print("GameOver")
# print(f"{decisionOne} was decisionOne\n")
# print(f"{decisionTwo} was decisionTwo\n")
# print(f"{decisionThree} was decisionThree")