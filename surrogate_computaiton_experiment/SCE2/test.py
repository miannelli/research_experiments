from time import sleep, time
from threading import Thread
import random
from multiprocessing import Process, Manager

INTERPROBE_INTERVAL = 3         # Time between task pair probes (in seconds)
EXPERIMENT_SIZE = 5             # Number of Trials per Interprobe Interval
TASKAMOUNT = 1000              # Number of Tasks in Chunk
INTERCHUNK_GAP = .250           # Time between background Chunks Groups Launched
CHUNK_AMOUNT = 1000               # Number of chunks per task
MICROCHUNK_GAP = .001           # Time between chunk launches
TASK_LAUNCHERS = 5            # Number of Concurrent Task Launcher Processes

TASK_MASK = 1
LAUNCHER_MASK = 2

taskSizes = [10000]
probeTaskSizes = [100000]
intraprobeIntervals = [i/40. for i in range(0, 81)]
backgroundTraffics = [250]

def task(taskSize):
    a = 0
    for i in range(1, taskSize):
        a += 1


def backgroundTaskLauncher(taskSize, flag):
    while flag[0]:
        for i in range(0, CHUNK_AMOUNT):
            Thread(target=task, args=(taskSize,)).start()
            sleep(MICROCHUNK_GAP)
        sleep(INTERCHUNK_GAP*random.random()*2)


if __name__ == '__main__':
    manager = Manager()
    flag = manager.list([True])
    for i in range(0, TASK_LAUNCHERS):
        Process(target = backgroundTaskLauncher, args = (TASKAMOUNT, flag)).start()
    while True:
        sleep(1)
    flag[0] = False