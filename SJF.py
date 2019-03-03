from Process import Process
from ProcessesAssignmentAlg import ProcessesAssignmentAlg

class SJF_Scheduler(ProcessesAssignmentAlg):
    def __init__(self, processes):
        done = []
        while len(processes) > 0:
            processToRun = self.popShortest(processes)
            while processToRun.isActive():
                processToRun.run()
                self.increaseWaitTimeForOther(processes)
            done.append(processToRun)

        SJF_Scheduler.printStats(done)

    def popShortest(self, processes):
        shortestP = processes[0]
        for p in processes:
            if p.cycles < shortestP.cycles:
                shortestP = p
        processes.remove(shortestP)
        return shortestP

    def increaseWaitTimeForOther(self, processes):
        for process in processes:
            process.wait()

def getExampleProcesses():
    return [Process(20), Process(5), Process(2)]


if __name__ == '__main__':
    SJF_Scheduler(getExampleProcesses())
