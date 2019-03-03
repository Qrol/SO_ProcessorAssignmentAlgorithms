from Process import Process
from ProcessesAssignmentAlg import ProcessesAssignmentAlg

class FCFS_Scheduler(ProcessesAssignmentAlg):
    done = []
    time = 0
    processesInQueue = []
    def __init__(self, processes):
        self.processes = processes
        self.queryNewProcesses(processes)
        while len(self.processesInQueue) > 0:
            self.runQueuedProcesses()
        FCFS_Scheduler.printStats(self.done)

    def runQueuedProcesses(self):
        while(0 < len(self.processesInQueue)):
            p = self.processesInQueue[0]
            while(p.isActive()):
                p.run()
                self.increaseWaitTimeForOther(p, self.processesInQueue)
                self.queryNewProcesses(self.processes)

            self.done.append(p)
            self.processesInQueue.remove(p)

    def increaseWaitTimeForOther(self, processToOmmit, processes):
        self.time += 1
        for p in processes:
            if p != processToOmmit:
                p.wait()

    def queryNewProcesses(self, processes):
        for process in processes:
            if(process.arrivalTime <= self.time and process not in self.processesInQueue and process not in self.done):
                self.processesInQueue.append(process)


def getExampleProcesses():
    return [Process(20, 0), Process(5, 0), Process(2, 0), Process(6, 2)]


if __name__ == '__main__':
    FCFS_Scheduler(getExampleProcesses())
