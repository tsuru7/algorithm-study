import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    n=i_input()
    a=l_input()
    return n,a

def solve(n,a):
    '''
    m 個選んで平均値が整数になる通り数を求めて、m = 1..n の和を取る
    m 個選んで平均値が整数になる⇒m 個選んで m の倍数になる
    dp[i][j][k] : i 番目までで j 個選んだとき m で割った余りが k となる通り数
    dp[i+1][j][k] += dp[i][j][k]   # i 番目を選ばないとき
    dp[i+1][j+1][(k + ai) % m] += dp[i][j][k]  # i 番目を選ぶとき
    '''
    MOD = 998244353 
    ans=0
    for m in range(1, n+1):
        if m == 1:
            ans += n
            continue
        dp = [[[0 for _ in range(m)] for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0][0] = 1
        for i in range(n):
            ai = a[i]
            for j in range(m+1):
                for k in range(m):
                    dp[i+1][j][k] += dp[i][j][k]
                    dp[i+1][j][k] %= MOD
                    if j+1 <= m:
                        dp[i+1][j+1][(k+ai) % m] += dp[i][j][k]
                        dp[i+1][j+1][(k+ai) % m] %= MOD
        ans += dp[n][m][0]
        ans %= MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
