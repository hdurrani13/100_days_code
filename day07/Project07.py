# Project: Hang Man 
'-----------------------------'
import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)

print(logo)
# print(chosen_word)

place_holder = ""
game_over = False
lives = 6

# for position in range(len(chosen_word)):
#     place_holder += "_"

while len(chosen_word) != len(place_holder):
    place_holder += '_'
print(place_holder) 

correct_letters = []

while not game_over:

    print(f"**************************[ {lives}/6 lives left ]*************************")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guess {guess}.")
    
    display = ""

    for char in chosen_word:
        if guess == char:
            display += char
            correct_letters.append(guess)
        elif char in correct_letters:
            display += char
        else:
            display += "_"

    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word, you lose a life.")

    print(stages[-lives - 1])
    print(f'You have {lives} left.')

    if lives == 0:
        print(f"*******************[ The Word is '{chosen_word}' You Lose! ]*******************")
        game_over = True
    
    if "_" not in display:
        game_over = True
        print("You Win!")