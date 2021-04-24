n = int(input())
a = list(map(int, input().split()))

s = [0]*(n+1)
s[0] = 0
for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]

for k in range(1, n+1):
    i = 0
    maxvalue = 0
    while i+k <= n:
        maxvalue = max(maxvalue, s[i+k] - s[i])
        i += 1
    print(maxvalue)

