n = int(input())
r = []
for i in range(n):
    r.append(int(input()))

rmax = -10**9

for i in range(n):
    j=i+1
    while (j<n):
        rij = r[j]-r[i]
        if (rij>rmax):
            rmax = rij
        j += 1

print(rmax)
