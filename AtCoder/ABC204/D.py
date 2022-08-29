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
    t=l_input()
    return n,t

def main(n,t):
    total = sum(t)
    dp = [[False]*(10**5+1) for _ in range(100)]
    dp[0][0] = True
    dp[0][t[0]] = True
    for i in range(n-1):
        for j in range(10**5+1):
            if dp[i][j]:
                dp[i+1][j] = True
                dp[i+1][j+t[i+1]] = True
    ans = INFTY
    for j in range(10**5+1):
        if dp[n-1][j]:
            other = total - j
            ans = min(ans, max(j, other))

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,t=readinput()
    ans=main(n,t)
    printans(ans)
