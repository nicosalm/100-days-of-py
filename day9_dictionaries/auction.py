"""
    This program is a blind auction, where bidders enter their name and bid, and the highest bidder wins.
"""
import os
from time import sleep
from art import logo as auction_logo

print(auction_logo) # art

# prompt for initial bid
name = input("What is your name? ")
bid = int(input("What is your bid? $"))
bids = {name: bid}
bidding = True

# prompt for other bidders
while bidding:
    other_bidders = input("Are there any other bidders? (yes/no) ")
    if other_bidders == "yes":
        os.system('cls' if os.name == 'nt' else 'clear') # clear screen
        print(auction_logo)
        name = input("What is your name? ")
        bid = int(input("What is your bid? $"))
        bids[name] = bid
    else:
        bidding = False

highest_bid = 0
winner = "" 

# find highest bidder in bids
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder

print("Calculating highest bidder...")
sleep(2) # sleep for 2 seconds, for dramatic effect
print(f"{winner} with a bid of ${highest_bid}.")