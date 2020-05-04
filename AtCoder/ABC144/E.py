import numpy as np

n, k = list(map(int,input().split()))
a = list(map(int,input().split()))
f = list(map(int,input().split()))
af = [ ai*fi for ai, fi in zip(a,f)]
af_sorted = af.copy()
af_sorted.sort(reverse=True)
ndim = af_sorted[0]
af_mat = np.zeros((ndim,ndim))
for j in range(0,len(af_sorted)):
    i = 0
    while (i<af_sorted[j]):
        af_mat[i,j] = 1
        i+=1

cost = 0
i = ndim-1
while (cost < k):
    j = 0
    while (af_mat[i,j]>0):
        j += 1
    cost += j
    i -= 1
print(i-1)
