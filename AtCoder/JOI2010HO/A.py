n, m = map(int, input().split())
s = []
for _ in range(n-1):
    s.append(int(input()))
a = []
for _ in range(m):
    a.append(int(input()))

l = [0]*(n+1)
l[1] = 0
for i in range(2, n+1):
    l[i] = l[i-1] + s[i-2]

MOD=10**5
now = 1
dist = 0
for day in range(m):
    next = now + a[day]
    dist = (dist + abs(l[next] - l[now])) % MOD
    now = next

print(dist)

