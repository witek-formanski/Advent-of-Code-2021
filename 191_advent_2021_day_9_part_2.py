# 2022-10-07
# 1:23 - 2:04

openfile = open('notepad/176_advent_2021_day_9.txt')

data = []
for line in openfile.readlines():
	int_list = []
	for string_digit in [*line.strip()]:
		int_list.append(int(string_digit))
	data.append(int_list)
print(data)

def GetValue(data, point):
	if point[0] < 0 or point[0] >= len(data):
		return 10
	if point[1] < 0 or point[1] >= len(data[0]):
		return 10
	return data[point[0]][point[1]]

# def TurnValueToNine(data, point):
# 	if point[0] < 0 or point[0] > len(data):
# 		continue
# 	if point[1] < 0 or point[1] > len(data[0]):
# 		continue
# 	data[point[0]][point[1]] = 11

basins = []
for x in range(len(data)):
	for y in range(len(data[x])):
		count = 0
		to_check = [[x,y]]
		checked = []
		while len(to_check) > 0:
			if to_check[0] not in checked and GetValue(data, to_check[0]) < 9:
				count += 1
				checked.append(to_check[0])
				xx = to_check[0][0]
				yy = to_check[0][1]
				adjacent_points = [[xx+1, yy], [xx-1,yy], [xx, yy+1], [xx, yy-1]]
				to_check.extend(adjacent_points)
			if to_check[0][0] > 0 and to_check[0][0] < len(data) and to_check[0][1] > 0 and to_check[0][1] < len(data[0]):
				data[to_check[0][0]][to_check[0][1]] = 12
			del to_check[0]
		if count > 0:
			# print(data)
			basins.append(count)

print(sorted(basins, reverse=True)[0]*sorted(basins, reverse=True)[1]*sorted(basins, reverse=True)[2])


# dlaczego not in tak bardzo przyspiesza program?
