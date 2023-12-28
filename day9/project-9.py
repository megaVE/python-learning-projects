import art
import os

print(art.logo)
print("Welcome to the secret auction program.")

bids = {}
has_one_more_person = True

while has_one_more_person:
    name = input("What is your name? ")
    bid = float(input("What's your bid?: $"))
    
    bids[name] = bid

    one_more_person = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if(one_more_person != 'yes'):
        has_one_more_person = False
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

winner_name = ""
winner_bid = -1.0
for key in bids:
    if(bids[key] > winner_bid):
        winner_name = key
        winner_bid = bids[key]

print(f"\nThe winner is {winner_name} with a bid of ${winner_bid}")