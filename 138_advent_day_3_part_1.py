#20.08.2022

g_bin = ''	#gamma
e_bin = ''	#epsilon

with open('c:/Users/forwi/Witek/Szkoła/Liceum/Informatyka/projekty_pythona/notatnik/137_advent_day_3.txt') as f:
    data = f.readlines()
# print(data)
# print(len(data))

mother = []
for bin_number in data:
	daughter = []
	bin_number = bin_number.rstrip()
	for digit in bin_number:
		daughter.append(digit)
	mother.append(daughter)
# print(mother)

father = []
for i in range(0,len(mother[0])):
	father.append([])
# print(father)


for daughter in mother:
	for i in range(0,len(daughter)):
		father[i].append(daughter[i])
# print(father)
# print(len(father[0]))

zeros = 0
ones = 0
gamma = []
for son in father:
	zeros = son.count('0')
	ones = son.count('1')
	# print(f'zeros: {zeros}, ones: {ones}')
	if zeros > ones:
		gamma.append('0')
	elif zeros < ones:
		gamma.append('1')
	elif zeros == ones:
		gamma.append('2')
# print(gamma)

epsilon = []
for i in gamma:
	if i == '0':
		epsilon.append('1')
	elif i == '1':
		epsilon.append('0')
	elif i == '2':
		epsilon.append('2')
# print(epsilon)

g_bin = ''.join(gamma)
e_bin = ''.join(epsilon)
# print(g_bin)
# print(e_bin)

g_dec = int(g_bin,2)
e_dec = int(e_bin,2)
# print(g_dec)
# print(e_dec)

x = g_dec * e_dec
print(x)


