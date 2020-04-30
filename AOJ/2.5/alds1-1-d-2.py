n = int(input())
r = []
for i in range(n):
    r.append(int(input()))

rmin = r[0]
dmax = -10**9

for i in range(1, n):
    d = r[i] - rmin
    if (d > dmax):
        dmax = d
    if (r[i]<rmin):
        rmin = r[i]

print(dmax)
