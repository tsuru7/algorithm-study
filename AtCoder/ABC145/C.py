from itertools import permutations
from math import sqrt

n=int(input())
permlist = list(permutations(range(n)))
#print('permlist: {}'.format(permlist))

x = []
y = []
for i in range(n):
    xi,yi = list(map(int,input().split()))
    x.append(xi)
    y.append(yi)

lengths = 0.0
for p in permlist:
    length = 0.0
    for _ in range(len(p)-1):
        i = p[_]
        j = p[_+1]
        #print('i: {} j:{}'.format(i,j))
        length += sqrt( (x[i]-x[j])**2 + (y[i]-y[j])**2 )
    #print('length: {}'.format(length))
    lengths += length

print(lengths/len(permlist))
