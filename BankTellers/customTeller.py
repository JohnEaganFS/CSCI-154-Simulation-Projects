import time
import math
import heapq
import queue
import numpy

# Customer arrives event
# When customer arrives, they'll check each teller choose the first one is idle.
# If there are none available, the customer (arrival time, work units) is pushed on the waiting line.
def customerArrives(time, windows, workUnits, eventQueue, waitingQueue):
    ct = 0 # teller index
    for teller in windows:  # for each teller, see if they are idle or not
        if teller[0] == "IDLE": # if teller is idle, push onto event queue a becomeBusy event
            heapq.heappush(eventQueue, (time, 1, ct, workUnits))
            return
        ct += 1 # go to next teller
    waitingQueue.put((time, workUnits)) # no tellers idle, wait in line

# Teller becomes busy event
# The teller becomes busy and the time it will take to perform the work is calculated.
# The teller will become idle at the current time + how long it will take to complete the task.
def becomeBusy(time, windows, teller, workUnits, eventQueue):
    windows[teller][0] = "BUSY"  # become busy
    timeTaken = math.ceil(workUnits / windows[teller][1] * 60)  # calculate time to perform work (WU / WU/h) * 60 = hours to complete work * 60 = minutes to complete work
    heapq.heappush(eventQueue, (time + timeTaken, 2, teller))  # push onto event queue for teller to become idle at current time + timeTaken

# Teller becomes idle event
# When teller finishes a job, they become idle.
# Before doing so, check the waiting line and see if there are any customers.
# If so, get them from the queue and calculate how long they were waiting based on current time - arrival time of customer
# Push become busy event at current time (start work immediately). This could be changed to have a slightly more accurate representation where it takes time for teller to signal customer, customer to get to window, etc.
# Else (no customers), just become idle and wait.
def becomeIdle(time, windows, teller, eventQueue, waitingQueue):
    if not waitingQueue.empty():  # check waiting line
        customer = waitingQueue.get()
        waitingTime = time - customer[0]  # calc waiting time
        heapq.heappush(eventQueue, (time, 1, teller, customer[1]))  # become busy
        return 1, waitingTime  # return waiting time and if a waiter is now being served
    else:
        windows[teller][0] = "IDLE"  # become idle
        return 0, 0  # return no waiting time and no waiter being served

# General Teller without a priority queue for small requests
# Initializes the teller and customer amount, hours of work, etc.
# Event queue (events) is a priority queue based on time
# events filled with exogenous events (customers arriving and end of workday)
# While events is not empty, get next event and act according to event number.
# Simulation ends (breaks) once event 3 (endOfWorkDay) is reached.
def generalTeller(windows, tellerEfficiency, customers, hours):
    N = windows
    M = customers
    hours = hours
    minutes = hours * 60
    numpy.random.seed(int(time.time()))

    tellers = []
    for i in range(N):
        tellers.append(["IDLE", tellerEfficiency])
    #tellers = [["IDLE", 10]] * N # can't do this with mutables if you want to change values inside ("IDLE" -> "BUSY")
    waiting = queue.Queue()

    events = []

    # 0 = arrive
    # 1 = becomeBusy
    # 2 = becomeIdle
    # 3 = endOfWorkDay
    randList = numpy.random.normal(10, 0.5, M) # generate a random list of work units for each customer according to normal distribution
    randIndex = 0
    for i in range(0, minutes, math.ceil(minutes/M)): # customers arrive in uniform distribution minutes / num of customers
        randWork = randList[randIndex]  # get random work-units
        while randWork < 5.0 or randWork > 15.0:            # while the value isn't in the truncated range, make up a new value
            randWork = numpy.random.normal(10, 0.5, 1)[0]
        heapq.heappush(events, (i, 0, randWork))  # push the customer arrive event into the events queue
        randIndex += 1 # increment to get next work unit value for next iteration

    heapq.heappush(events, (480, 3)) # push the end of work day exogenous event
    jobsDone = 0
    waitingTime = 0
    waitersServed = 0
    while not len(events) == 0: # while events not empty
        event = heapq.heappop(events) # pop an event
        eventTime = event[0]
        eventAction = event[1]
        if eventAction == 0: # customer arrival
            work = event[2]
            customerArrives(eventTime, tellers, work, events, waiting)
        elif eventAction == 1: # teller becomes busy
            tellerIndex = event[2]
            work = event[3]
            becomeBusy(eventTime, tellers, tellerIndex, work, events)
        elif eventAction == 2: # teller becomes idle
            jobsDone += 1
            tellerIndex = event[2]
            x, y = becomeIdle(eventTime, tellers, tellerIndex, events, waiting)
            if x:
                waitingTime += y
                waitersServed += x
        else:  # end of work day
            break

    stillWorking = 0
    for i in tellers: # see how many tellers still working
        if i[0] == "BUSY":
            stillWorking += 1
    if jobsDone == 0: # no jobs completed, need to define waiting time as something
        return jobsDone, waiting.qsize(), stillWorking, 9999999
    if waitersServed: # return waiting time as total waiting time / waiters served
        return jobsDone, waiting.qsize(), stillWorking, int(waitingTime / waitersServed)
    else: # else, just return 0 if no one had to wait or no waiters were served
        return jobsDone, waiting.qsize(), stillWorking, 0

# Customer arrives (priority queue)
def customerArrivesLight(time, windows, workUnits, eventQueue, waitingQueue, lightQueue):
    ct = 0
    for teller in windows:
        if teller[0] == "IDLE":
            heapq.heappush(eventQueue, (time, 1, ct, workUnits))
            return
        ct += 1
    if workUnits <= 9.5:  # if the work units is less than or equal to 9.5, the customer is a priority and gets put on the light queue
        lightQueue.put((time, workUnits))
    else:
        waitingQueue.put((time, workUnits))

# Teller becomes busy (priority queue)
# same as becomeBusy
def becomeBusyLight(time, windows, teller, workUnits, eventQueue):
    windows[teller][0] = "BUSY"
    timeTaken = math.ceil(workUnits / windows[teller][1] * 60)
    heapq.heappush(eventQueue, (time + timeTaken, 2, teller))

# Teller becomes idle (priority queue)
def becomeIdleLight(time, windows, teller, eventQueue, waitingQueue, lightQueue):
    if not lightQueue.empty(): # check the light queue first because these are priority customers
        customer = lightQueue.get()
        waitingTime = time - customer[0]
        heapq.heappush(eventQueue, (time, 1, teller, customer[1]))
        return 1, waitingTime
    elif not waitingQueue.empty():
        customer = waitingQueue.get()
        waitingTime = time - customer[0]
        heapq.heappush(eventQueue, (time, 1, teller, customer[1]))
        return 1, waitingTime
    else:
        windows[teller][0] = "IDLE"
        return 0, 0

# Priority queue teller system for small requests
# Same as the generalTeller but adds a lightWaiting queue for small requests.
def priorityTeller(windows, tellerEfficiency, customers, numhours):
    N = windows
    M = customers
    hours = numhours
    minutes = hours * 60
    numpy.random.seed(int(time.time()))

    tellers = []
    for i in range(N):
        tellers.append(["IDLE", tellerEfficiency])
    #tellers = [["IDLE", 10]] * N
    waiting = queue.Queue()
    lightWaiting = queue.Queue() # new light queue for small requests

    events = []

    # 0 = arrive
    # 1 = becomeBusy
    # 2 = becomeIdle
    # 3 = endOfWorkDay
    randList = numpy.random.normal(10, 0.5, M)
    randIndex = 0
    for i in range(0, minutes, math.ceil(minutes/M)):
        randWork = randList[randIndex]
        while randWork < 5.0 or randWork > 16.0:
            randWork = numpy.random.normal(10, 0.5, 1)[0]
        heapq.heappush(events, (i, 0, randWork))
        randIndex += 1

    heapq.heappush(events, (480, 3))
    jobsDone = 0
    waitingTime = 0
    waitersServed = 0
    while not len(events) == 0: # while events not empty
        event = heapq.heappop(events)
        eventTime = event[0]
        eventAction = event[1]
        if eventAction == 0:
            work = event[2]
            customerArrivesLight(eventTime, tellers, work, events, waiting, lightWaiting)
        elif eventAction == 1:
            tellerIndex = event[2]
            work = event[3]
            becomeBusyLight(eventTime, tellers, tellerIndex, work, events)
        elif eventAction == 2:
            jobsDone += 1
            tellerIndex = event[2]
            x, y = becomeIdleLight(eventTime, tellers, tellerIndex, events, waiting, lightWaiting)
            if x:
                waitingTime += y
                waitersServed += x
        else:
            break

    stillWorking = 0
    for i in tellers:
        if i[0] == "BUSY":
            stillWorking += 1

    if jobsDone == 0: # jobs waiting is now from both queues
        return jobsDone, waiting.qsize() + lightWaiting.qsize(), stillWorking, 9999999

    if waitersServed:
        return jobsDone, waiting.qsize() + lightWaiting.qsize(), stillWorking, int(waitingTime / waitersServed)
    else:
        return jobsDone, waiting.qsize() + lightWaiting.qsize(), stillWorking, 0