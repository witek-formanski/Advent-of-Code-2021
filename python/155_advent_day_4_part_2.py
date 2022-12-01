#21.08.2022

import numpy as np

with open('notepad/154_2.txt') as f:
    data = f.readlines()
# print(data)

random_series_variable = data.pop(0)
random_series_variable = random_series_variable.rstrip()
random_series_list = list(random_series_variable.split(','))
numbers = []
for i in random_series_list:
	j = int(i)
	numbers.append(j)
print(numbers)

# print(data)
data_strip = []
for i in data:
	data_strip.append(i.strip())
# print(data_strip)
# print(len(data_strip)/6)

bingo = []
for i in range(0,len(data_strip)//6):
	bingo.append([])
	for j in range(1,6):
		k = data_strip[i*6+j]
		l = list(k.split(' '))
		while '' in l:
			l.remove('')
		o = []
		for m in l:
			n = int(m)
			o.append(n)
		bingo[i].append(o)
# print(bingo)
# print(len(bingo))

# bingo - 100 macierzy, każda po 5 wierszy i 5 kolumn
# bingo[nr_macierzy = a][nr_wiersza = b][nr_kolumny = c]

biar = np.array(bingo)
# biar_copy = biar
# print(biar)
# print(len(biar))
# print(biar[0][0][0])

# biar[0][0][0] = -1
# print(biar)
# active=True

MS =[]
for i in range(0,100):
	MS.append(i)

for number in numbers:
	if len(MS)==1:
		break
	# if active==False:
	# 	break
	# print(f'number={number}')
	for i in range(0,len(biar)):				#wybór macierzy
		if len(MS)==1:
			break
		# if active==False:
		# 	break
		# print(f'i={i}')
		for j in range(0,len(biar[0])):			#wybór wiersza
			if len(MS)==1:
				break
			# if active==False:
			# 	break
			# print(f'j={j}')
			for k in range(0,len(biar[0][0])):	#wybór kolumny
				# print(f'k={k}')
				if number == biar[i][j][k]:
					biar[i][j][k] = -1
					if biar[i][j][0]+biar[i][j][1]+biar[i][j][2]+biar[i][j][3]+biar[i][j][4] == -5:
						print(f'BINGO! biar[macierz={i}][wiersz={j}], number={number}')
						if i in MS:
							MS.remove(i)
						if len(MS)==1:
							# N = number
							break
						# active=False
						# break
					elif biar[i][0][k]+biar[i][1][k]+biar[i][2][k]+biar[i][3][k]+biar[i][4][k] == -5:
						print(f'BINGO! biar[macierz={i}][kolumna={k}], number={number}')
						if i in MS:
							MS.remove(i)					
						if len(MS)==1:
							# N = number
							break
						# active=False
						# break

# print(biar)
# print(len(numbers))
# print(f'M = {M}, N = {N}')

# print(N)

M = MS[0]
print(M)
print(biar[M])

active=True
for number in numbers:
	if active==False:
		break
	for i in range(0,5):
		if active==False:
			break
		for j in range(0,5):
			if active==False:
				break
			if number == biar[M][i][j]:
				biar[M][i][j] = -1
				if biar[i][j][0]+biar[i][j][1]+biar[i][j][2]+biar[i][j][3]+biar[i][j][4] == -5:
						print(f'BINGO! biar[macierz={i}][wiersz={j}], number={number}')
						N = number
						active=False
						break
				elif biar[i][0][k]+biar[i][1][k]+biar[i][2][k]+biar[i][3][k]+biar[i][4][k] == -5:
					print(f'BINGO! biar[macierz={i}][kolumna={k}], number={number}')
					N = number
					active=False
					break

S=0
for i in range(0,5):
	for j in range(0,5):
		if biar[M][i][j] != -1:
			S += biar[M][i][j]
print(f'N={N},S={S}')
print(S*N)