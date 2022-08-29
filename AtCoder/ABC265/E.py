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
    n,m=m_input()
    a,b,c,d,e,f=m_input()
    xyList = [l_input() for _ in range(m)]
    return n,m,a,b,c,d,e,f,xyList

def to1d(m1, m2):
    return m1*n+m2

def to2d(x):
    return divmod(x, n)

def solve(n,m,a,b,c,d,e,f,xyList):
    dp = [[0 for _ in range((n+1)*(n+1))] for _ in range(n+1)]
    x1 = a
    y1 = b
    x2 = c
    y2 = d
    x3 = e
    y3 = f

    shogai = set()
    for x, y in xyList:
        shogai.add((x, y))

    MOD = 998244353
    dp[0][0] = 1
    for i in range(n):
        for j1 in range(i+1):
            for j2 in range(i+1):
                j3 = i-j1-j2
                if j3 < 0:
                    continue

                dp[i+1][to1d(j1+1, j2)] += dp[i][to1d(j1, j2)]  # step 1
                dp[i+1][to1d(j1+1, j2)] %= MOD
                x = (j1+1)*x1+j2*x2+j3*x3
                y = (j1+1)*y1+j2*y2+j3*y3
                if (x, y) in shogai:
                    dp[i+1][to1d(j1+1, j2)] = 0

                dp[i+1][to1d(j1, j2+1)] += dp[i][to1d(j1, j2)]  # step 2
                dp[i+1][to1d(j1, j2+1)] %= MOD
                x = j1*x1+(j2+1)*x2+j3*x3
                y = j1*y1+(j2+1)*y2+j3*y3
                if (x, y) in shogai:
                    dp[i+1][to1d(j1, j2+1)] = 0

                dp[i+1][to1d(j1, j2)]   += dp[i][to1d(j1, j2)]  # step 3
                dp[i+1][to1d(j1, j2)]   %= MOD
                x = j1*x1+j2*x2+(j3+1)*x3
                y = j1*y1+j2*y2+(j3+1)*y3
                if (x, y) in shogai:
                    dp[i+1][to1d(j1, j2)] = 0


    ans=sum(dp[n]) % MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a,b,c,d,e,f,xyList=readinput()
    ans=solve(n,m,a,b,c,d,e,f,xyList)
    printans(ans)
