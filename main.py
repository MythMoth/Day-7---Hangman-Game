# Import modules

from ASCII_art import logo
from ASCII_art import stages
from word_list import word_list
import random

# Welcome screen
print(logo + "\n\n")
print("Welcome to PyHangman! \n")

# Game Setup
game_over = False
num_lives = 6
chosen_word = random.choice(word_list)
guess_list = []
for letter in chosen_word:
    guess_list += "_"

# Game loop
while not game_over:
    guess_string = ""
    for i in guess_list:
        guess_string += i
    print(guess_string)
    guess = input("Guess a letter: ")
    i = 0

    correct_guess = False
    for letter in chosen_word:
        if guess == letter:
            guess_list[i] = letter
            correct_guess = True
        i += 1

    if not correct_guess:
        num_lives -= 1
    print(stages[num_lives])

    game_over = True
    for letter in guess_list:
        if letter == "_":
            game_over = False

    if game_over:
        print("You won!")
        print(f"The word was {chosen_word}")

    if num_lives == 0:
        print("You lost, Game over.")
        print(f"The word was {chosen_word}")
        game_over = True



