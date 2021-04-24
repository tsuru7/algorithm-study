n, w=map(int, input().split())
wv=[]
for _ in range(n):
    wv.append(list(map(int, input().split())))
# print(wv)

dp=[]
for _ in range(w+1):
    dp.append([0]*(n+1))

for i in range(1, n+1):
    wi,vi=wv[i-1]
    # print(wi,vi)
    for j in range(w+1):
        dp[j][i] = dp[j][i-1]
        if j-wi>=0:
            dp[j][i] = max(dp[j][i], dp[j-wi][i-1]+vi)
print(dp[w][n])
# for i in range(w+1):
#     print(dp[i])
        