def readinput():
    n = input()
    return n

def solve(n):
    '''
    N以下の非負整数の個数を求める（自明なサンプル）
    '''
    l = len(n)
    dp = [[0 for _ in range(2)] for _ in range(l+1)]
    dp[0][1] = 1

    for i in range(l):
        di = int(n[i])
        # smaller -> smaller (d: [0..9])
        for d in range(10):
            dp[i+1][0] += dp[i][0]
        # equal -> smaller (d: [0..di-1])
        for d in range(di):
            dp[i+1][0] += dp[i][1]
        # equal -> equal (d: di)
        dp[i+1][1] += dp[i][1]
    return dp[l][0] + dp[l][1]

def printans(ans):
    print(ans)
    return

if __name__ == '__main__':
    n = readinput()
    ans = solve(n)
    printans(ans)
