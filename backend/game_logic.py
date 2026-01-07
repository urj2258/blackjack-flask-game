import random

def displayCards():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["♠","♥","♦","♣"]
    deck = [f"{suit}{rank}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def setupGame():
    deck = displayCards()
    player = []
    dealer = []
    player.append(deck.pop())
    player.append(deck.pop())
    dealer.append(deck.pop())
    dealer.append(deck.pop())
    return deck , player , dealer

def cardValues(cards):
    Values = []
    total = 0
    for card in cards:
        rank = card[1:]
        if rank in ['J', 'Q', 'K']:
            Values.append(10)
        elif rank == 'A':
            Values.append(11)
        else:
            Values.append(int(rank))
    
    total = sum(Values)
    ace_count = Values.count(11)
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    
    return total

def dealerTurn(dealer, deck):
    # Logic: Dealer hits until >= 17
    dealer_score = cardValues(dealer)  
    while dealer_score < 17:
        dealer.append(deck.pop())
        dealer_score = cardValues(dealer)  

def comparison(dealerSc ,playerSc):
    if dealerSc <  playerSc:
        return "WIN"
    elif dealerSc == playerSc:
        return "PUSH"
    else:
        return "LOSE"
