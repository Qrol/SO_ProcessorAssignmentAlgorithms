from Process import Process
from ProcessesAssignmentAlg import ProcessesAssignmentAlg

class ROT_Scheduler(ProcessesAssignmentAlg):
    done = []

    def __init__(self, processes, K = 3):
        i = 0
        while len(processes) > 0:
            self.queryNewProcesses(processes)

            process = processes[i]

            j = 0
            while j < K and process.isActive():
                process.run()
                self.time += 1
                for p in processes:
                    if(p == process): continue
                    p.wait()
                j += 1

            if not process.isActive():
                self.done.append(process)
                processes.remove(process)
                if(len(processes)>0):
                    i = i % len(processes)
                continue

            i = (i + 1) % len(processes)

        ROT_Scheduler.printStats(self.done)


def getExampleProcesses():
    return [Process(20, 0), Process(5, 0), Process(2, 0), Process(4, 1)]

if __name__ == '__main__':
    ROT_Scheduler(getExampleProcesses())
