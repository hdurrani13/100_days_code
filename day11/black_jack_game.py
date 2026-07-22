# Project: BlackJack
# -------------------------------------- #

import random
import day14.art as art
'''
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
def deal_card():
    user_card = []
    computer_card = []

    if len(user_card) != 2:
        user_card += random.sample(cards,2)
    if len(computer_card) != 2:
        computer_card += random.sample(cards,2)
    
    print(user_card)
    print(computer_card)

deal_card()
'''

def deal_card():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Lose, opponent has blackJack!"
    elif u_score == 0:
        return "Win, BlackJack!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "opponent went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You Lose!"

def play_game():
    print(art.logo)
    user_card = []
    computer_card = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your card: {user_card}, current score: {user_score}")
        print(f"Computer first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}.")
    print(f"Opponent final hand: {computer_card}, final score: {computer_score}.")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # print("\n" * 50)
    play_game()