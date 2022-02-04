import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  #randomly chooeses somehting from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    lives = 6
    
    #getting the user input
    while len(word_letters) > 0 and lives > 0:
        #letters already used
        print("You have ", lives,  "lives left and you have used these letters: "," ".join(used_letters))
        
        #what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: "," ".join(word_list))        
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 
                print("That letter is not in the word")
        elif user_letter in used_letters:
            print("You have already used that character. Try a new one")
        else:
            print('Invalid character. Type another one please')
            
    #gets here when en(word_letters) == 0
    if lives == 0:
        print('Game over, the word was: ', word)
    else:
        print('You guessed the word', word, '!!!')
    

hangman()
    