n = int(input())
ij = []
for i in range(1,n+1):
    r = n % i
    if (r != 0):
        continue
    j = n // i
    ij.append(i+j-2)
#print(ij)
print(min(ij))
