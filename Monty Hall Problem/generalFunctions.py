import random

def makeRandomDoors(doorAmt):
    carDoor = int(random.random() * doorAmt)
    doors = [0] * doorAmt
    doors[carDoor] = 1
    return doors

def didPlayerWin(playerStrategy, isPlayerDoorCar):
    if playerStrategy == 0:  # always switch
        return not isPlayerDoorCar
    elif playerStrategy == 1:  # never switch
        return bool(isPlayerDoorCar)
    else:  # switch randomly
        doSwitch = int(random.random() * 2)
        return doSwitch != isPlayerDoorCar

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

