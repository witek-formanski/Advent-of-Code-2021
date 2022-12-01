# 2022-11-05
#	23:14 - 0:21

with open('notepad/209_advent_2021_day_14.txt', 'r') as f:
	file = f.readlines()
	template = file[0].strip()
	data = [x.strip().split(' -> ') for x in file[2:]]
print(template)
# print(data)

rules = {}
for i in data:
	rules[i[0]] = i[1]
print(rules)

# create {pairs_dict} - dictionary storing number of current pairs of adjacent characters
pairs_dict = {}
for pair in rules.keys():
	pairs_dict[pair] = 0
print(pairs_dict)

# create {char_dict} - dictionary storing number of each character
chars_dict = {}
for char in set(rules.values()):
	chars_dict[char] = 0
# print(chars_dict)

# before any steps:
for i in range(len(template)-1):
	pairs_dict[template[i] + template[i+1]] += 1
	chars_dict[template[i]] += 1
chars_dict[template[-1]] += 1
# print(pairs_dict)
# print(chars_dict)

def step(n):
	global pairs_dict, chars_dict, rules
	for i in range(n):
		new_pairs_dict = pairs_dict.copy()
		new_chars_dict = chars_dict.copy()
		for key, value in pairs_dict.items():
			new_chars_dict[rules[key]] += value
			new_pairs_dict[key[0] + rules[key]] += value
			new_pairs_dict[rules[key] + key[1]] += value
			new_pairs_dict[key] -= value
		pairs_dict = new_pairs_dict
		chars_dict = new_chars_dict
		# print('\n\nstep', i, ':\n', chars_dict, '\n', pairs_dict)
	ans = max(chars_dict.values()) - min(chars_dict.values())
	return ans
print(step(40))