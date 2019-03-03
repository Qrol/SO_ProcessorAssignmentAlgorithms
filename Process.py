import time
import sys

class Process:
    __timePerOneCycle = 0.6#in seconds
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
        time.sleep(float(self.__timePerOneCycle)/(dotsNum + 1))
        for i in range(dotsNum):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(float(self.__timePerOneCycle)/(dotsNum + 1))
        print
        self.cycles -= 1

    def wait(self):
        self.waitTime += 1

    def isActive(self):
        return self.cycles > 0
