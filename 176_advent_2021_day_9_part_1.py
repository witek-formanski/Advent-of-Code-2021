# 2022-09-28
# 	10:41 - 11:56

def read_file(filename):
    with open(filename, 'r') as file:
        return [list(map(int, list(line.strip()))) for line in file.read().strip().split("\n")]
data2 = read_file('notepad/176_2.txt')

# stworzyć macierz zeros - 100x100 wypełnioną zerami

# jeśli dany punkt w macierzy data2 jest mniejszy od obu 
# sąsiadujących w poziomie, dodać 1 w macierzy zeros w tym punkcie

# analogicznie z punktami sąsiadującymi w pionie

# jeżeli w macierzy zeros jakiś punkt ma wartość 2,
# to jest punktem najniższym w otoczeniu

zeros = []
for i in range(100):
	j = []
	for k in range(100):
		j.append(0)
	zeros.append(j)
# print(zeros)
# print(len(zeros))
# print(len(zeros[0]))

# PUNKTY ŚRODKOWE:

for i in range(100):
	for j in range(1,99):
		if data2[i][j] < data2[i][j+1] and data2[i][j] < data2[i][j-1]:
			zeros[i][j] += 1
# print(zeros)

for i in range(1,99):
	for j in range(100):
		if data2[i][j] < data2[i+1][j] and data2[i][j] < data2[i-1][j]:
			zeros[i][j] += 1
# print(zeros)

# PUNKTY BRZEGOWE (BEZ NAROŻNIKÓW):

for j in range(1,99):
	if data2[0][j] < data2[1][j]:
			zeros[0][j] += 1
	if data2[-1][j] < data2[-2][j]:
			zeros[-1][j] += 1
# print(zeros[0], zeros[-1])

for i in range(1,99):
	if data2[i][0] < data2[i][1]:
			zeros[i][0] += 1
	if data2[i][-1] < data2[i][-2]:
			zeros[i][-1] += 1

# NAROŻNIKI:

if data2[0][0] < data2[0][1]:
		zeros[0][0] += 1
if data2[0][0] < data2[1][0]:
		zeros[0][0] += 1

if data2[0][-1] < data2[0][-2]:
		zeros[0][-1] += 1
if data2[0][-1] < data2[1][-1]:
		zeros[0][-1] += 1

if data2[-1][0] < data2[-1][1]:
		zeros[-1][0] += 1
if data2[-1][0] < data2[-2][0]:
		zeros[-1][0] += 1

if data2[-1][-1] < data2[-2][-1]:
		zeros[-1][-1] += 1
if data2[-1][-1] < data2[-1][-2]:
		zeros[-1][-1] += 1

# print(zeros)

# ZLICZANIE 2 W MACIERZY ZEROS I WYNIK:

x = 0
for i in range(100):
	for j in range(100):
		if zeros[i][j] == 2:
			x += data2[i][j]+1
print(x)