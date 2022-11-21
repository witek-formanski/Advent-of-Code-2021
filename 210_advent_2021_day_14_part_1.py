# 2022-11-03
#	22:32 - 23:47

with open('notepad/209_advent_2021_day_14.txt', 'r') as f:
	file = f.readlines()
	template = file[0].strip()
	data = [x.strip().split(' -> ') for x in file[2:]]
# print(template)
# print(data)

# create a glossary (rules) from data list (data)
# create a set (rules_keys) of glossary keys (from 0th element of each data list's element)
rules = {}
rules_keys = set([])
for i in data:
	rules[i[0]] = i[1]
	rules_keys.add(i[0])
# print(rules)
# print(rules_keys)

def step(n):
	for j in range(n):
		global template, rules, rules_keys
		draft_template = ''
		for i in range(len(template)-1):
			pair = template[i] + template[i+1]
			# print(pair)
			if pair in rules_keys:
				inserted_element = rules[pair]
				draft_template += template[i] + inserted_element
			elif pair not in rules_keys:
				draft_template += template[i]
				print('NONE!', 'i = ', i)
		draft_template += template[i+1]
		template = draft_template
		# print('step ', j+1)
	return template
# print(step(10))

characters_list = [*step(10)]
characters_set = set(characters_list)
characters_glossary = {}
for character in characters_set:
	characters_glossary[character] = characters_list.count(character)
print(characters_glossary)
values = characters_glossary.values()
ans = max(values) - min(values)
print(ans)


