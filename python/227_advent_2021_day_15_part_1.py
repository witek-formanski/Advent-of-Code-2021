# 	2022-11-29
#		22:48 - 0:25
# 	2022-11-30
#		14:00 - 14:04
#		17:10 - 17:42
#		23:56 - 0:27

# I assume, that I can only move down or to the right 
# (impossible is "coming back" up or to the left)

# I assume, that given matrix has the same number of rows and columns

# idea - sum risks at each diagonal 
# (points on one diagonal are reached after same number of steps)

def openAsMatrix(file):
	with open(file) as f:
		return [[int(i) for i in j] for j in f.read().splitlines()]

# listOfPoints:
# 0 - [[0, 0]]
# 1 - [[0, 1], [1, 0]]
# 2 - [[0, 2], [1, 1], [2, 0]]
# 3 - [[0, 3], [1, 2], [2, 1], [3, 0]]

def listOfPointsUp(i):		# 0 <= i <= 99
	if i == 0:
		return [[0, 0]]
	elif i >= 1:
		draft = []
		for point in listOfPointsUp(i-1):
			for j in range(2):
				newPoint = point.copy()
				newPoint[j] +=1
				if newPoint not in draft:
					draft.append(newPoint)
		return draft

def listOfPointsDown(i):	# 198 >= i >= 99
	if i == 198:
		return [[99, 99]]
	elif i <= 197:
		draft = []
		for point in listOfPointsDown(i+1):
			for j in range(2):
				newPoint = point.copy()
				newPoint[j] -=1
				if newPoint not in draft:
					draft.append(newPoint)
		return draft
# print(len(listOfPointsUp(0)))
# print(len(listOfPointsUp(99)))
# print(len(listOfPointsDown(99)))
# print(len(listOfPointsDown(198)))
# print(listOfPointsUp(99))

def getDiagonalRiskUp(point, matrix):
	priorPointZeroValue = matrix[point[0]-1][point[1]]
	priorPointOneValue = matrix[point[0]][point[1]-1]
	if point[0] > 0 and point[1] > 0:
		substract = min(priorPointOneValue, priorPointZeroValue)
	elif point[0] == 0 and point[1] == 0:
		return 0
	elif point[0] == 0:
		substract = priorPointOneValue
	elif point[1] == 0:
		substract = priorPointZeroValue
	return matrix[point[0]][point[1]] + substract

def getDiagonalRiskDown(point, matrix):
	# priorPointZeroValue = matrix[point[0]+1][point[1]]
	# priorPointOneValue = matrix[point[0]][point[1]+1]
	if point[0] < 99 and point[1] < 99:
		substract = min(matrix[point[0]][point[1]+1], matrix[point[0]+1][point[1]])
	elif point[0] == 99 and point[1] == 99:
		return matrix[point[0]][point[1]]
	elif point[0] == 99 and point[1] != 99:
		substract = matrix[point[0]][point[1]+1]
	elif point[1] == 99 and point[0] != 99:
		substract = matrix[point[0]+1][point[1]]
	return matrix[point[0]][point[1]] + substract

def fromUpperLeftCorner(matrix):
	for i in range(len(matrix)):
		for aPoint in listOfPointsUp(i):
			matrix[aPoint[0]][aPoint[1]] = getDiagonalRiskUp(aPoint, matrix)

def fromBottomRightCorner(matrix):
	for i in range(198,98,-1):
		for aPoint in listOfPointsDown(i):
			matrix[aPoint[0]][aPoint[1]] = getDiagonalRiskDown(aPoint, matrix)

def writeToFile(matrix, file):
	with open(file, 'w') as f:
		for row in matrix:
			for element in row:
				f.write(str(element))
				f.write('\t')
			f.write('\n')

def findRiskList(matrix):
	number = len(matrix) - 1
	pointsList = listOfPointsUp(number)
	riskList = []
	for pointAddress in pointsList:
		m = matrix[pointAddress[0]][pointAddress[1]]
		riskList.append(m)
	return riskList


def main():
	matrixA = openAsMatrix('notepad/227_advent_2021_day_15.txt')
	matrixB = [row.copy() for row in matrixA]
	matrixB[0][0] = 0
	fromUpperLeftCorner(matrixB)
	fromBottomRightCorner(matrixB)
	# writeToFile(matrixA, 'notepad/227_A.txt')
	# writeToFile(matrixB, 'notepad/227_B.txt')

	return min(findRiskList(matrixB))

print(main())


