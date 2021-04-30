import time
import random

import customGame

if __name__ == "__main__":
    random.seed(time.time())

    print("Player Policies: 0 - Stick >= 17  1 - Stick >= Hard 17  2 - Always Stick  3 - Hit < 21  4 - Hit Soft 17 or Dealer Has 4/5/6  5 - Hit on Soft 17  6 - Random Stick/Hit  7 - Basic Strategy")
    inputPolicy = int(input("Enter player policy: "))
    print("Deck Type: 0 - Infinite Deck  1 - Single Deck")
    inputDeck = int(input("Enter deck type: "))
    inputIterations = int(input("Enter number of games: "))

    start = time.time()
    wins, losses, ties, avg = customGame.customGame(inputPolicy, inputDeck, inputIterations)
    elapsed = time.time() - start

    print()
    print("Input:", inputPolicy, inputDeck, inputIterations)
    print("Wins:", wins)
    print("Losses:", losses)
    print("Ties:", ties)
    print("Average Win%:", avg)
    print("Time:", elapsed)