import sys
a=int(sys.stdin.readline())
m=[0]*10001
for j in range(a):
    m[int(sys.stdin.readline())]+=1

for i in range(len(m)):
    if m[i]!=0:
        for z in range(m[i]):
            print(i)