# 2022-10-02
# 21:21 - 23:00

def read_file(filename):
    with open(filename, 'r') as file:
        return [[*line.strip()] for line in file.readlines()]





data = read_file('notepad/178_2.txt')
print(data)

m = []
for i in range(len(data)):
	opener_list = []
	for j in range(len(data[i])):
		o = data[i][j]
		if o == '(':
			opener_list.append(o)
		elif o == ')':
			if opener_list[-1] == '(':
				del opener_list[-1]
			elif opener_list[-1] != '(':
				k = [i, j, o, opener_list[-1]]
				m.append(k)
				break
		elif o == '[':
			opener_list.append(o)
		elif o == ']':
			if opener_list[-1] == '[':
				del opener_list[-1]
			elif opener_list[-1] != '[':
				k = [i, j, o, opener_list[-1]]
				m.append(k)	
				break
		elif o == '<':
			opener_list.append(o)
		elif o == '>':
			if opener_list[-1] == '<':
				del opener_list[-1]
			elif opener_list[-1] != '<':
				k = [i, j, o, opener_list[-1]]
				m.append(k)	
				break
		elif o == '{':
			opener_list.append(o)
		elif o == '}':
			if opener_list[-1] == '{':
				del opener_list[-1]
			elif opener_list[-1] != '{':
				k = [i, j, o, opener_list[-1]]
				m.append(k)	
				break
		else:
			print('ERROR')

# print(m)

points = {')':3, ']':57, '}':1197, '>':25137}

# n = []
# for i in m:
# 	n.append(i[1])

n = [i[2] for i in m]
# print(n)

x = sum([points[i] for i in n])
print(x)