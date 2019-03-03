import time
import sys

class Process:
    __timePerOneCycle = 0.01#in seconds
    idCounter = 0
    waitTime = 0

    def __init__(self, cycles, arrivalTime):
        self.arrivalTime = arrivalTime
        self.id = Process.idCounter
        Process.idCounter += 1
        self.cycles = cycles

    def run(self):
        sys.stdout.write("Running process {}".format(self.id))
        dotsNum = 3
        for i in range(dotsNum):
            time.sleep(float(self.__timePerOneCycle)/dotsNum)
            sys.stdout.write('.')
        print
        self.cycles -= 1

    def wait(self):
        self.waitTime += 1

    def isActive(self):
        return self.cycles > 0
