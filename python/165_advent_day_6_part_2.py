#25.08.2022

with open('notepad/163_2.txt') as f:
	data = f.readlines()

data_list = list(data[0].split(','))
initial = [int(x) for x in data_list]
print(initial)
print(len(initial))

# zero, one, two, three, four, five = 0,0,0,0,0,0
# for i in initial:
# 	if i==0:
# 		zero+=1
# 	elif i==1:
# 		one+=1
# 	elif i==2:
# 		two+=1
# 	elif i==3:
# 		three+=1
# 	elif i==4:
# 		four+=1
# 	elif i==5:
# 		five+=1


# glossary!
fishies = {
	'fish0': initial.count(0), 'fish1': initial.count(1), 
	'fish2': initial.count(2), 'fish3': initial.count(3), 
	'fish4': initial.count(4), 'fish5': initial.count(5),
	'fish6': initial.count(6), 'fish7': initial.count(7),
	'fish8': initial.count(8), 'fish9': initial.count(9),
	}
print(fishies)

for i in range(256):
	k = fishies['fish0']
	fishies['fish9'] = k
	fishies['fish7'] += k
	fishies['fish0'] = fishies['fish1']
	fishies['fish1'] = fishies['fish2']
	fishies['fish2'] = fishies['fish3']
	fishies['fish3'] = fishies['fish4']
	fishies['fish4'] = fishies['fish5']
	fishies['fish5'] = fishies['fish6']
	fishies['fish6'] = fishies['fish7']
	fishies['fish7'] = fishies['fish8']
	fishies['fish8'] = fishies['fish9']
	fishies['fish9'] = 0
	print(i, fishies)
# 	initial.extend([9]*initial.count(0))
# 	initial = [6 if x==0 else x-1 for x in initial]
# print(initial)
# print(len(initial))

x = fishies['fish0']+fishies['fish1']+fishies['fish2']+fishies['fish3']+fishies['fish4']+fishies['fish5']+fishies['fish6']+fishies['fish7']+fishies['fish8']+fishies['fish9']
print(x)