import datetime

def prepareData(noFile, noInstance):
	with open("data/sch" + str(noFile) + ".txt",'r') as fp:
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
	return ScheduledTasks, bestTime

def saveData(tasks, processTime):
	times = [[] for _ in range( len(tasks) )]
	time = 0
	for task in tasks:
		time += task[0]
		times[task[3] - 1] = time
	with open("result.txt", 'w') as fw:
		fw.write(str(processTime) + '\n')
		fw.write(' '.join(map(str, times)))

def saveSprawko(i, n, k, h, time, procesTime):
	with open("sprawko.txt", 'a+') as fw:
		fw.write(str(str(i) + ' ' + str(n) + ' ' + str(k) + ' ' + str(h) + ' ' + "0" + ' ' + str(time) + ' ' + "0" + ' ' + str(procesTime) + "\n"))


if __name__ == '__main__':
    nn = [10, 20, 50, 100, 200, 500, 1000]
    kk = [2, 7]
    hh = [0.4, 0.6]
    ii = 1

    for n in nn:
        for k in kk:
            for h in hh:

                start = datetime.datetime.now()

                tasks = prepareData(n, k)
                dueTime = calculateSum(tasks, h)

                #Prepare data set
                tasks.sort(key = lambda task: task[1] - task[2])

                #Schedule task with algorithm
                scheduledTasks, time = schedule(tasks, dueTime)

                end = datetime.datetime.now()
                diff = end - start

                print(ii, n)
                #Save data
                saveSprawko(ii, n, k, h, time, round(diff.total_seconds() * 1000000))
                ii += 1
