# 2022-10-20
#	17:15 - 17:36
#	19:38 - 20:00
# 	22:48 - 23:00

folds_list = []

def read_file(filename):
    with open(filename, 'r') as file:
    	flag = True
    	draft_list = []
    	global folds_list
    	for line in file.readlines():
    		if line == '\n':
    			flag = False
    		elif line != '\n' and flag == True:
    			draft_list.append(line)
    		elif line != '\n' and flag == False:
    			folds_list.append(line.strip().split(' ')[2].split('='))
    	return [line.strip().split(',') for line in draft_list]

data = read_file('notepad/206_2.txt')
# print(data)
for x in range(len(folds_list)):
	folds_list[x][1] = int(folds_list[x][1])
print(folds_list[0])

max_x = 0
max_y = 0
coordinates = []
for i in data:
	k = []
	if int(i[0]) > max_x:
		max_x = int(i[0])
	if int(i[1]) > max_y:
		max_y = int(i[1])
	for j in i:
		k.append(int(j))
	coordinates.append(k)
# print(coordinates)
# print(max_x)	# 1310
# print(max_y)	# 893

zeros = []
for y in range(max_y+1):
	line = []
	for x in range(max_x+1):
		line.append(0)
	zeros.append(line)
# print(zeros)

for point in coordinates:
	zeros[point[1]][point[0]] = 1
# print(zeros)

n = 0
fold = folds_list[n][1]
if folds_list[n][0] == 'x':
	for y in range(len(zeros)):
		for x in range(len(zeros[y])):
			if x < fold:
				zeros[y][x] += zeros[y][2*fold-x]
	for y in range(len(zeros)):
		del zeros[y][fold:]
# print(zeros)

ans = 0
for y in range(len(zeros)):
	for x in range(len(zeros[y])):
		if zeros[y][x] > 0:
			ans += 1
print(ans)



