# 2022-10-03
# 13:25 - 16:06 (while lectures)

def read_file(filename):
    with open(filename, 'r') as file:
        return [[*line.strip()] for line in file.readlines()]

data = read_file('notepad/178_2.txt')
# print(data[-1])

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

n = [i[0] for i in m]
n.sort(reverse=True)

for i in n:
	del data[i]
# print(len(data))
# print(data[0])

def if_open(o, sign_open, sign_close, opener_list):
	if o == sign_open:
			opener_list.append(o)
	elif o == sign_close:
		if opener_list[-1] == sign_open:
			del opener_list[-1]
		elif opener_list[-1] != sign_open:
			print('ERROR')

p = []
for i in range(len(data)):
	opener_list = []
	for j in range(len(data[i])):
		o = data[i][j]
		if_open(o, '(', ')', opener_list)
		if_open(o, '[', ']', opener_list)
		if_open(o, '{', '}', opener_list)
		if_open(o, '<', '>', opener_list)
	p.append(opener_list)
# print(len(p))


x = 0

def count_x(opener, value, sign):
	global x
	if sign == opener:
		x *= 5
		x += value

x_list = []
for line_number in range(len(p)):
	line = p[line_number]
	line.reverse()
	x = 0
	for sign in line:
		count_x('(', 1, sign)
		count_x('[', 2, sign)
		count_x('{', 3, sign)
		count_x('<', 4, sign)
	x_list.append(x)
# x_list.sort()
# print(x_list)

import statistics
print(statistics.median(x_list))