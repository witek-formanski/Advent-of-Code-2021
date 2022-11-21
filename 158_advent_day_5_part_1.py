#24.08.2022

import numpy as np

with open('notepad/158_2.txt') as f:
	data = f.readlines()
# print(data)
# print(len(data))

data_strip = []
for i in data:
	data_strip.append(i.rstrip())
# print(data_strip)

data_prefinal = []
for i in data_strip:
	j = list(i.split(' -> '))
	k = list(j[0].split(','))
	l = list(j[1].split(','))
	k[0] = int(k[0])
	k[1] = int(k[1])
	l[0] = int(l[0])
	l[1] = int(l[1])
	m = []
	m.append(k)
	m.append(l)
	data_prefinal.append(m)
# print(data_prefinal)
# print(len(data_prefinal))

data_final = []
vertical = []
horizontal = []
for i in data_prefinal:
	if i[0][0]==i[1][0]:
		data_final.append(i)
		vertical.append(i)
	elif i[0][1]==i[1][1]:
		data_final.append(i)
		horizontal.append(i)
print(data_final)
# print(len(data_final))
# print(len(vertical))
# print(len(horizontal))

board = np.zeros((1000,1000), int)
# print(board)

# data_truly_final = []
for i in data_final:
	if i[0][0] > i[1][0]:
		#switch
		i[0][0], i[1][0] = i[1][0], i[0][0]
	if i[0][1] > i[1][1]:
		#switch
		i[0][1], i[1][1] = i[1][1], i[0][1]


# print(vertical)
for i in data_final:
	x1 = i[0][0]
	y1 = i[0][1]
	x2 = i[1][0]
	y2 = i[1][1]
	board[y1:y2+1, x1:x2+1] += 1
np.set_printoptions(threshold=np.inf)
# print(board)

k = 0
for i in range(0,1000):
	for j in range(0,1000):
		if board[i][j] >= 2:
			k += 1
print(k)
