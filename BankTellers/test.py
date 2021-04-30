import tellerGeneralFunctions
import time

ITERATIONS = 10000

def printResults(a, b, c, d):
    print("Jobs Done:", int(a))
    print("Jobs Waiting:", int(b))
    print("Active Jobs:", int(c))
    print("Average Wait Time:", int(d))


if __name__ == "__main__":
    start = time.time()
    print("------------------------------------------")
    print("Original Problem")
    print("------------------------------------------")
    jobsDone = 0
    customersWaiting = 0
    activeJobs = 0
    avgWait = 0
    for i in range(ITERATIONS):
        w, x, y, z = tellerGeneralFunctions.generalTeller(10, 10, 160, 8)
        jobsDone += w
        customersWaiting += x
        activeJobs += y
        avgWait += z
    jobsDone /= ITERATIONS
    customersWaiting /= ITERATIONS
    activeJobs /= ITERATIONS
    avgWait /= ITERATIONS
    printResults(jobsDone, customersWaiting, activeJobs, avgWait)
    print("------------------------------------------")

    print("One More Window")
    print("------------------------------------------")
    jobsDone = 0
    customersWaiting = 0
    activeJobs = 0
    avgWait = 0
    for i in range(ITERATIONS):
        w, x, y, z = tellerGeneralFunctions.generalTeller(11, 10, 160, 8)
        jobsDone += w
        customersWaiting += x
        activeJobs += y
        avgWait += z
    jobsDone /= ITERATIONS
    customersWaiting /= ITERATIONS
    activeJobs /= ITERATIONS
    avgWait /= ITERATIONS
    printResults(jobsDone, customersWaiting, activeJobs, avgWait)
    print("------------------------------------------")

    print("One Less Window")
    print("------------------------------------------")
    jobsDone = 0
    customersWaiting = 0
    activeJobs = 0
    avgWait = 0
    for i in range(ITERATIONS):
        w, x, y, z = tellerGeneralFunctions.generalTeller(9, 10, 160, 8)
        jobsDone += w
        customersWaiting += x
        activeJobs += y
        avgWait += z
    jobsDone /= ITERATIONS
    customersWaiting /= ITERATIONS
    activeJobs /= ITERATIONS
    avgWait /= ITERATIONS
    printResults(jobsDone, customersWaiting, activeJobs, avgWait)
    print("------------------------------------------")

    print("Small Request Priority")
    print("------------------------------------------")
    jobsDone = 0
    customersWaiting = 0
    activeJobs = 0
    avgWait = 0
    for i in range(ITERATIONS):
        w, x, y, z = tellerGeneralFunctions.priorityTeller(10, 10, 160, 8)
        jobsDone += w
        customersWaiting += x
        activeJobs += y
        avgWait += z
    jobsDone /= ITERATIONS
    customersWaiting /= ITERATIONS
    activeJobs /= ITERATIONS
    avgWait /= ITERATIONS
    printResults(jobsDone, customersWaiting, activeJobs, avgWait)
    print("------------------------------------------")

    print("One Speedy Teller")
    print("------------------------------------------")
    jobsDone = 0
    customersWaiting = 0
    activeJobs = 0
    avgWait = 0
    for i in range(ITERATIONS):
        w, x, y, z = tellerGeneralFunctions.generalTeller(1, 100, 160, 8)
        jobsDone += w
        customersWaiting += x
        activeJobs += y
        avgWait += z
    jobsDone /= ITERATIONS
    customersWaiting /= ITERATIONS
    activeJobs /= ITERATIONS
    avgWait /= ITERATIONS
    printResults(jobsDone, customersWaiting, activeJobs, avgWait)
    print("------------------------------------------")

    print("Many Slow Tellers")
    print("------------------------------------------")
    jobsDone = 0
    customersWaiting = 0
    activeJobs = 0
    avgWait = 0
    for i in range(ITERATIONS):
        w, x, y, z = tellerGeneralFunctions.generalTeller(100, 1, 160, 8)
        jobsDone += w
        customersWaiting += x
        activeJobs += y
        avgWait += z
    jobsDone /= ITERATIONS
    customersWaiting /= ITERATIONS
    activeJobs /= ITERATIONS
    avgWait /= ITERATIONS
    printResults(jobsDone, customersWaiting, activeJobs, avgWait)
    print("------------------------------------------")
    print("Time:", time.time() - start)

