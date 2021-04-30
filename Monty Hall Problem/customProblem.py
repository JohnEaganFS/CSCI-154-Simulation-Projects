import generalFunctions
import random


def classic(doors, playerStrategy):
    numberOfDoors = len(doors)
    isPlayerDoorCar = doors[int(random.random() * numberOfDoors)]
    for i in range(numberOfDoors - 2):
        doors.remove(0)

    return generalFunctions.didPlayerWin(playerStrategy, isPlayerDoorCar)

def openRandom(doors, playerStrategy):
    numberOfDoors = len(doors)
    isPlayerDoorCar = doors[int(random.random() * numberOfDoors)]
    if isPlayerDoorCar:
        return generalFunctions.didPlayerWin(playerStrategy, isPlayerDoorCar)

    for i in range(numberOfDoors - 2):
        randomDoor = int(random.random() * (numberOfDoors - 1))
        if randomDoor == 0:
            return False
        numberOfDoors -= 1

    return generalFunctions.didPlayerWin(playerStrategy, isPlayerDoorCar)

def customMHP(doorAmt, playerStrategy, hostStrategy, iterations):
    wins = 0
    losses = 0

    for i in range(iterations):
        doors = generalFunctions.makeRandomDoors(doorAmt)
        if hostStrategy == 0:  # classic
            wonGame = classic(doors, playerStrategy)
        elif hostStrategy == 1:  # random doors
            wonGame = openRandom(doors, playerStrategy)
        else:
            wonGame = True
        if wonGame:
            wins += 1
        else:
            losses += 1
    avg = wins / iterations * 100
    return wins, losses, avg
