# Debugging 

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

# my_function()


'''
from random import randint
dice_image = ["1","2","3","4","5","6"]
dice_num = randint(1, 5)

print(dice_image[dice_num])
'''

# year = int(input("What's your year of birth? \n"))

# if year >= 1980 and year <= 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")


'''
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed in an invalid error. Please try again with a numerical response.")
    age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at your {age}.")
'''

'''
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page += int(input("Number of words per page: "))
total_words = pages * word_per_page

print(total_words)
'''
'''
# Using Debugger

import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
'''
'''
try:
    age = int(input("How old are you?\n"))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical input")
    age = int(input("How old are you?\n"))
if age >= 18:
    print(f"You can drive at {age}.")
else:
    print("You need to be 18 to drive.")
'''
'''
Word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
Word_per_page = int(input("Number of words per page: "))
print(Word_per_page)
total_words = pages * Word_per_page
print(total_words)
'''

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."