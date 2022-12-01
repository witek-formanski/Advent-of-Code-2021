#25.08.2022

with open('notepad/163_2.txt') as f:
	data = f.readlines()

data_list = list(data[0].split(','))
initial = [int(x) for x in data_list]

for i in range(80):
	# print(i)
	initial.extend([9]*initial.count(0))
	initial = [7 if x==0 else x for x in initial]
	initial = [x-1 for x in initial]
# print(initial)
print(len(initial))