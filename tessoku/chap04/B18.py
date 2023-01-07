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
    n,s=m_input()
    a=l_input()
    return n,s,a

def solve(n,s,a):
    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        ai = a[i]
        for j in range(s+1):
            dp[i+1][j] |= dp[i][j]
            if j+ai <= s:
                dp[i+1][j+ai] |= dp[i][j]
    if dp[n][s]:
        ans = []
        j = s
        for i in range(1, n+1)[::-1]:
            ai = a[i-1]
            if j-ai >= 0 and dp[i-1][j-ai]:
                ans.append(i)
                j -= ai
                # print(j, ai)
        return ans[::-1]
    else:
        return [-1]

def printans(ans):
    if ans == [-1]:
        print(*ans)
    else:
        print(len(ans))
        print(*ans)

if __name__=='__main__':
    n,s,a=readinput()
    ans=solve(n,s,a)
    printans(ans)
