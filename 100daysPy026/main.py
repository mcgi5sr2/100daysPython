# list comprehension
# new_list = [new_item for item in list]
import random

numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]
# print(new_list)

name = "Angela"
letters = [letter for letter in name]
# print(letters)

range_to_be_doubled = range(1, 5)
double_range = [number * 2 for number in range_to_be_doubled]
# print(double_range)

# conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]

# square numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n * n for n in numbers]
#
# list_of_strings = input().split(',')
# list_of_ints = [int(n.strip()) for n in list_of_strings]
# list_of_odd_numbers = [n for n in list_of_ints if n%2 != 0]

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# students_scores = {student:random.randint(1, 100) for student in names}
# print(students_scores)
#
# passed_students = {students:score for (students, score) in students_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an unladen swallow?"
# dictionary = {words:(len(words)) for words in sentence.split() }
# print(dictionary)

# dict_temp_C = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 10, "Saturday": 16, "Sunday": 9}
# dict_temp_F = {day: temp * 9 / 5 + 32 for (day, temp) in dict_temp_C.items()}
# print(dict_temp_F)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # loop through a dict
# for (key, value) in student_dict.items():
#     print(value)
#
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# #loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)
#
# # loop through each of the rows of the data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     print(row.score)
#     if row.student == "Angela":
#         print(row.score)

