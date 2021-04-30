import time
import random

cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
random.seed(time.time())

def pickCardsSingle(deck, cardAmt, firstCard):
    deckLength = 52 - firstCard
    for i in range(cardAmt):
        card = int(random.random() * deckLength) + firstCard
        #print("FirstCard:", firstCard)
        #print("card:", card)
        deck[firstCard], deck[card] = deck[card], deck[firstCard]
        firstCard += 1
        deckLength = 52 - firstCard
    return deck, firstCard

def calcHandValues(cards):
    haveAces = 1 in cards
    handValues = []
    if haveAces:
        numAces = cards.count(1)
        possibleAces = [(x,y) for x in [0,1,2,3,4] for y in [0,1,2,3,4] if x + y == numAces]
        temp = sum(cards) - numAces
        possibleHands = [temp + (x * 1) + (y * 11) for (x,y) in possibleAces]
        for i in possibleHands:
            if i <= 21:
                handValues.append(i)
    else:
        temp = sum(cards)
        if temp <= 21:
            handValues.append(temp)
    return handValues

def basicStrategySoft(handVal, dealerCard):
    if handVal > 18:
        return "STAND"
    elif handVal == 18:
        if dealerCard in [9,10,1]:
            return "HIT"
        else:
            return "STAND"
    else:
        return "HIT"

def basicStrategyHard(handVal, dealerCard):
    if handVal >= 17:
        return "STAND"
    elif handVal > 12:
        if dealerCard in [6,7,8,9,10,1]:
            return "HIT"
        else:
            return "STAND"
    elif handVal == 12:
        if dealerCard in [4,5,6]:
            return "STAND"
        else:
            return "HIT"
    else:
        return "HIT"

def hitOrStand(playerCards, dealerCards, policy):
    handValues = calcHandValues(playerCards)
    #print(handValues)
    if policy == 0:
        for i in handValues:
            if i >= 17:
                return "STAND"
        return "HIT"
    elif policy == 1:
        if handValues[len(handValues) - 1] >= 17:
            return "STAND"
        else:
            return "HIT"
    elif policy == 2:
        return "STAND"
    elif policy == 3:
        if handValues[0] < 21:
            return "HIT"
        return "STAND"
    elif policy == 4:
        if len(handValues) > 1 and handValues[0] == 17:
            return "HIT"
        if dealerCards[0] in [4,5,6]:
            return "STAND"
        else:
            return "HIT"
    elif policy == 5:
        if len(handValues) > 1 and handValues[0] == 17:
            return "HIT"
        for i in handValues:
            if i >= 17:
                return "STAND"
        return "HIT"
    elif policy == 6:
        hit = int(random.random() * 2)
        if hit:
            return "HIT"
        else:
            return "STAND"
    else:
        hasSoft = len(handValues) > 1
        if hasSoft:
            return basicStrategySoft(handValues[0], dealerCards[0])
        else:
            return basicStrategyHard(handValues[0], dealerCards[0])


def singleDeck(policy):
    deckStart = 0
    #deck = [x for x in range(52)]
    deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    deck, deckStart = pickCardsSingle(deck, 2, deckStart)
    playerCards = [deck[0], deck[1]]
    #print("Player:", playerCards)

    deck, deckStart = pickCardsSingle(deck, 2, deckStart)
    dealerCards = [deck[2], deck[3]]

    playerDecision = ""
    while playerDecision != "STAND":
        handValues = calcHandValues(playerCards)
        if handValues == []:
            #print("Player BUST")
            return False
        if handValues[0] == 21:
            #print("Player BLACKJACK")
            return True
        playerDecision = hitOrStand(playerCards, dealerCards, policy)
        if playerDecision == "HIT":
            deck, deckStart = pickCardsSingle(deck, 1, deckStart)
            playerCards.append(deck[deckStart - 1])
        #print(playerDecision)
        #print("PlayerCardsAfter:", playerCards)

   # print("Dealer:", dealerCards)
    dealerDecision = ""
    while dealerDecision != "STAND":
        handValues = calcHandValues(dealerCards)
        if handValues == []:
            #print("Dealer BUST")
            return True
        if handValues[0] == 21:
            #print("Dealer BLACKJACK")
            return False
        if handValues[0] == 17 and len(handValues) == 2:
            dealerDecision = "HIT"
        elif handValues[0] >= 17:
            dealerDecision = "STAND"
        else:
            dealerDecision = "HIT"
        if dealerDecision == "HIT":
            deck, deckStart = pickCardsSingle(deck, 1, deckStart)
            dealerCards.append(deck[deckStart - 1])
        #print(dealerDecision)
        #print("DealerCardsAfter:", dealerCards)

    playerCardValue = calcHandValues(playerCards)[0]
    dealerCardValue = calcHandValues(dealerCards)[0]

    #print("SHOWDOWN")
    #print("Player:", playerCards, "=", playerCardValue)
    #print("Dealer:", dealerCards, "=", dealerCardValue)
    # Win = 1
    # Loss = 0
    # Tie = 2
    if playerCardValue > dealerCardValue:
        #print("Player WINS")
        return 1
    elif playerCardValue < dealerCardValue:
        #print("Player LOSES")
        return 0
    else:
        #print("Player and Dealer TIE")
        return 2

def pickCardsInfinite():
    infinite = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9,
                    9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    card = int(random.random() * 52)
    return infinite[card]

def infiniteDeck(policy):
    playerCards = [pickCardsInfinite(), pickCardsInfinite()]
    #print("Player:", playerCards)

    dealerCards = [pickCardsInfinite(), pickCardsInfinite()]

    playerDecision = ""
    while playerDecision != "STAND":
        handValues = calcHandValues(playerCards)
        if handValues == []:
            #print("Player BUST")
            return False
        if handValues[0] == 21:
            #print("Player BLACKJACK")
            return True
        playerDecision = hitOrStand(playerCards, dealerCards, policy)
        if playerDecision == "HIT":
            playerCards.append(pickCardsInfinite())
        #print(playerDecision)
        #print("PlayerCardsAfter:", playerCards)

    #print("Dealer:", dealerCards)
    dealerDecision = ""
    while dealerDecision != "STAND":
        handValues = calcHandValues(dealerCards)
        if handValues == []:
            #print("Dealer BUST")
            return True
        if handValues[0] == 21:
            #print("Dealer BLACKJACK")
            return False
        if handValues[0] == 17 and len(handValues) == 2:
            dealerDecision = "HIT"
        elif handValues[0] >= 17:
            dealerDecision = "STAND"
        else:
            dealerDecision = "HIT"
        if dealerDecision == "HIT":
            dealerCards.append(pickCardsInfinite())
        #print(dealerDecision)
        #print("DealerCardsAfter:", dealerCards)

    playerCardValue = calcHandValues(playerCards)[0]
    dealerCardValue = calcHandValues(dealerCards)[0]

    #print("SHOWDOWN")
    #print("Player:", playerCards, "=", playerCardValue)
    #print("Dealer:", dealerCards, "=", dealerCardValue)
    # Win = 1
    # Loss = 0
    # Tie = 2
    if playerCardValue > dealerCardValue:
        #print("Player WINS")
        return 1
    elif playerCardValue < dealerCardValue:
        #print("Player LOSES")
        return 0
    else:
        #print("Player and Dealer TIE")
        return 2

    # print("Player:", playerCards)
    # print("Dealer:", dealerCards)
    # print("Deck:", deck)

def customGame(playerPolicy, deckType, n):
    wins = 0
    losses = 0
    ties = 0

    for i in range(n):
        if deckType:
            wonGame = singleDeck(playerPolicy)
            #print("--------------------------------------------------------")
        else:
            wonGame = infiniteDeck(playerPolicy)
            #print("--------------------------------------------------------")
        if wonGame == 1:
            wins += 1
        elif wonGame == 0:
            losses += 1
        else:
            ties += 1

    if n - ties == 0:
        return wins, losses, ties, 0
    avg = wins / (n - ties) * 100
    return wins, losses, ties, avg