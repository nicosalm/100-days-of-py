# hangman game

import random

# generate a random word

from english_words import get_english_words_set # https://pypi.org/project/english-words/
web2lowerset = get_english_words_set(['web2'], lower=True)

the_word = random.choice(list(web2lowerset))
the_word = "apple"

# dictionary of characters and their status

dict = {}
dict = dict.fromkeys(the_word, False)
lives = 10

# print the word with blanks

print("Welcome to Hangman!")
print("You have 10 lives to guess the word.")
print("The word has", len(the_word), "letters.")
print("Good luck!")

print("The word is: ", end="")
print ("_ " * len(the_word))
print (" ")

# main loop

while lives > 0:
    user = input("Guess a letter: ")
    if (user in the_word):
        dict[user] = True
        print("Correct!")
        
        # print the word with blanks, but with correct letters filled in
        string = ""
        for key in dict:
            if dict[key] == True:
                string += key + " "
            else:
                string += "_ "
        if string == the_word:
            print("You win!")
            break
        print("The word is: ", end="")
        print(string)
        print(" ")
    else:
        lives -= 1
        print("Wrong!")
        if lives == 0:
            print("You lose!")
            print("The word was: ", end="")
            print(the_word)
            break
        print("You have", lives, "lives left.")
        print(" ")
            
    