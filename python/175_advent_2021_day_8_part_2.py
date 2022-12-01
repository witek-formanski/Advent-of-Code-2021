# 2022-09-24
# 	22:51 - 23:35

# 2022-09-26
# 	22:06 - about 30 min break - 0:12

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
# print(data2[:10])
# print("\n")

# [[[10 x 'pattern'], [4 x 'digit']], ...]

# [
# 	[
# 		[10 x 'pattern'], [4 x 'digit']
# 	],
# 	...
# ]



# len
	# 0 - 6
	# 1 - 2
	# 2 - 5
	# 3 - 5
	# 4 - 4
	# 5 - 5
	# 6 - 6
	# 7 - 3
	# 8 - 7
	# 9 - 6

	# 0,6,9 - len = 6
	# 2,3,5 - len = 5

# segments (letters)
	# 1 - [c,f]
	# 7 - a
	# 4 - [b,d]

# step by step decoding:
	
	# detecting 1,4,7,8:
		# len
	
	# detecting 6:
		# lack of c (known from 1)
	# detecting 0:
		# lack of d (known from 4)
	# detecting 9:
		# 0 and 6 detected
	
	# detecting 3:
		# occurrence of c and f (known from 1)
	# detecing 5:
		# occurence of b and d (known from 4)
	# detecting 2:
		# 3 and 5 detected


# [
# 	i [
# 		i[0] [10 x 'pattern'], [4 x 'digit']
# 	  ],
# 	...
# ]

recipe = []
for i in data2:
	k = {}
	j = 0
	# print(len(i[0]))
	while len(i[0]) == 10:
		l = i[0][j]
		if len(l) == 2:
			s = [*l]
			s.sort()
			q = ''.join(s)
			k[q] = 1
			cf = [*l]
			# print(cf)
			j = 0
			i[0].remove(l)
		else:
			j += 1
	# print(len(i[0]))
	while len(i[0]) == 9:
		l = i[0][j]
		if len(l) == 4:
			s = [*l]
			s.sort()
			q = ''.join(s)
			k[q] = 4
			bd = [*l]
			# print(bd)
			bd.remove(cf[0])
			bd.remove(cf[1])
			# print(bd)
			j = 0
			i[0].remove(l)
		else:
			j += 1
	# print(len(i[0]))
	while len(i[0]) == 8:
		l = i[0][j]
		if len(l) == 3:
			s = [*l]
			s.sort()
			q = ''.join(s)
			k[q] = 7
			j = 0
			i[0].remove(l)
		else:
			j += 1
	# print(len(i[0]))
	while len(i[0]) == 7:
		l = i[0][j]
		if len(l) == 7:
			s = [*l]
			s.sort()
			q = ''.join(s)
			k[q] = 8
			j = 0
			i[0].remove(l)
		else:
			j += 1
	# print(len(i[0]))
	while len(i[0]) == 6:
		l = i[0][j]
		m = [*l]
		if len(l) == 6:
			check = all(x in m for x in cf)
			if check == False:
				s = [*l]
				s.sort()
				q = ''.join(s)
				k[q] = 6
				j = 0
				# print(m)
				i[0].remove(l)
			else:
				j += 1
		else:
			j += 1
	# print(len(i[0]))
	while len(i[0]) == 5:
		l = i[0][j]
		m = [*l]
		if len(l) == 6:
			check = all(x in m for x in bd)
			if check == False:
				s = [*l]
				s.sort()
				q = ''.join(s)
				k[q] = 0
				j = 0
				# print(m)
				i[0].remove(l)
			else:
				j += 1
		else:
			j += 1
	# print(len(i[0]))
	while len(i[0]) == 4:
		l = i[0][j]
		if len(l) == 6:
			s = [*l]
			s.sort()
			q = ''.join(s)
			k[q] = 9
			j = 0
			i[0].remove(l)
		else:
			j += 1
	# print(len(i[0]))
	while len(i[0]) == 3:
		l = i[0][j]
		m = [*l]
		if len(l) == 5:
			check = all(x in m for x in cf)
			if check == True:
				s = [*l]
				s.sort()
				q = ''.join(s)
				k[q] = 3
				j = 0
				# print(m)
				i[0].remove(l)
			else:
				j += 1
		else:
			j += 1
	# print(len(i[0]))
	while len(i[0]) == 2:
		l = i[0][j]
		m = [*l]
		if len(l) == 5:
			check = all(x in m for x in bd)
			if check == True:
				s = [*l]
				s.sort()
				q = ''.join(s)
				k[q] = 5
				j = 0
				# print(m)
				i[0].remove(l)
			else:
				j += 1
		else:
			j += 1
	# print(len(i[0]))
	# while len(i[0]) == 1:
	# 	l = i[0][j]
	# 	if len(l) == 5:
	# 		k[l] = 2
	# 		j = 0
	# 		i[0].remove(l)
	# 	else:
	# 		j += 1
	# print(len(i[0]))
	l = i[0][0]
	s = [*l]
	s.sort()
	q = ''.join(s)
	k[q] = 2
	i[0].remove(l)
	recipe.append(k)
# print(recipe[:10])
# print(data2[:10])

outputs = []
for i in range(len(data2)):
	k = []
	for j in range(4):
		n = data2[i][1][j]
		n = [*n]
		# print(n)
		n.sort()
		# print(n)
		n = ''.join(n)
		# print(n)
		# print(recipe[i])
		# print(recipe[i][n])
		# print('\n')
		k.append(recipe[i][n])
	# print(k)
	k = ''.join(str(e) for e in k)
	# print(k)
	outputs.append(k)
# print(outputs)

x = sum(int(e) for e in outputs)
print(x)