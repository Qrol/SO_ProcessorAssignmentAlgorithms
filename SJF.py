from Process import Process
from ProcessesAssignmentAlg import ProcessesAssignmentAlg

class SJF_Scheduler(ProcessesAssignmentAlg):

    def __init__(self, processes):
        self.queryNewProcesses(processes)
        while len(self.processesInQueue) > 0:
            processToRun = self.popShortest(self.processesInQueue)
            while processToRun.isActive():
                processToRun.run()
                self.increaseWaitTimeForOther(self.processesInQueue)
                self.queryNewProcesses([process for process in processes if process != processToRun])
            self.done.append(processToRun)


        SJF_Scheduler.printStats(self.done)

    def popShortest(self, processes):
        shortestP = processes[0]
        for p in processes:
            if p.cycles < shortestP.cycles:
                shortestP = p
        processes.remove(shortestP)
        return shortestP

    def increaseWaitTimeForOther(self, processes):
        self.time += 1
        for process in processes:
            process.wait()

def getExampleProcesses():
    return [Process(20, 0), Process(5, 0), Process(2, 0), Process(3, 3)]

if __name__ == '__main__':
    SJF_Scheduler(getExampleProcesses())
