import random
#from the words file, import variable words
from words import words
import string

def get_valid_word(words):
    
    #randomly select a word from the list
    word = random.choice(words)

    while '-' in word or ' ' in word:
         #randomly select a word from the list
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet=set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    
    lives = 10
    #user input
    while len(word_letters) > 0 and lives > 0:

        #letters used
        print('You have used these letters: ', ' '.join(used_letters))
        print(f"You have {lives} live(s) left.")

        #what the current word is (W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        #if this is a valid character (user letter) in the alphabet that hasnt been used yet, add to the used_letter set
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                #word letters decreases in size each time user correctly guesses the letter
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not included in the word")
            
        elif user_letter in used_letters:
            print("You have already used that character. Try again")

        else:
            print("Invalid chracter, try again!")

    if lives==0:
        print(f'You died! The word was {word}')
    else:
        print("You guessed the word ", word, '!')
    
hangman()         


