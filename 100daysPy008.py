# ## Caesars Cypher Day 008 of 100 Python
# # Simple Function
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()

# # Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do, {name}?")
#     print("Isn't the weather nice today?")

# greet_with_name("Angela")

# # Functions with more than one input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with("Jack Bauer", "Nowhere")
# greet_with(name = "Jack Bauer", location = "Nowhere")

# # Paint Coverage
# # number of cans = (wall height * wall width) / coverage per can (5m**2)

# import math
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# def paint_calc(height, width, cover):
# #    cansOfPaint = (round(height*width)/cover)
#     cansOfPaint = (math.ceil((height*width)/cover))
#     print(f"you'll need {cansOfPaint} cans of paint")
#     return (cansOfPaint)

# paint_calc(height=test_h, width=test_w, cover=coverage)
# #print(f"you'll need {cansOfPaint} cans of paint")

# Prime number checker
# def prime_checker(number):
#     i = 2
#     while i < number:
#         if number % i == 0:
#             print(f"{number} is not a Prime")
#             return
#         i += 1
#     print(f"{number} is a Prime")
#     return

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#         if is_prime:
#             print(f"It's a prime number.")
#         else:
#             print(f"It's not a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)
