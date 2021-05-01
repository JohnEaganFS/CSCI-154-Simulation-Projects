import time
import random

# Calculates the possible hand values (soft and hard)
# First checks if there are any aces.
# If so, count the number of aces and find every possible pairing of those aces as 1's and 11's
# The possible hand values will be the sum of the rest of the cards (sum(cards) - numAces) + those combinations of 1's and 11's
# Only add hands to the handValues list if it's <= 21 because everything else is a bust. [] implies no non-bust hands i.e. bust
# If no aces, just sum the card values and append if <= 21.
def calcHandValues(cards):
    haveAces = 1 in cards  # check if aces in hand
    handValues = []  # initially no hands, can only add a hand if it won't bust
    if haveAces:  # Aces Case
        numAces = cards.count(1)
        possibleAces = [(x,y) for x in [0,1,2,3,4] for y in [0,1,2,3,4] if x + y == numAces]  # make every (x,y) pair of the num of aces counting as 1 or 11 (x -> 1, y -> 11)
        temp = sum(cards) - numAces                                                           # Ex: I have two aces. (0,2) or (1,1) or (2,0) => two 11's or one 1, one 11 or two 1's
        possibleHands = [temp + (x * 1) + (y * 11) for (x,y) in possibleAces]  # add the rest of the cards with those possible ace values
        for i in possibleHands:
            if i <= 21:
                handValues.append(i)
    else:  # No aces (hard hand)
        temp = sum(cards)  # simply sum the card values
        if temp <= 21:
            handValues.append(temp)
    return handValues

# Basic Strategy for Soft hands
# Simply copies the logic for the following chart:
# https://www.blackjackapprenticeship.com/wp-content/uploads/2018/10/mini-blackjack-strategy-chart.png
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

# Basic Strategy for Hard hands
# Simply copies the logic for the following chart:
# https://www.blackjackapprenticeship.com/wp-content/uploads/2018/10/mini-blackjack-strategy-chart.png
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

# Hit or Stand for the Player Decisions
# This is where all the policies are implemented
# This function looks at the player's cards, dealer's cards, and the player policy to make the decision of HIT or STAND
def hitOrStand(playerCards, dealerCards, policy):
    handValues = calcHandValues(playerCards)
    # python 3.10 switch case would make this so much cleaner
    if policy == 0:                                     # Stand >= 17
        for i in handValues:
            if i >= 17:
                return "STAND"
        return "HIT"
    elif policy == 1:                                   # Stand >= Hard 17
        if handValues[len(handValues) - 1] >= 17: # last hand value will always be smallest according to calcHandValues (11's used first)
            return "STAND"
        else:
            return "HIT"
    elif policy == 2:                                   # Always Stand
        return "STAND"
    elif policy == 3:                                   # Hit < 21
        if handValues[0] < 21:
            return "HIT"
        return "STAND"
    elif policy == 4:                                   # Hit <= Soft 17 and stand on dealer 4,5,6
        if len(handValues) > 1 and handValues[0] == 17:
            return "HIT"
        if dealerCards[0] in [4,5,6]: # if dealer is showing a 4, 5, 6 on first card, stand
            return "STAND"
        else:
            return "HIT"
    elif policy == 5:                                   # Copy the dealer strategy
        if len(handValues) > 1 and handValues[0] == 17:
            return "HIT"
        for i in handValues:
            if i >= 17:
                return "STAND"
        return "HIT"
    elif policy == 6:                                   # Randomly hit/stand
        hit = int(random.random() * 2)
        if hit:
            return "HIT"
        else:
            return "STAND"
    else:                                               # Basic Strategy
        hasSoft = len(handValues) > 1
        if hasSoft:
            return basicStrategySoft(handValues[0], dealerCards[0])
        else:
            return basicStrategyHard(handValues[0], dealerCards[0])

# Picking cards from a single deck
# This implementation relies on the deck "losing" cards as cards are drawn
# What it really does is pick a card from the available cards and swaps that card with the first card available in the deck
# It then increments the firstCard value such that the chosen card (swapped one) is no longer in range
# Ex: [1,2,3,4] Let's say we choose 3.
#     [3,2,1,4] Swap 3 and first card i.e. 1.
#     firstCard = 0 + 1 = 1  The first available card is now set to index 1, which is 2 so the 3 can no longer be accessed.
# This modified deck and the first card that should be available are returned to maintain the deck across multiple player decisions (multiple HITs).
def pickCardsSingle(deck, cardAmt, firstCard):
    deckLength = 52 - firstCard
    for i in range(cardAmt):
        card = int(random.random() * deckLength) + firstCard
        deck[firstCard], deck[card] = deck[card], deck[firstCard]
        firstCard += 1
        deckLength = 52 - firstCard
    return deck, firstCard

# SINGLE DECK BLACKJACK
# Sets up the initial deck that the player and dealer will be drawing from.
# Picks two cards which will be the player's.
# Picks two more which will be the dealer's.
# The player performs his decisions first and continues until he decides to STAND, busts, or hits 21.
# Dealer then goes and acts according to the dealer strategy.
# If both the player and dealer don't bust or hit 21, they have a showdown.
# Their biggest hand values are compared and whoever has bigger wins or a tie for equal hands.
def singleDeck(policy):
    deckStart = 0  # initially no cards chosen
    deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]  # initial deck
    deck, deckStart = pickCardsSingle(deck, 2, deckStart)  # update deck and deckStart
    playerCards = [deck[0], deck[1]]  # player gets the first two cards chosen

    deck, deckStart = pickCardsSingle(deck, 2, deckStart)  # update deck and deckStart
    dealerCards = [deck[2], deck[3]]  # dealer gets next two cards

    playerDecision = ""
    while playerDecision != "STAND":  # player makes a decision until he stands, busts, or hits 21
        handValues = calcHandValues(playerCards)  # calculate handvalues
        if handValues == []:  # empty handValues means you busted
            return False
        if handValues[0] == 21:  # if 21, player wins
            return True
        playerDecision = hitOrStand(playerCards, dealerCards, policy)  # make player decision
        if playerDecision == "HIT":  # if hit, pick another card and add to player's cards
            deck, deckStart = pickCardsSingle(deck, 1, deckStart)
            playerCards.append(deck[deckStart - 1])

    dealerDecision = ""
    while dealerDecision != "STAND":  # same as player
        handValues = calcHandValues(dealerCards)
        if handValues == []:  # bust
            return True
        if handValues[0] == 21:  # blackjack, win
            return False
        if handValues[0] == 17 and len(handValues) == 2:  # if more than one handValue, then there is a soft hand at index 0
            dealerDecision = "HIT"  # hit on soft 17
        elif handValues[0] >= 17:  # stand on anything > 17 or on hard 17
            dealerDecision = "STAND"
        else:
            dealerDecision = "HIT"  # otherwise (< 17), hit
        if dealerDecision == "HIT":  # if hit, pick a card and add to hand
            deck, deckStart = pickCardsSingle(deck, 1, deckStart)
            dealerCards.append(deck[deckStart - 1])

    #SHOWDOWN
    playerCardValue = calcHandValues(playerCards)[0]
    dealerCardValue = calcHandValues(dealerCards)[0]

    # Win = 1
    # Loss = 0
    # Tie = 2
    if playerCardValue > dealerCardValue:
        return 1  # player win
    elif playerCardValue < dealerCardValue:
        return 0  # player loss
    else:
        return 2  # tie

# Pick cards from an infinite deck
# Simply defines the possible values for the cards and picks one value randomly
# This could have been simplified with one of each value except 10 which would have four instances for the 10, J, Q, K, but I thought this better represented the idea of choosing any from a complete deck.
def pickCardsInfinite():
    infinite = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9,
                    9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    card = int(random.random() * 52)
    return infinite[card]

# INFINITE DECK
# Performs essentially the same game as Single Deck except that cards are drawn using pickCardsInfinite(). No maintaining of deck required.
def infiniteDeck(policy):
    playerCards = [pickCardsInfinite(), pickCardsInfinite()]

    dealerCards = [pickCardsInfinite(), pickCardsInfinite()]

    playerDecision = ""
    while playerDecision != "STAND":
        handValues = calcHandValues(playerCards)
        if handValues == []:
            return False
        if handValues[0] == 21:
            return True
        playerDecision = hitOrStand(playerCards, dealerCards, policy)
        if playerDecision == "HIT":
            playerCards.append(pickCardsInfinite())

    dealerDecision = ""
    while dealerDecision != "STAND":
        handValues = calcHandValues(dealerCards)
        if handValues == []:
            return True # Dealer Bust
        if handValues[0] == 21:
            return False # Dealer Blackjack
        if handValues[0] == 17 and len(handValues) == 2:
            dealerDecision = "HIT"
        elif handValues[0] >= 17:
            dealerDecision = "STAND"
        else:
            dealerDecision = "HIT"
        if dealerDecision == "HIT":
            dealerCards.append(pickCardsInfinite())

    #SHOWDOWN
    playerCardValue = calcHandValues(playerCards)[0]
    dealerCardValue = calcHandValues(dealerCards)[0]

    # Win = 1
    # Loss = 0
    # Tie = 2
    if playerCardValue > dealerCardValue:
        return 1  # player win
    elif playerCardValue < dealerCardValue:
        return 0  # player loss
    else:
        return 2  # tie

# Keeps track of wins, losses, ties, avg.
def customGame(playerPolicy, deckType, n):
    random.seed(time.time())
    wins = 0
    losses = 0
    ties = 0

    for i in range(n):
        if deckType:
            wonGame = singleDeck(playerPolicy)
        else:
            wonGame = infiniteDeck(playerPolicy)
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