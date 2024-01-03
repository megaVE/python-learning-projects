import art
import random

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


def draw_card():
    """Gets a new card from the deck"""
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    
    return random.choice(cards)

def show_cards(player_cards, cpu_cards):
    """Prints the player cards and the first card from the CPU"""
    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {cpu_cards[0]}")

def check_sum(deck):
    sum = 0
    ace_counter = 0

    for card in deck:
        if card == 'A':
            sum += 1
            ace_counter += 1
        elif card == 'J' or card == 'Q' or card == 'K':
            sum += 10
        else:
            sum += card
    
    for _ in range(ace_counter):
        if sum + 10 <= 21:
            sum += 10
        else:
            break

    return sum

def end_game(player_cards, cpu_cards):
    print(f"Your final hand: {player_cards}")
    print(f"Computer's final hand: {cpu_cards}")
    
    print("[RESULT]", end=' ')
    if check_sum(player_cards) == check_sum(cpu_cards) or check_sum(player_cards) > 21 and check_sum(cpu_cards) > 21:
        print("Draw!")
    elif check_sum(player_cards) > check_sum(cpu_cards) or check_sum(cpu_cards) > 21:
        print("You Win!")
    else:
        print("You Lost!")

print(art.logo)

while True:
    player_cards = [draw_card(), draw_card()]
    cpu_cards = [draw_card(), draw_card()]

    computer_wants_card = True
    player_wants_card = True
    while check_sum(player_cards) < 21 and check_sum(cpu_cards) < 21 and (computer_wants_card or player_wants_card):
        show_cards(player_cards, cpu_cards)
        more_cards = input("> Type 'y' to get another card, type 'n' to pass: ")
        
        if more_cards == 'y':
            player_cards.append(draw_card())
            player_wants_card = True
        else:
            player_wants_card = False

        if 21 - check_sum(cpu_cards) > 6:
            cpu_cards.append(draw_card())
            print("The computer picked up another card")
        else:
            computer_wants_card = False

    end_game(player_cards, cpu_cards)

    if input("> Do you want to play again? Type 'y' or 'n': ") != 'y':
        break