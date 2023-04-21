import time
import random
from english_words import get_english_words_set # https://pypi.org/project/english-words/

name = input("What is your name? ")
print ("Hello, " + name, "– Time to play hangman!")

time.sleep(1) # 1 second delay

print ("Start guessing...")
time.sleep(0.5)

# here we set the secret word.
web2lowerset = get_english_words_set(['web2'], lower=True)
word = random.choice(list(web2lowerset))

guesses = ''
turns = 10

# while the turns are more than zero
while turns > 0:         
    
    failed = 0   
              
    for char in word:      
        if char in guesses:    
            print (char,end=""),    
        else:
            print ("_",end=""),     
            failed += 1    

    if failed == 0:        
        print (" ... You won")
        break            
    
    guess = input(" ... guess a character: ") 
    guesses += guess                    

    if guess not in word:  
        turns -= 1
        print ("Wrong")  
        print ("You have", + turns, 'more guesses' )
        if turns == 0:           
            print ("You Lose"  )