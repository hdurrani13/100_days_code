# Project: Rock Paper Scissors
"--------------------------------"
import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

list1 = [rock, paper, scissors]

# User Choice for rock paper scissors (0 1 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Condition to print the image for user 
if user_choice >= 0 and user_choice <= 2:
    print("You chose:")
    print(list1[user_choice])

# Print computer's choice image 
random_choice = random.randint(0, 2)
print("Computer chose:")
print(list1[random_choice])

# Conditions for the entire rock paper scissors game
if user_choice >= 3 or user_choice < 0:
    print("Invalid Number, You Lose!")
elif user_choice == 0 and random_choice == 2:
    print("You Win!")
elif random_choice == 0 and user_choice == 2:
    print("You Lose!") 
elif random_choice > user_choice:
    print("You Lose!")
elif user_choice > random_choice:
    print("You Win!")
elif random_choice == user_choice:
    print("It's a draw!")
elif user_choice >= 3 or user_choice < 0:
    print("Invalid Number, You Lose!")

