import sys
INFTY=sys.maxsize

n,k=map(int,input().split())
h=list(map(int,input().split()))
h.insert(0,INFTY)

dp = [INFTY]*(n+1)
dp[1] = 0

# もらうDP
for i in range(2, n+1):
    for kk in range(1, k+1):
        if i-kk>=1:
            dp[i]=min(dp[i], dp[i-kk]+abs(h[i]-h[i-kk]))
        else:
            break
print(dp[n])
