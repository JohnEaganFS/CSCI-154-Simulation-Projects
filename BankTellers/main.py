import time
import math
import heapq
import queue
import numpy

def customerArrives(time, windows, workUnits, eventQueue, waitingQueue):
    ct = 0
    for teller in windows:
        if teller[0] == "IDLE":
            heapq.heappush(eventQueue, (time, 1, ct, workUnits))
            return
        ct += 1
    waitingQueue.put((time, workUnits))

def becomeBusy(time, windows, teller, workUnits, eventQueue):
    windows[teller][0] = "BUSY"
    #print("Teller:", teller, "starting job")
    timeTaken = math.ceil(workUnits / windows[teller][1] * 60)
    heapq.heappush(eventQueue, (time + timeTaken, 2, teller))

def becomeIdle(time, windows, teller, eventQueue, waitingQueue):
    #print("Teller:", teller, "finishing job")
    if not waitingQueue.empty():
        customer = waitingQueue.get()
        waitingTime = time - customer[0]
        heapq.heappush(eventQueue, (time, 1, teller, customer[1]))
        return 1, waitingTime
    else:
        windows[teller][0] = "IDLE"
        return 0, 0

# Driver function for your own testing. Enjoy.
if __name__ == "__main__":
    N = int(input("Number of Tellers/Windows: "))
    M = int(input("Number of Customers: "))
    hours = int(input("Number of Hours: "))
    tellerEfficiency = int(input("Teller Efficiency: "))
    minutes = hours * 60
    numpy.random.seed(int(time.time()))

    tellers = []
    for i in range(N):
        tellers.append(["IDLE", tellerEfficiency])
    # tellers = [["IDLE", 10]] * N
    waiting = queue.Queue()

    events = []

    # 0 = arrive
    # 1 = becomeBusy
    # 2 = becomeIdle
    # 3 = endOfWorkDay
    randList = numpy.random.normal(10, 0.5, M)
    # for i in range(len(randList)):
    #    num = randList[i]
    #    while num < 5.0 or num > 15.0:
    #        num = numpy.random.normal(10, 0.5, 1)[0]
    #     randList[i] = num
    randIndex = 0
    for i in range(0, minutes, math.ceil(minutes / M)):
        randWork = randList[randIndex]
        while randWork < 5.0 or randWork > 15.0:
            randWork = numpy.random.normal(10, 0.5, 1)[0]
        heapq.heappush(events, (i, 0, randWork))
        randIndex += 1

    heapq.heappush(events, (480, 3))
    jobsDone = 0
    waitingTime = 0
    waitersServed = 0
    while not len(events) == 0:  # while events not empty
        event = heapq.heappop(events)
        eventTime = event[0]
        eventAction = event[1]
        # print(event)
        if eventAction == 0:
            work = event[2]
            customerArrives(eventTime, tellers, work, events, waiting)
        elif eventAction == 1:
            tellerIndex = event[2]
            work = event[3]
            becomeBusy(eventTime, tellers, tellerIndex, work, events)
        elif eventAction == 2:
            jobsDone += 1
            tellerIndex = event[2]
            x, y = becomeIdle(eventTime, tellers, tellerIndex, events, waiting)
            if x:
                # print(y)
                waitingTime += y
                waitersServed += x
        else:
            break

    stillWorking = 0
    for i in tellers:
        if i[0] == "BUSY":
            stillWorking += 1

    print()
    print("Jobs Done:", jobsDone)
    print("Still Waiting:", waiting.qsize())
    print("Still Working:", stillWorking)
    if waitersServed:
        #print("Average Waiting Time:", int(waitingTime / waitersServed))
        print("Average Waiting Time:", int(waitingTime / jobsDone))
    else:
        print("Average Waiting Time:", 0)
    print("DONE")



