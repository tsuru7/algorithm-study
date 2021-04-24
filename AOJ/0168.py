n=int(input())
nList = []
while n > 0:
    nList.append(n)
    n=int(input())

maxn = max(nList)

dp = [0]*(maxn+1)
dp[0] = 1
for i in range(1, maxn+1):
    if i > 2:
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    elif i == 2:
        dp[i] = dp[i-2] + dp[i-1]
    elif i == 1:
        dp[i] = dp[i-1]

for n in nList:
    npattern = dp[n]
    years = npattern // 3650
    if npattern % 3650 != 0:
        years += 1
    print(years)


    