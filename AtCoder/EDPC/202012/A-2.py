import sys
INFTY = sys.maxsize

n = int(input())
h = list(map(int, input().split()))
h.insert(0, INFTY)

dp = [INFTY]*(n+1)
dp[1] = 0
for i in range(2, n+1):
    if i-1>=1:
        dp[i] = min(dp[i], dp[i-1]+abs(h[i-1]-h[i]))
    if i-2>=1:
        dp[i] = min(dp[i], dp[i-2]+abs(h[i-2]-h[i]))

print(dp[n])

