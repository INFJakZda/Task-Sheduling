def prepareData(noFile, noInstance):
	with open("data/sch" + str(noFile) + ".txt",'r') as fp:
		noInstances = int(fp.readline())
		arr = []
		for k in range(1, noInstances + 1):
			noLines = int(fp.readline())
			if (k == noInstance):
				for _ in range(noLines):
					arr.append(list(map(int, fp.readline().split())))
				break
			else:
				for _ in range(noLines):
					fp.readline()
		return arr

def calculateSum(dataSet, h):
	sum = 0
	for row in dataSet:
		sum += row[0]
	return round(sum * h)

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
	

def schedule(tasks, dueTime):
	ScheduledTasks = []
	BestScheduled = []
	bestTime = 0
	for idx, task in enumerate(tasks):
		if not ScheduledTasks:
			ScheduledTasks.append(task)
		else:
			bestTime = 999999999
			for i in range( len(ScheduledTasks) + 1 ):
				ScheduledTasks.insert(i, task)
				currentPenalty = calculatePenalty(ScheduledTasks, dueTime)
				if (bestTime > currentPenalty):
					bestTime = currentPenalty
					BestScheduled = ScheduledTasks.copy()
				ScheduledTasks.pop(i)
			ScheduledTasks = BestScheduled.copy()
	print(calculatePenalty(ScheduledTasks, dueTime))
	#print(ScheduledTasks)

if __name__ == '__main__':
	n = 20
	k = 7
	h = 0.2

	dataSet = prepareData(n, k)
	dueTime = calculateSum(dataSet, h)

	#Prepare data set
	tasks.sort(key = lambda task: task[1] - task[2])

	#Schedule task with algorithm
	schedule(dataSet, dueTime)