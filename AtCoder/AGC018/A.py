from math import gcd

n, k = map(int, input().split())
a = list(map(int, input().split()))

if n == 1:
    if a[0] == k:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
    exit()

maxa = max(a[0], a[1])
g = gcd(a[0], a[1])
for i in range(2, n):
    g = gcd(g, a[i])
    maxa = max(maxa, a[i])

if k <= maxa and k % g == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')