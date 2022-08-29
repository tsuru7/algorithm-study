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
    n=i_input()
    p=l_input()
    return n,p

def main(n,p):
    dp = []
    for _ in range(n+1):
        dp.append([0]*10001)
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(10001):
            if dp[i-1][j] > 0:
                dp[i][j] += dp[i-1][j]
                dp[i][j+p[i-1]] += dp[i-1][j]
    
    ans=0
    for j in range(10001):
        if dp[n][j] > 0:
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p=readinput()
    ans=main(n,p)
    printans(ans)
