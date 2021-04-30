import time
import random
random.seed(time.time())
cardValues = [1,2,3,4,5,6,7,8,9,10,10,10,10]
testAmt = 100000

def findScore(hitValue):
    sumValue = 0
    for i in range(0, testAmt, 1):
        card1 = cardValues[random.randint(0, 12)]
        card2 = cardValues[random.randint(0, 12)]

        handVal = card1 + card2

        while handVal <= hitValue:
            newCard = cardValues[random.randint(0, 12)]
            handVal += newCard

        if handVal > 21:
            handVal = 0

        sumValue += handVal

    avgScore = sumValue / testAmt
    print("Hitting on", str(hitValue) + ":", avgScore)

if __name__ == "__main__":
    for i in range(1, 21):
        findScore(i)
