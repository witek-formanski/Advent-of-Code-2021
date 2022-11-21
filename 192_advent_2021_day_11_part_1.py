# 2022-10-03
# 	16:07 - ?
# 2022-10-04
# 	13:57 - ?
# 2022-10-05
#	15:42 - ?
# 2022-10-09
#	14:27 - 14:59

import numpy as np

def read_data(filename):
	open_file = open(filename, 'r')
	lines_list = []
	for line in open_file.readlines():
		line = [int(string) for string in [*line.strip()]]
		lines_list.append(line)
	return lines_list
data = read_data('notepad/182_2.txt')

minus_value = -100
minus_line1 = [minus_value for i in range(10)]
minus_line2 = [minus_value for i in range(10)]
data.insert(0, minus_line1)
data.append(minus_line2)

for line_number in range(len(data)):						# ???
	data[line_number].insert(0, minus_value)
	data[line_number].append(minus_value)

print(f'before any steps:\n {np.asarray(data)}')

# number_of_flashes = 0

# def add(data):
# 	for line_number in range(1,len(data)-1):
# 		for octopus_number in range(1,len(data[line_number])-1):
# 			data[line_number][octopus_number]+=1

# def single_flash(data):
# 	if data[line_number][octopus_number] > 9:
# 		data[line_number+1][octopus_number]+=1
# 		data[line_number-1][octopus_number]+=1
# 		data[line_number][octopus_number+1]+=1
# 		data[line_number][octopus_number-1]+=1
# 		data[line_number+1][octopus_number+1]+=1
# 		data[line_number+1][octopus_number-1]+=1
# 		data[line_number-1][octopus_number+1]+=1
# 		data[line_number-1][octopus_number-1]+=1


def step(data, number_of_steps):
	number_of_single_flashes = 0
	# ADD
	for step_number in range(number_of_steps):
		for line_number in range(1,len(data)-1):
			for octopus_number in range(1,len(data[line_number])-1):
				data[line_number][octopus_number]+=1
		print(f'step {step_number} after ADD:\n {np.asarray(data)}')
	
	# FLASH		
		active = True
		k = 0
		flashed = []
		while active == True:
			k+=1
			data_copy = [i.copy() for i in data]
			# in_use = []
			

			for line_number in range(1,len(data)-1):
				for octopus_number in range(1,len(data[line_number])-1):
					in_use = [line_number, octopus_number]
					if in_use not in flashed and data[line_number][octopus_number] > 9:
						data[line_number+1][octopus_number]+=1
						data[line_number-1][octopus_number]+=1
						data[line_number][octopus_number+1]+=1
						data[line_number][octopus_number-1]+=1
						data[line_number+1][octopus_number+1]+=1
						data[line_number+1][octopus_number-1]+=1
						data[line_number-1][octopus_number+1]+=1
						data[line_number-1][octopus_number-1]+=1
						flashed.append(in_use)
						number_of_single_flashes+=1
			print('multiple flash')
			if data_copy == data:
				active = False
		print(f'step {step_number} after FLASH:\n {np.asarray(data)}')

	# EXHAUST
		for coordinates_list in flashed:
			data[coordinates_list[0]][coordinates_list[1]] = 0
		print(f'step {step_number} after EXHAUST:\n {np.asarray(data)}')



	print(f'number_of_single_flashes = {number_of_single_flashes}')
step(data,100)