### Loops

# ### Fruit Loops
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)

# ### Average Height 
# students_heights = input("Input a list of students heights ").split()
# for n in range(0, len(students_heights)):
#     students_heights[n] = int(students_heights[n])
# print(students_heights)

# ## use a for loop to calculate the len() and sum() of student_heights
# len = 0
# sum = 0

# for students in students_heights:
#     sum += students
#     len += 1

# print(F"The number of students or len is {len}")
# print(F"The sum students heights or sum is {sum}")
# print(f"The average height is {sum/len}")

# ### Highest Score  78 65 89 55 91 64 89
# student_scores = input("Input a list of Student Scores").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highestScore = 0
# for scores in student_scores:
#     if scores > highestScore:
#         highestScore = scores
# print(f"The Highest score is {highestScore}")
# print(f"The max student score is {max(student_scores)}")

## Using for loops with the range function
# range defaults to an increase of 1
# range stops and does not include the top boundary
# for <number> in range(a,b,<steps>)
#    do...
# total = 1
# for number in range(0, 101,2):
#     total += number
#     print(number)
# print(total)

### FIZZ BUZZ
## If divisible by 3 say fizz
## If divisible by 5 say buzz
## If divisible by 5 and 3 say fizzbuzz
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

### Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# len(letters) == 52
# len(symbols) == 9

# loop to print nr_letters, then nr_symbols, then nr_numbers
# for pwordLetters in range (0, nr_letters):
#     print(letters[random.randint(0,51)], end='')
# for pwordSymbols in range (0, nr_symbols):
#     print(symbols[random.randint(0,8)], end='')
# for pwordNumbers in range (0, nr_numbers):
#     print(numbers[random.randint(0,9)], end='')
# print()

# pwordList = []
# for pwordLetters in range (0, nr_letters):
#     pwordList.append(letters[random.randint(0,51)])
# for pwordSymbols in range (0, nr_symbols):
#     pwordList.append(symbols[random.randint(0,8)])
# for pwordNumbers in range (0, nr_numbers):
#     pwordList.append(numbers[random.randint(0,9)])
# #print(pwordList)
# random.shuffle(pwordList)
# pwordList = ''.join(pwordList)
# print(pwordList)

### Given answer even more concise
# password = ""
# for char in range(1, nr_letters +1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols +1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers +1):
#     password += random.choice(numbers)
# print(password)

passwordList = []
for char in range(1, nr_letters +1):
    passwordList += random.choice(letters)
for char in range(1, nr_symbols +1):
    passwordList += random.choice(symbols)
for char in range(1, nr_numbers +1):
    passwordList += random.choice(numbers)
random.shuffle(passwordList)
password = ""
for char in passwordList:
    password += char
print(password)