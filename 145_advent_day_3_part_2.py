#20.08.2022

with open('notepad/137_2.txt') as f:
    data = f.readlines()
# print(data)
# print(len(data))

oxygen = []
for i in data:
	oxygen.append(i.rstrip())
# print(oxygen)
# print(len(oxygen))


for j in range(0,len(oxygen[0])):	#12
	zeros_list = []
	ones_list = []
	zeros = 0
	ones = 0
	for i in range(0,len(oxygen)):	#1000		
		if oxygen[i][j] == '0':
			zeros_list.append(oxygen[i])
		elif oxygen[i][j] == '1':
			ones_list.append(oxygen[i])
	print(f'step {j}: zeros = {len(zeros_list)}, ones = {len(ones_list)}')

	if len(zeros_list) > len(ones_list):
		oxygen = zeros_list
		print(f'step {j}: zeros')
	elif len(zeros_list) < len(ones_list):
		oxygen = ones_list
		print(f'step {j}: ones')
	elif len(zeros_list) == len(ones_list):
		oxygen = ones_list
		print(f'step {j}: tie')
	print(f'step {j}, len(oxygen) = {len(oxygen)}\n')

# print(len(oxygen))
print(f'oxygen binary = {oxygen}')
ox = int(oxygen[0], 2)
print(f'oxygen decimal = {ox}\n\n')


carbon_dioxide = []
for i in data:
	carbon_dioxide.append(i.rstrip())

for j in range(0,len(carbon_dioxide[0])):	#12
	if len(carbon_dioxide) == 1:
		break
	else:
		zeros_list = []
		ones_list = []
		zeros = 0
		ones = 0
		for i in range(0,len(carbon_dioxide)):	#1000		
			if carbon_dioxide[i][j] == '0':
				zeros_list.append(carbon_dioxide[i])
			elif carbon_dioxide[i][j] == '1':
				ones_list.append(carbon_dioxide[i])
		print(f'step {j}: zeros = {len(zeros_list)}, ones = {len(ones_list)}')

		if len(zeros_list) < len(ones_list):
			carbon_dioxide = zeros_list
			print(f'step {j}: zeros')
		elif len(zeros_list) > len(ones_list):
			carbon_dioxide = ones_list
			print(f'step {j}: ones')
		elif len(zeros_list) == len(ones_list):
			carbon_dioxide = zeros_list
			print(f'step {j}: tie')
		print(f'step {j}, len(carbon_dioxide) = {len(carbon_dioxide)}\n')

print(f'carbon_dioxide binary = {carbon_dioxide}')
co2 = int(carbon_dioxide[0], 2)
print(f'carbon_dioxide decimal = {co2}\n\n')

x = ox * co2
print(x)