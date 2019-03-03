from Process import Process
from ProcessesAssignmentAlg import ProcessesAssignmentAlg

class FCFS_Scheduler(ProcessesAssignmentAlg):
    def __init__(self, processes):
        for p in processes:
            while(p.cycles > 0):
                p.run()
                p.wait()

        FCFS_Scheduler.printStats(processes)


def getExampleProcesses():
    return [Process(20), Process(5), Process(2)]


if __name__ == '__main__':
    FCFS_Scheduler(getExampleProcesses())
