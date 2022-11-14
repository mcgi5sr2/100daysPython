## Beginnner Hangman

# Start
# Generate random word
# Generate as many blanks as letters in the word
# Ask the user to guess a letter
# IS the letter guessed in the word?
# Yes replace the blank with the letter
# No "Lose a Life"
# Are all the blanks filled If No, go back to Ask the user to guess a letter
# Have they run out of lives? if yes GameOver, if No go back to Ask the user to guess a letter

# #Step 1 
# import random
# word_list = ["aardvark", "baboon", "camel"]
# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen_word = random.choice(word_list)
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter: ").lower()
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#     if guess == letter:
#         print("Right")
#     else:
#         print("Wrong")

# #Step 2
# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #TODO-1: - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# display = []
# for letter in range(0, len(chosen_word)):
#     display.append("_")
# print(display)


# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# #guess = input("Guess a letter: ").lower()
# # i = 0
# # while i < int(len(chosen_word)):
# #     if chosen_word[i] == guess:
# #         display[i] = guess
# #     i += 1 

# # print(enumerate(chosen_word))
# # for index, letter in enumerate(chosen_word):
# #     if letter == guess:
# #         display[index] = guess
# # print(display)
# end_of_game = False
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#     word_length = len(chosen_word)
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter

# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
#     print(display)

#     if "_" not in display:
#         end_of_game = True
#         print("YouWin")

# #Step 4

# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
# #Set 'lives' to equal 6.
# lives = 6
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
# print(lives)  
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
    
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#     #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1. 
#     if guess not in chosen_word:
#         lives -= 1
#         print(stages[lives])
#     #If lives goes down to 0 then the game should stop and it should print "You lose."
#     if lives == 0:
#         print("YouLose")
#         end_of_game = True
#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
    
#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
      
#     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

#Step 5

import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess == "end":
        end_of_game = True
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    #if guess in display:
    #    print(f"You have already guessed: {guess}")
    if guess in guesses:
        print(f"You have already guessed: {guess}")
    else:
        guesses.append(guess)
    print(f"you have guessed:{guesses}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word: #and guess not in str(guesses):
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"The letter {guess} is not in the word uh oh")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])