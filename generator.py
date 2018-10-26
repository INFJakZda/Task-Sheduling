import numpy as np

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

if __name__ == '__main__':
	n = 10
	k = 2
	h = 0.4

	dataSet = prepareData(n, k)
	dueTime = calculateSum(dataSet, h)