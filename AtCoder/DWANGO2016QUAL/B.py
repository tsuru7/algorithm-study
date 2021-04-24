n = int(input())
k = list(map(int, input().split()))
l = [0]*n
l[0] = k[0]
for i in range(1, n-1):
    l[i] = min(k[i-1], k[i])
l[n-1] = k[n-2]
print(' '.join(map(str, l)))
