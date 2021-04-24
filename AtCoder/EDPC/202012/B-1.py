import sys
INFTY=sys.maxsize

n,k=map(int,input().split())
h=list(map(int,input().split()))
h.insert(0,INFTY)

dp = [INFTY]*(n+1)
dp[1] = 0

# 配るDP
for i in range(1, n):
    for kk in range(1, k+1):
        if i+kk<=n:
            dp[i+kk]=min(dp[i+kk], dp[i]+abs(h[i]-h[i+kk]))
        else:
            break
print(dp[n])
