import datetime
import sys
from math import floor

def prepareData(noFile, noInstance):
	with open("sch" + str(noFile) + ".txt",'r') as fp:
		noInstances = int(fp.readline())
		arr = []
		for k in range(1, noInstances + 1):
			noLines = int(fp.readline())
			if (k == noInstance):
				for idx in range(noLines):
					ele = list(map(int, fp.readline().split()))
					ele.append(idx + 1)
					arr.append(ele)
				break
			else:
				for _ in range(noLines):
					fp.readline()
		return arr

def calculateSum(tasks, h):
	sum = 0
	for row in tasks:
		sum += row[0]
	return floor(sum * h)

def calculatePenalty(tasks, dueTime):
	penalty = 0
	time = 0
	for task in tasks:
		time += task[0] 
		penaltyTime = dueTime - time
		if (penaltyTime < 0):
			penalty -= penaltyTime * task[2]
		elif (penaltyTime > 0):
			penalty += penaltyTime * task[1]
	return penalty

def saveData(tasks, processTime, elapsedTime):
	times = [[] for _ in range( len(tasks) )]
	time = 0
	for task in tasks:
		times[task[3] - 1] = time
		time += task[0]
	with open("wyniki.txt", 'w') as fw:
		fw.write(str(processTime) + '\n')
		fw.write(str(elapsedTime) + '\n')
		fw.write(' '.join(map(str, times)))

if __name__ == '__main__':
    start = datetime.datetime.now()

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    h = float(sys.argv[3])
    tasks = prepareData(n, k)
    dueTime = calculateSum(tasks, h)

    #Prepare data set
    tasks.sort(key = lambda task: task[1] - task[2])
    time = calculatePenalty(tasks, dueTime)

    end = datetime.datetime.now()
    diff = end - start

    #Save data
    saveData(tasks, time, round(diff.total_seconds() * 1000000))
