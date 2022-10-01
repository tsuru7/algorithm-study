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
    slist = [input() for _ in range(5)]
    return n,slist

def solve(n,slist):
    dp = [[INFTY, INFTY, INFTY] for _ in range(n+1)]
    color = ['R', 'B', 'W']
    dp[0] = [0, 0, 0]
    for i in range(1, n+1):
        for j in range(3):
            count = 0
            for row in range(5):
                if slist[row][i-1] != color[j]:
                    count += 1
            for k in range(3):
                if k == j:
                    continue
                dp[i][j] = min(dp[i][j], dp[i-1][k] + count)

    return min(dp[-1])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,slist=readinput()
    ans=solve(n,slist)
    printans(ans)
