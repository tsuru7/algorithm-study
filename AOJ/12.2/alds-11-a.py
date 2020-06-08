n=int(input())
L=[]
for l in range(n):
    L.append([])
M=[]
for m in range(n):
    mm=[0]*n
    M.append(mm)

for i in range(n):
    inp=list(map(int,input().split()))
    #print()
    L[inp[0]-1]=inp[2:]

for i,l in enumerate(L):
    for k in l:
        M[i][k-1]=1

for m in M:
    print(' '.join(map(str,m)))

