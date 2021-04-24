def readinput():
    n=int(input())
    s = []
    for _ in range(n):
        s.append(input())
    return n,s

def main(n,s):
    dp = [ [0, 0] for i in range(n+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(n):
        if s[i] == 'AND':
            dp[i+1][0] = dp[i][0]*2 + dp[i][1]
            dp[i+1][1] = dp[i][1]
        else:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][0] + dp[i][1]*2
    return dp[n][1]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    printans(ans)
