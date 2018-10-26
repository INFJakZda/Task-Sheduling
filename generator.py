

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
			k += 1
		return arr

if __name__ == '__main__':
	n = 20
	k = 5
	h = 0.4

	dataSet = prepareData(n, k)
