# rock paper scissors game
import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("The rules are simple: rock beats scissors, scissors beats paper, and paper beats rock. Best of 3!")
    
    # create a dictionary of the possible choices
    choices = {"rock": 0, "paper": 1, "scissors": 2}
    
    # create a dictionary of the possible outcomes
    outcomes = {"win": 0, "lose": 1, "tie": 2}
    
    user_strikes = 0
    computer_strikes = 0
    
    # now, let's play the game, best of 3
    while user_strikes < 2 and computer_strikes < 2:
        user_choice = input("Please enter your choice (rock, paper, or scissors): ")
        computer_choice = random.choice(list(choices.keys()))
        
        # determine the outcome
        outcome = (choices[user_choice] - choices[computer_choice]) % 3
        if outcome == outcomes["win"]:
            print("You win!")
            computer_strikes += 1
            
        elif outcome == outcomes["lose"]:
            print("You lose!")
            user_strikes += 1
            
        else:
            print("It's a tie!")
            continue
        
        print("Your score: ", user_strikes)
        print("Computer score: ", computer_strikes)
        
    if user_strikes == 2:
        print("You win the game!")
    else:
        print("You lose the game!")
        
if __name__ == "__main__":
    main()
    
