"""Blackjack, by Eray
The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack

Tags: large, game, card game"""

import random, sys

# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = "backside"

def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True: # Keep asking until they enter a valid amount.
        print("How much do you bet? (1-{}, or QUIT)".format(maxBet))
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Player entered a valid bet.
        

def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank),suit)) # Add the face and ace cards.
        for rank in ("J","Q","K","A"):
            deck.append((rank, suit)) # Add the face and ace cards.
    random.shuffle(deck)
    return deck