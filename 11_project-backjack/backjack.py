"""
    BLACKJACK
    
    Simple terminal blackjack game with a single player and dealer. 
    ⊛ The player can hit or stand. The dealer will hit until their hand is greater than 17. 
    ⊛ The player can only see one of the dealer's cards. 
    ⊛ Betting: The player may begin with a certain amount of money. 
      They can bet a certain amount each round. If they win, they get double their bet. 
      If they lose, they lose their bet. If they tie, they get their bet back. 
      If they run out of money, the game ends.
    ⊛ The player can play again if they have money left.
    
    Good luck!
"""

import os 
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
  """The deal function deals 2 random cards

  Args:
      deck (list): the deck of cards

  Returns:
      list: the hand with the 2 cards
  """
  hand = [] # create a hand
  for i in range(2): # deal 2 cards
    random.shuffle(deck)
    card = deck.pop()
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)
  return hand # return the hand with the 2 cards
  
def play_again():
  """Assess if the player wants to play again, if yes, the game restarts, if not, the game ends
  """
  again = input("Do you want to play again? (Y/N): ").lower()
  if again == "y":
    dealer_hand = []
    player_hand = []
    deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
    game()
    
  else:
    print("See you next time!")
    exit()
  
def total(hand):
  """Sums the total of the hand

  Args:
      hand (list): the hand of the player

  Returns:
      int: the total of the hand
  """
  
  total = 0
  for card in hand:
    # J, Q, K have a value of 10
    if card == 'J' or card == 'Q' or card == 'K':
      total += 10
    # A has a value of 1 or 11
    elif card == 'A':
      if total >= 11: total += 1
      else: total += 1
    else:
      total += card
  return total
  
def hit(hand):
  """Adds a card to the hand

  Args:
      hand (list): the hand of the player

  Returns:
      list: the hand with the new card added
  """
  card = deck.pop()
  if card == 11: card = "J"
  if card == 12: card = "Q"
  if card == 13: card = "K"
  if card == 14: card = "A"
  hand.append(card)
  return hand
  

def clear():
  """Clears the terminal
  """
  os.system('cls' if os.name == 'nt' else 'clear')

def print_results(dealer_hand, player_hand):
  """Prints the results of the game

  Args:
      dealer_hand (list): the hand of the dealer
      player_hand (list_): the hand of the player
  """
  clear()
  print("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
  print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
  
def blackjack(dealer_hand, player_hand):
  """Checks if blackjack has been met

  Args:
      dealer_hand (list): the hand of the dealer
      player_hand (list): the hand of the player
  """
  if total(player_hand) == 21:
    print_results(dealer_hand, player_hand)
    print("Blackjack!")
    play_again()
  
def score(dealer_hand, player_hand):
  """Evalutes the score of the game

  Args:
      dealer_hand (list): the hand of the dealer
      player_hand (list): the hand of the player
  """
  if total(player_hand) == 21:
    print_results(dealer_hand, player_hand)
    print("Blackjack!")
  elif total(dealer_hand) == 21:
    print_results(dealer_hand, player_hand)
    print("Dealer wins!")
  elif total(player_hand) > 21:
    print_results(dealer_hand, player_hand)
    print("You busted!")
  elif total(dealer_hand) > 21:
    print_results(dealer_hand, player_hand)
    print("Dealer busted!")
  elif total(player_hand) < total(dealer_hand):
    print_results(dealer_hand, player_hand)
    print("Dealer wins!")
  elif total(player_hand) > total(dealer_hand):
    print_results(dealer_hand, player_hand)
    print("You win!")
  else:
    print_results(dealer_hand, player_hand)
    print("Push!")

def game():
  """The gameplay loop
  """
  choice = 0
  clear()
  print ("WELCOME TO BLACKJACK!\n")
  dealer_hand = deal(deck)
  player_hand = deal(deck)
  print ("The dealer is showing a " + str(dealer_hand[0]))
  print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
  blackjack(dealer_hand, player_hand)
  quit=False
  while not quit:
      choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
      if choice == 'h':
          hit(player_hand)
          print(player_hand)
          if total(player_hand)>21:
              print('You busted')
              play_again()
      elif choice=='s':
          while total(dealer_hand)<17:
              hit(dealer_hand)
              print(dealer_hand)
              if total(dealer_hand)>21:
                  print('Dealer busts, you win!')
                  play_again()
          score(dealer_hand,player_hand)
          play_again()
      elif choice == "q":
          print("Bye!")
          quit=True
          exit()
  
if __name__ == "__main__":
  game()