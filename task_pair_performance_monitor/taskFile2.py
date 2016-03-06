from time import sleep, time
from threading import Thread
import random
from multiprocessing import Process, Manager


INTERPROBE_INTERVAL = 3        #Time between task pair probes (in seconds)
EXPERIMENT_SIZE = 1
TASKAMOUNT = 10000
INTERCHUNK_GAP = .250 #Time between background task launched
CHUNK_AMOUNT = 100 #Number of chunks per task
MICROCHUNK_GAP = .001


taskSizes = [10000]
probeTaskSizes = [100000]
intraprobeIntervals = [i for i in range(0,401,25)]
backgroundTraffics = [250]

def task(taskSize):
    a = 0;
    for i in range(1,taskSize):
        a+=1


def probeTask(probeTaskSize,times,type):
    times['Task ' + str(type) + ' Start Time'] = time()
    task(probeTaskSize)
    times['Task ' + str(type) + ' Finish Time'] = time()


def backgroundTaskLauncher(taskSize):
    global flag
    while flag==True:
        for i in range(0,CHUNK_AMOUNT):
            Thread(target=task, args=(taskSize,)).start()
            sleep(MICROCHUNK_GAP)
	    
        sleep(INTERCHUNK_GAP*random.random()*2)

def taskPairLauncher(intraprobeGap, probeTaskSize, times):
    pTask1 = Process(target=probeTask, args=(probeTaskSize,times,1,))
    times['Task 1 Scheduled At'] = time()
    pTask1.start()
    sleep(intraprobeGap)
    pTask2 = Process(target=probeTask, args=(probeTaskSize,times,2,))
    times['Task 2 Scheduled At'] = time()
    pTask2.start()
    pTask1.join()
    pTask2.join()
    return times



global flag
flag = True

if __name__ == '__main__':
    global flag
    f = open('myfile','w')
    manager = Manager()
    #print("Task 1 Launch\tTask 2 Launch\tTask 1 Start\tTask 1 Finish\tTask 2 Start\tTask 2 Finish\tDelta\tDelta Prime")
    for backgroundTraffic in backgroundTraffics:
        for taskSize in taskSizes:
            flag = True
            for i in range(1,20):
                Process(target=backgroundTaskLauncher, args=(taskSize,)).start()
            for probeTaskSize in probeTaskSizes:
                for intraprobeInterval in intraprobeIntervals:
                    qstats = []
                    qpstats = []
                    for trial in range(0,EXPERIMENT_SIZE):
                        sleep(INTERPROBE_INTERVAL)
                        timeArray = manager.dict()
                        taskPair = Process(target=taskPairLauncher, args=(intraprobeInterval/1000, probeTaskSize, timeArray))
                        taskPair.start()
                        taskPair.join()
                        qpstats.append(timeArray['Task 2 Start Time']-timeArray['Task 1 Start Time'])
                        qstats.append(timeArray['Task 2 Scheduled At']-timeArray['Task 1 Scheduled At'])
                        #results = [timeArray['Task 2 Scheduled At']-timeArray['Task 1 Scheduled At'],timeArray['Task 2 Finish Time']-timeArray['Task 1 Finish Time']]
                        #results = [timeArray['Task 1 Scheduled At'],timeArray['Task 2 Scheduled At'],timeArray['Task 1 Start Time'],timeArray['Task 1 Finish Time'],timeArray['Task 2 Start Time'],timeArray['Task 2 Finish Time']]
                        #results +=results2
                    results = [sum(qstats)/EXPERIMENT_SIZE,sum(qpstats)/EXPERIMENT_SIZE]
                    print(str(intraprobeInterval)+ '\t' + str(results[0]) + '\t' + str(results[1]))


            flag = False
