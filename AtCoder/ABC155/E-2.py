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
    n=input()
    return n

def solve(n):
    l = len(n)
    dp0 = [0 for _ in range(l+1)]
    dp1 = [0 for _ in range(l+1)]
    dp1[0] = 1
    for i in range(l):
        di = int(n[i])
        if di == 0:
            dp0[i+1] = dp0[i]
        else:
            dp0[i+1] = min(dp0[i]+di, dp1[i]+10-di)
        if di == 9:
            dp1[i+1] = dp1[i]
        else:
            dp1[i+1] = min(dp0[i]+di+1, dp1[i]+10-di-1)
    return dp0[l]

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
