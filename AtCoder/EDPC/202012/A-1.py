import sys
INFTY = sys.maxsize

n = int(input())
h = list(map(int, input().split()))
h.insert(0, INFTY)

dp = [INFTY]*(n+1)
dp[1] = 0
for i in range(1,n):
    if i+1 <= n:
        dp[i+1] = min(dp[i+1], dp[i]+abs(h[i]-h[i+1]))
    if i+2 <= n:
        dp[i+2] = min(dp[i+2], dp[i]+abs(h[i]-h[i+2]))
print(dp[n])


