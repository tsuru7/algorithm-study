import sys
INFTY=sys.maxsize

n, wlim = map(int, input().split())
wvList = []
for _ in range(n):
    wvList.append(map(int, input().split()))

dp = []
for i in range(10**5+1):
    dp.append([INFTY]*(n+1))

dp[0][0] = 0
for i in range(1, n+1):
    w, v = wvList[i-1]
    for j in range(10**5+1):
        if dp[j][i-1] < INFTY:
            dp[j][i] = dp[j][i-1] # 買わない場合は重さは同じ
            # print('not buy: dp[{}][{}] = {}'.format(j, i, dp[j][i]))
        if j-v >= 0 and dp[j-v][i-1] < INFTY:
            dp[j][i] = min(dp[j][i], dp[j-v][i-1]+w) # 買う場合は同じ価値でより軽い方
            # print('buy: dp[{}][{}] = {}'.format(j, i, dp[j][i]))

vmax = 0
for j in range(10**5+1):
    if dp[j][n] <= wlim:
        # print('dp[{}][{}]: {}'.format(j,n,dp[j][n]))
        vmax = max(vmax, j)
print(vmax)