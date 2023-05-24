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