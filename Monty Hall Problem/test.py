import random
import time
import matplotlib.pyplot as plt

import generalFunctions
import customProblem

M = 10000
ITERATION_LIST = [10, 100, 1000, 10000, 100000]
DOOR_LIST = [3, 6, 9, 20, 100]

def printResults(iterations, avgDev):
    print("Iterations:", iterations)
    print("Average Deviation(n = " + str(M) + "):", avgDev, "\n")

def calcDeviation(avg, theoretical):
    return abs(avg - theoretical) / theoretical * 100

def test(numDoors, player, host, iterations, theoretical):
    avgDeviation = 0
    for j in range(M):
        avg = customProblem.customMHP(numDoors, player, host, iterations)[2]
        avgDeviation += calcDeviation(avg, theoretical)
    avgDeviation /= M
    printResults(iterations, avgDeviation)

if __name__ == "__main__":
    start = time.time()
    random.seed(time.time())
    print("Classic Monty Hall (3, 6, 9, 20, 100)")
    # Classic Monty Hall (3, 6, 9, 20, 100)
    # Iterations 10, 100, 1000, 10000, 100000

    print("================================================\n")
    print("Player Strategy: Always Switch")
    # Switch
    for d in DOOR_LIST:
        print("------------------------------------------------")
        print(d, "Doors")
        theory = generalFunctions.theoreticalOddsClassicSwitch(d)
        print("Theoretical:", theory, "\n")
        for i in ITERATION_LIST:
            test(d, 0, 0, i, theory)

    print("================================================\n")
    print("Player Strategy: Always Stay")
    # Stay
    for d in DOOR_LIST:
        print("------------------------------------------------")
        print(d, "Doors")
        theory = generalFunctions.theoreticalOddsClassicStay(d)
        print("Theoretical:", theory, "\n")
        for i in ITERATION_LIST:
            test(d, 1, 0, i, theory)

    print("++++++++++++++++++++++++++++++++++++++++++++++++")
    print("================================================")
    print("++++++++++++++++++++++++++++++++++++++++++++++++\n")

    print("Host Opens Random Doors (3, 6, 9, 20, 100)")
    # Host Opens Random Doors (3, 6, 9, 20, 100)
    # Iterations 10, 100, 1000, 10000, 100000

    print("================================================\n")
    print("Player Strategy: Always Switch")
    # Switch
    for d in DOOR_LIST:
        print("------------------------------------------------")
        print(d, "Doors")
        theory = generalFunctions.theoreticalOddsRandomDoors(d)
        print("Theoretical:", theory, "\n")
        for i in ITERATION_LIST:
            test(d, 0, 1, i, theory)

    print("================================================\n")
    print("Player Strategy: Always Stay")
    # Stay
    for d in DOOR_LIST:
        print("------------------------------------------------")
        print(d, "Doors")
        theory = generalFunctions.theoreticalOddsRandomDoors(d)
        print("Theoretical:", theory, "\n")
        for i in ITERATION_LIST:
            test(d, 1, 1, i, theory)
    elapsed = time.time() - start
    print("Time:", elapsed)