#19.08.2022

x = 0 
y = 0

with open('notepad/134_2.txt') as f:
    aa = f.readlines()

print(aa)

bbb = []
for a in aa:
	bb = a.split()
	bbb.append(bb)

print(bbb)

for bb in bbb:
	if bb[0] == 'forward':
		x += int(bb[1])
	elif bb[0] == 'down':
		y += int(bb[1])
	elif bb[0] == 'up':
		y -= int(bb[1])


print(x)
print(y)
print(x*y)