class ProcessesAssignmentAlg:
    @staticmethod
    def printStats(processes):
        sumWaitTime = 0
        for process in processes:
            sumWaitTime += process.waitTime
            print("Proces {} wait time: {}".format(process.id, process.waitTime))
        print("Average wait time: {}".format(float(sumWaitTime)/len(processes)))
