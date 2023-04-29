# higher lower game, using the higher lower api
from game_data import data as game_data
import random
from art import logo, vs
import os

def format(account):
    """format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

# generate a random account from the game data
def get_random_account():
    """Get data from random account."""
    return random.choice(game_data)

print(get_random_account()["name"])

def check_answer(guess, a, b):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.
    """
    if a["follower_count"] > b["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"
    
def clear():
  """Clears the terminal
  """
  os.system('cls' if os.name == 'nt' else 'clear')
    
def game():
    # display art
    print(logo)
    
    # generate a random account from the game data
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()
    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Against B: {format(account_b)}") 
    
    while game_should_continue:
        # ask user for a guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        # check if user is correct
        # get follower count of each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, account_a, account_b)
        # give user feedback on their guess
        # score keeping
        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            account_a = account_b
            account_b = get_random_account()
            print(f"Compare A: {format(account_a)}")
            print(vs)
            print(f"Against B: {format(account_b)}") 
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
        
if __name__ == "__main__":
    game()