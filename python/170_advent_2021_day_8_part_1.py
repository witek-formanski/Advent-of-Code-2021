# 2022-09-24
# 	22:07 - 22:48

with open('notepad/170_2.txt') as f:
	data1 = f.readlines()
# print(data1)
# ['10 patterns | 4-digit output\n', ...]

data2 = []
for i in data1:
	j = i.split('|')
	j[0] = j[0].strip()
	j[1] = j[1].strip()
	data2.append(j)
# print(data2)
# [['10 patterns', '4-digit output'], ...]

for i in data2:
	i[0] = i[0].split()
	i[1] = i[1].split()
# print(data2)

# [[[10 x 'pattern'], [4 x 'digit']], ...]

# [
# 	[
# 		[10 x 'pattern'], [4 x 'digit']
# 	],
# 	...
# ]

outputs = []
for i in range(len(data2)):
	j = data2[i][1]
	outputs.append(j)
# print(outputs)
# [
# 	[4 x 'digit'],
# 	...
# ]

k = 0
for i in outputs:
	for j in i:
		if len(j) == 2:		#1
			k+=1
		elif len(j) == 3:	#7
			k+=1
		elif len(j) == 4:	#4
			k+=1
		elif len(j) == 7:	#8
			k+=1
print(k)
# first try

