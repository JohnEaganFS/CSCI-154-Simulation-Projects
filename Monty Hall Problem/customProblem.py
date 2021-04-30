import generalFunctions # more implementation of MHP
import random

# classic MHP
# Input is list of doors (Ex: [0,0,1]) and player strategy
# Output is bool of "Did player win?" (true/false)
def classic(doors, playerStrategy):
    numberOfDoors = len(doors) # get num of doors
    isPlayerDoorCar = doors[int(random.random() * numberOfDoors)]   # Initial choice. Set player door car to any one of the doors (0 = Goat, 1 = Car).
                                                                    # isPlayerDoorCar acts as integer bool for player choosing car door (0/1).
    for i in range(numberOfDoors - 2): # remove N - 2 doors with goats
        doors.remove(0) # remove 0 so only remove goats

    return generalFunctions.didPlayerWin(playerStrategy, isPlayerDoorCar) # return whether player won or not. Look at generalFunctions.py for exact implementation.

# falling host variation
# Input and output same as classic MHP above
def openRandom(doors, playerStrategy):
    numberOfDoors = len(doors)
    isPlayerDoorCar = doors[int(random.random() * numberOfDoors)] # Initial choice
    if isPlayerDoorCar:     # if player chooses car door initially, the car door can't get removed so go ahead and just return if player won or not based on strategy (switch/stay)
        return generalFunctions.didPlayerWin(playerStrategy, isPlayerDoorCar) # switch -> lose, stay -> win, independent of variation
        # this could be simplified to: if playerStrategy == 0: return false else: return true ¯\_( ツ )_/¯
    for i in range(numberOfDoors - 2): # else, if player door isn't the car, the car could get removed. N - 2 doors accidentally opened.
        randomDoor = int(random.random() * (numberOfDoors - 1)) # get a random door from doors (not including player's door)
        if randomDoor == 0: # if the door chosen is door 0, car is considered removed (could have tracked exact car door index, but this produces the same thing with less code)
            return False
        numberOfDoors -= 1 # decrement number of doors because there is one less door to consider

    return generalFunctions.didPlayerWin(playerStrategy, isPlayerDoorCar)

# Driver function for implementing data tracking of wins/losses.
# Goes through iterations and calls appropriate MHP variation based on player, host, doorAmt.
def customMHP(doorAmt, playerStrategy, hostStrategy, iterations):
    wins = 0
    losses = 0

    for i in range(iterations):
        doors = generalFunctions.makeRandomDoors(doorAmt)   # making random doors based on doorAmt
        if hostStrategy == 0:  # classic
            wonGame = classic(doors, playerStrategy)
        elif hostStrategy == 1:  # falling host
            wonGame = openRandom(doors, playerStrategy)
        else: # just in case ¯\_( ツ )_/¯
            print("No, stop that.")
            wonGame = True
        if wonGame:
            wins += 1
        else:
            losses += 1
    avg = wins / iterations * 100
    return wins, losses, avg
