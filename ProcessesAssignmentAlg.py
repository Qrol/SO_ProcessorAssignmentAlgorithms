class ProcessesAssignmentAlg:

    done = []
    time = 0
    processesInQueue = []

    @staticmethod
    def printStats(processes):
        sumWaitTime = 0
        for process in processes:
            sumWaitTime += process.waitTime
            print("Proces {} wait time: {}".format(process.id, process.waitTime))
        print("Average wait time: {}".format(float(sumWaitTime)/len(processes)))

    def queryNewProcesses(self, processes):
        for process in processes:
            if(process.arrivalTime <= self.time and process not in self.processesInQueue and process not in self.done):
                self.processesInQueue.append(process)
