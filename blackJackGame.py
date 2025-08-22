import random

def printBanner():
    print("+" + "="*45 + "+")
    print("|                                             |")
    print("|         🃏  WELCOME TO BLACKJACK  🃏        |")
    print("|                                             |")
    print("+" + "="*45 + "+")
    print("        ┌─────┐   ┌─────┐   ┌─────┐")
    print("        | A   |   | 10  |   |  K  |")
    print("        | ♠   |   | ♦   |   | ♥   |")
    print("        └─────┘   └─────┘   └─────┘")


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

def comparison(dealerSc ,playerSc):
    if dealerSc <  playerSc:
        print("+" + "-"*35 + "+")
        print("|         🌟  YOU WIN 🙌  🌟          |")
        print("+" + "-"*35 + "+")
    elif dealerSc == playerSc:
        print("+" + "-"*35 + "+")
        print("|        ⚖️  (PUSH) TIE 😅           |")
        print("+" + "-"*35 + "+")
    else:
        print("+" + "-"*35 + "+")
        print("|         💀  YOU LOSE 😓           |")
        print("+" + "-"*35 + "+")

def printCard(cards, hideCard = False):
    for i, card in enumerate(cards):
        suit = card[0]
        rank = card[1:]

        if hideCard  and i == 0:
            print("┌─────────┐")
            print("│░░░░░░░░░│")
            print("│░░░░░░░░░│")
            print("│░░░░░░░░░│")
            print("│░░░░░░░░░│")
            print("│░░░░░░░░░│")
            print("└─────────┘")
        else:
            print("┌─────┐")
            print(f"| {rank}   |")  
            print(f"| {suit}   |")
            print("└─────┘")
        print()

def playerTurn(player, deck):
    while True:
        userRequest = input("Type 'h' to draw a card or 's' to stop: ").lower()
        if userRequest == "h":
            player.append(deck.pop())   
            print("player Cards are: ")
            printCard(player, hideCard = False)
            player_score = cardValues(player)  
            print(f"So the total score you have is: {player_score}")
            if player_score > 21:
                print("You cant add more cards😓")
                break
        elif userRequest == "s":   
            break
        else:
            print("Invalid choice, type 'h' or 's'.")

def dealerTurn(dealer, deck):
    print("dealer Cards are: ")
    printCard(dealer, hideCard = False)  
    dealer_score = cardValues(dealer)  
    print(f"Total score of dealer is: {dealer_score}")
    while dealer_score < 17:
        dealer.append(deck.pop())
        print(f"As dealer score is below 17, dealer new Cards are: ")
        printCard(dealer, hideCard = False)
        dealer_score = cardValues(dealer)  
        print(f"Now dealer total score is : {dealer_score}")

def playGame():
    printBanner()
    print("--------- Lets start the game --------------")

    deck , player , dealer = setupGame()

    print("player Cards are: ")
    printCard(player, hideCard = False)
    print("dealer Cards are: ")
    printCard(dealer, hideCard = True)

    player_score = cardValues(player)

    if player_score == 21:
        print("--- Black Jack 🎊🎉 ---")
    else:
        playerTurn(player, deck)
        player_score = cardValues(player)
        if player_score > 21:
            print("You are BUSTED🔥😓")
        else:  
            dealerTurn(dealer, deck)
            dealer_score = cardValues(dealer)
            player_score = cardValues(player)
            if dealer_score > 21:
                print("+" + "-"*40 + "+")
                print("|        💥 DEALER IS BUSTED 💥          |")
                print("|             🌟 YOU WIN 🤭 🌟          |")
                print("+" + "-"*40 + "+")
            else:
                comparison(dealer_score, player_score)

def play_again():
    while True:
           playGame()
           choice = input("To play again enter 'y', if not enter 'n': ").lower()
           if choice == 'y':
               continue  
           elif choice == 'n':
               print("---- GAME OVER ----")
               break
           else:
               print("Invalid input! Try again.")
    

play_again()
