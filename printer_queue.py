"""Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.

For each second (currentSecond):

Does a new print task get created? If so, add it to the queue with the currentSecond as the timestamp.

If the printer is not busy and if a task is waiting,

Remove the next task from the print queue and assign it to the printer.

Subtract the timestamp from the currentSecond to compute the waiting time for that task.

Append the waiting time for that task to a list for later processing.

Based on the number of pages in the print task, figure out how much time will be required.

The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task.

If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.

After the simulation is complete, compute the average waiting time from the list of waiting times generated.

"""
from pythonds.basic.queue import Queue
import random


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()  # Create a queue of print tasks
    waitingtimes = (
        []
    )  # Each task will be given a timestamp upon its arrival. The queue is empty to start.

    # For each second (currentSecond):
    for currentSecond in range(numSeconds):
        # Does a new print task get created?
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(
                task
            )  # add it to the queue with the currentSecond as the timestamp.

        # If the printer is not busy and if a task is waiting,
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()  # Remove the next task from the print queue
            # and assign it to the printer.
            # Subtract the timestamp from the currentSecond to compute the waiting time for that task.
            waitingtimes.append(nexttask.waitTime(currentSecond))
            # Append the waiting time for that task to a list for later processing.
            labprinter.startNext(nexttask)

        # Based on the number of pages in the print task, figure out how much time will be required.
        # The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task.
        # If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.

        labprinter.tick()

    # After the simulation is complete, compute the average waiting time from the list of waiting times generated.
    averageWait = sum(waitingtimes) / len(waitingtimes)
    print(
        "Average Wait %6.2f secs %3d tasks remaining."
        % (averageWait, printQueue.size())
    )

for i in range(10):
    simulation(3600,5)
