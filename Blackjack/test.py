import time
import random

import customGame

def test(playerStrat, deckType, n):
    wins, losses, ties, avg = customGame.customGame(playerStrat, deckType, n)
    print("Wins:", wins)
    print("Losses:", losses)
    print("Ties:", ties)
    print("Average Win% (n = " + str(n) + "):", avg)

if __name__ == "__main__":
    start = time.time()
    random.seed(time.time())
    ITERATIONS = 100000000
    PLAYER_STRATEGIES = ["Stand >= 17", "Stick >= Hard 17", "Always Stick", "Hit < 21", "Hit Soft 17 or Dealer Has 4/5/6", "Hit on Soft 17", "Random Stick/Hit", "7 - Basic Strategy"]

    print("=====================INFINITE DECK======================")

    for i in range(len(PLAYER_STRATEGIES)):
        print("--------------------------------------------------------")
        print("Player Strategy: " + PLAYER_STRATEGIES[i])
        test(i, 0, ITERATIONS)

    print()
    print("========================================================")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("========================================================\n")

    print("======================SINGLE DECK=======================")
    for i in range(len(PLAYER_STRATEGIES)):
        print("--------------------------------------------------------")
        print("Player Strategy: " + PLAYER_STRATEGIES[i])
        test(i, 1, ITERATIONS)

    elapsed = time.time() - start
    print("Time:", elapsed)