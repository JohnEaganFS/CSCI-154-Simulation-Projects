import random

# making random doors
# The car door index is chosen as random int between [0, doorAmt)
# Doors list declared as doorAmt 0's
# Change carDoor index to car (1)
def makeRandomDoors(doorAmt):
    carDoor = int(random.random() * doorAmt)
    doors = [0] * doorAmt # be careful with mutables, just working with ints so it's fine
    doors[carDoor] = 1
    return doors

# did the player win
# if the strategy is switch, return the opposite of isPlayerDoorCar (goat & switch -> car, car & switch -> goat)
# if stay strategy, return if player chose the car initially (isPlayerDoorCar)
# if player chooses random strat, choose a player decision randomly (0 -> stay, 1 -> switch). Return doSwitch != isPlayerDoorCar (0 != 0 -> Loss, 0 != 1 -> Win, 1 != 0 -> Win, 1 != 1 -> Loss)
def didPlayerWin(playerStrategy, isPlayerDoorCar):
    if playerStrategy == 0:  # always switch
        return not isPlayerDoorCar #implicit casting, cool
    elif playerStrategy == 1:  # never switch
        return bool(isPlayerDoorCar)
    else:  # switch randomly
        doSwitch = int(random.random() * 2)
        return doSwitch != isPlayerDoorCar

# functions for calculating the theoretical odds of winning for each variation and strategy
# Summary: Classic Switch (N - 1) / ((N-1)(N - p - 1)) where N = num of doors, p = doors opened by host. p = N - 2 for this simulation.
#          Classic Stay & Random Doors with any Strategy 1 / N.
def theoreticalOddsClassicSwitch(numberOfDoors, doorsOpened=None):
    if doorsOpened is None:
        doorsOpened = numberOfDoors - 2
    return (1 / numberOfDoors) * ((numberOfDoors - 1) / (numberOfDoors - doorsOpened - 1)) * 100

def theoreticalOddsClassicStay(numberOfDoors, doorsOpened=None):
    if doorsOpened is None:
        doorsOpened = numberOfDoors - 2
    return 1 / numberOfDoors * 100

def theoreticalOddsRandomDoors(numberOfDoors, doorsOpened=None):
    if doorsOpened is None:
        doorsOpened = numberOfDoors - 2
    return 1 / numberOfDoors * 100

