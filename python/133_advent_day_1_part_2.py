#19.08.2022

with open('notepad/133_2.txt') as f:
    L = f.readlines()
# print(L)
# print(len(L))

M = []
for i in range(0,len(L)-2):
    m = []
    m.append(int(L[i].rstrip()))
    m.append(int(L[i+1].rstrip()))
    m.append(int(L[i+2].rstrip()))
    n = sum(m)
    M.append(n)

# print(M)
# print(len(M))

x = 0
for i in range(0,len(M)-1):
    if M[i+1] > M[i]:
        x += 1
    else:
        continue
print(x)


