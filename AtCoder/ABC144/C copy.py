from math import sqrt
n = int(input())
ij = []
i = 0
nr = int(sqrt(n))+1
while (i<=nr):
    i += 1
    r = n % i
    if (r != 0):
        continue
    j = n // i
    ij.append(i+j-2)
#print(ij)
print(min(ij))
