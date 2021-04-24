n=int(input())
abc=[]
for _ in range(n):
    abc.append(map(int, input().split()))

ia=0
ib=1
ic=2
dp=[]
dp.append([0]*n)
dp.append([0]*n)
dp.append([0]*n)

# 1日目
a,b,c=abc[0]
dp[ia][0] = a
dp[ib][0] = b 
dp[ic][0] = c

for i in range(1, n):
    a,b,c=abc[i]
    dp[ia][i] = max(dp[ia][i], dp[ib][i-1]+a)
    dp[ia][i] = max(dp[ia][i], dp[ic][i-1]+a)

    dp[ib][i] = max(dp[ib][i], dp[ic][i-1]+b)
    dp[ib][i] = max(dp[ib][i], dp[ia][i-1]+b)

    dp[ic][i] = max(dp[ic][i], dp[ia][i-1]+c)
    dp[ic][i] = max(dp[ic][i], dp[ib][i-1]+c)

print(max(dp[ia][n-1], dp[ib][n-1], dp[ic][n-1]))
