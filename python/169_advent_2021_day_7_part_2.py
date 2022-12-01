#31.08.2022

with open('notepad/166_2.txt') as f:
	data = f.readlines()
data_split = data[0].split(',')
data_final = []
for i in data_split:
	j = int(i)
	data_final.append(j)
max_ = max(data_final)
min_ = min(data_final)

# 1 -> 1
# 2 -> 1+2 = 3
# 3 -> 1+2+3 = 6
# 4 -> 1+2+3+4 = 10

# print(sum(range(0,5)))

# data_final = [16,1,2,0,4,2,7,1,2,14]
s_list = []
for i in range(min_,max_+1):
	s_i = 0
	for j in data_final:
		if j>=i:
			s_i += sum(range(0,abs(j-i+1)))
			# print(sum(range(0,abs(j-i+1))))
		elif j<i:
			s_i += sum(range(0,abs(j-i-1)))
			# print(sum(range(0,abs(j-i-1))))
	# print(s_i)
	s_list.append(s_i)
# print(s_list)
print(min(s_list))

from matplotlib import pyplot as plt
plt.plot(s_list)
plt.show()