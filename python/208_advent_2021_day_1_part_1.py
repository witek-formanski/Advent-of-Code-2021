# 2022-10-28
#	21:33 - 21:47

ans = 0

with open('notepad/208_advent_2021_day_1.txt', 'r') as f:
	data = f.readlines()
	for i in range(len(data)-1):
		line_1 = int(data[i+1].strip())
		line_2 = int(data[i].strip())
		if line_1 > line_2:
			ans += 1
print(ans)