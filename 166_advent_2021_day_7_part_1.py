#31.08.2022

with open('notepad/166_2.txt') as f:
	data = f.readlines()
# print(data)

data_split = data[0].split(',')
# print(data_split)
# print(len(data_split))

data_final = []
for i in data_split:
	j = int(i)
	data_final.append(j)
# print(data_final)

max_ = max(data_final)
min_ = min(data_final)
# print(max_, min_)

# s_i - fuel consumption
s_list = []
for i in range(min_, max_+1):
	s_i = 0
	for j in data_final:
		s_i += abs(j-i)
	s_list.append(s_i)
# print(s_list)
print(min(s_list))

from matplotlib import pyplot as plt
plt.plot(s_list)
plt.show()