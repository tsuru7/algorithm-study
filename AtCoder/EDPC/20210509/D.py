import sys
sys.setrecursionlimit(10**5)
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
    n,w=m_input()
    wv = []
    for _ in range(n):
        wv.append(l_input())
    return n,w,wv

def main(n,w,wv):
    dp = []
    for _ in range(n+1):
        dp.append([-10**18]*(w+1))
    dp[0][0] = 0
    for i in range(1, n+1):
        wi, vi = wv[i-1]
        for j in range(w+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j-wi >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-wi]+vi)
        print(dp)
    return dp[n][w]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,w,wv=readinput()
    ans=main(n,w,wv)
    printans(ans)
