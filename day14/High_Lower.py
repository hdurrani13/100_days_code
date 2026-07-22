# Imports
from art import logo, vs
from game_data import data
import random

def format_data(account):
    '''Formats the account data into printable format'''
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"\n{account_name},\n{account_description},\nFrom: {account_country}\n")

def check_answer(guess, A_followers, B_followers):
    '''Take the users guess and followers count and return if they got it right'''
    if A_followers > B_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display art
print(logo)
score = 0
account_B = random.choice(data)

while True:
    # Generate random accounts 
    account_A = account_B
    account_B = random.choice(data) 

    # Makes sure A /= b
    if account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Compare B: {format_data(account_B)}")

    # Ask the user 
    guess = input("who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 50)
    print(logo)
    
    A_follower_count = account_A["follower_count"]
    B_follower_count = account_B["follower_count"]
    is_correct = check_answer(guess, A_follower_count, B_follower_count)

    # Give user feedback
    if is_correct:
        score += 1
        print(f"You are right! {score}\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break






