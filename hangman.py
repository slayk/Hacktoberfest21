import random
import hangman_art
import hangman_world
import os

end_of_game = False
chosen_word = random.choice(hangman_world.word_list).lower()
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(hangman_art.logo)
    print(hangman_art.stages[lives])
    print(f"{' '.join(display)}")
    
    guess = input(" Guess a letter : ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives-=1
    
    if lives < 0:
        print(f" You lose! The word was {chosen_word} ")
        end_of_game = True

    if "_" not in display:
        end_of_game = True
        print(" You win. ")
