# 2022-10-09
# 	15:16 - 15:23
# 2022-10-10
# 	8:46 - ?
# 2022-10-19
#	22:59 - 23:17

def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip().split('-') for line in file.readlines()]

data = read_file('notepad/194_2.txt')
# print(data)

all_caves = [i.copy() for i in data]

# stworzyć set z wszystkimi jaskiniami

# stworzyć słownik:
#	klucz - jaskinia
#	wartości - wszystkie jaskinie połączone z daną jaskinią

# stworzyć listę list (paths, path)
#	na każdą z list (path):
#	dodać 'start'
#	wybrać pierwszą wartość (jaskinię) z caves_dict['start']
#	wybrać pierwszą

caves_set = set([])
for caves_pair in all_caves:
	for cave in caves_pair:
		caves_set.add(cave)
# print(caves_set)	

caves_dict = {}
for cave_in_set in caves_set:
	connected_caves = []
	for caves_pair in all_caves:
		if caves_pair[0] == cave_in_set:
			connected_caves.append(caves_pair[1])
		if caves_pair[1] == cave_in_set:
			connected_caves.append(caves_pair[0])
	caves_dict[cave_in_set] = connected_caves
# print(caves_dict)
# print('\n')

# delete 'start' values

for key in caves_dict:
	for value in caves_dict[key]:
		if value == 'start':
			caves_dict[key].remove('start')
print(caves_dict)

paths = []
paths_ended = []
paths.append(['start'])

while len(paths) != 0:
	key = paths[0][-1]
	for connected_cave in caves_dict[key]:
		new_path = paths[0].copy()
		new_path.append(connected_cave)
		if connected_cave == 'end':
			paths_ended.append(new_path)
		elif connected_cave == connected_cave.lower():
			if connected_cave not in paths[0]:
				paths.append(new_path)
		elif connected_cave == connected_cave.upper():
			paths.append(new_path)
		print(new_path)
		# print(paths_ended)
	del paths[0]

print(len(paths_ended))




			