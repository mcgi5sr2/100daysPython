### Takes a two digit number and sums the separate digits
# number = input("Enter a two digit number: ")
# print(number)
# digitOne = number[0]
# digitTwo = number[1]
# print(digitOne + "+" + digitTwo + "= " )
# answer = int(digitOne)+int(digitTwo)
# print(answer)

### BMI indicator
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # BMI is weight/height^2

# BMI = int(weight)/(float(height)**2)
# print(int(BMI))

### f-string add the character f infront of the string 
# print(f"yourscore is {score}, your {height is {height}, you are winning is {isWinning}")
# not that all the data types are within the "" string

# ## Life in Weeks
# age = input("What is your current age? ")

# #calc the number of days weeks and months left if you were to live to 90
# # 365 days in a year
# # 52 weeks in a year
# # 12 months in a year
# years_remaining = 90 - int(age)
# days = years_remaining * 365
# weeks = years_remaining * 52
# months = years_remaining * 12

# # out should be 
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

## Tip calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
people = int(input(("How many people to split the bill? ")))

#calculate tip as 1.%% then multiply by total bill
totalBill = ((tip/100)*bill) + bill
finalBill = "{:.2f}".format(totalBill/people)
output = f"Each person should pay {finalBill}"
print(output)