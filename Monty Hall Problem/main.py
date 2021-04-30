import random
import time
import matplotlib.pyplot as plt # ended up using excel with raw data for graphics

import customProblem # the file you want to look at for MHP implementation

# Driver function (no implementation here)
if __name__ == "__main__":
    random.seed(time.time())

    print("Custom: 0")
    inputSim = int(input("Enter: "))
    if inputSim == 0:
        inputDoorAmt = int(input("Enter amount of Doors: "))
        print("Player strategies: 0 - Always Switch  1 - Always Stay  2 - Random")
        inputPlayerStrategy = int(input("Enter your strategy: "))
        print("Host strategies: 0 - Classic  1 - Open Random Doors")
        inputHostStrategy = int(input("Enter host strategy: "))
        inputIterations = int(input("Enter number of iterations: "))

        start = time.time()
        wins, losses, avg = customProblem.customMHP(inputDoorAmt, inputPlayerStrategy, inputHostStrategy, inputIterations)
        elapsed = time.time() - start

        print("Input:", inputSim, inputDoorAmt, inputPlayerStrategy, inputHostStrategy, inputIterations)
        print("Wins:", wins)
        print("Losses:", losses)
        print("Average Win%:", avg)
        print("Time:", elapsed)



