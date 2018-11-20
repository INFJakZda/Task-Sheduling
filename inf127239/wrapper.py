import datetime
from subprocess import check_call

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

def saveSprawko(i, n, k, h, time, procesTime):
	with open("sprawko.txt", 'a+') as fw:
		fw.write(str(str(i) + ' ' + str(n) + ' ' + str(k) + ' ' + str(h) + ' ' + "0" + ' ' + str(time) + ' ' + "0" + ' ' + str(procesTime) + "\n"))

def calculatePenalty2(tasks, dueTime):
	penalty = 0
	time = 0
	for task in tasks:
		time = task[4] + task[0]
		penaltyTime = dueTime - time
		if (penaltyTime < 0):
			penalty -= penaltyTime * task[2]
		elif (penaltyTime > 0):
			penalty += penaltyTime * task[1]
	return penalty

def calculateTime(tasks, dueTime):
    with open("result.txt",'r') as fp:
        arr = []
        time = int(fp.readline())
        timeRun = int(fp.readline())
        startTimes = [int(i) for i in fp.readline().split()]
        # print(startTimes)
        # print(tasks)
        for i in range(len(tasks)):
            tasks[i].append(startTimes[i])
        myTime = calculatePenalty2(tasks, dueTime)
        if(myTime != time):
            print("ERR: Times are diff")
        return myTime


if __name__ == '__main__':
    nn = [10]
    kk = [1]
    hh = [0.6]
    ii = 1

    for n in nn:
        for k in kk:
            for h in hh:
                tasks = prepareData(n, k)
                dueTime = calculateSum(tasks, h)

                start = datetime.datetime.now()

                r = check_call(["/home/jakub/Desktop/semestr7/PTSZ/Task-Sheduling/inf127239/run.sh", str(n), str(k), str(h)])

                end = datetime.datetime.now()
                diff = end - start

                time = calculateTime(tasks, dueTime)

                print(ii, n)
                #Save data
                saveSprawko(ii, n, k, h, time, round(diff.total_seconds() * 1000000))
                ii += 1
