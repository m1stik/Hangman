#Importing libraries and assets
#Library 'replit' is used -> pip install replit
import random
from replit import clear
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

#Defining main variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
end_of_game = False
lives = 6

print(logo)

#Create blanks
for _ in range(word_length):
    display += "_"

#Main loop keeping the game up
while not end_of_game:
    #Input a letter
    guess = input("Guess a letter: ").lower()

    #Clearing ternimal
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        #Take life if wrong
        lives -= 1
        if lives == 0:
            #End game if 0 lives
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    #Display graphics
    print(stages[lives])