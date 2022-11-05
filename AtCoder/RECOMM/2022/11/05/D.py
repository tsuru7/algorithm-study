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
    n,x=m_input()
    return n,x

def nlayer(n):
    return pow(2, n+2) - 3

def npaty(n):
    return pow(2, n+1) - 1

def dfs(level, x):
    if x <= 1:
        return 0
    if 1 < x < 1 + nlayer(level-1):
        return dfs(level-1, x-1)
    if 1 + nlayer(level-1) == x:
        return npaty(level-1)
    if 1 + nlayer(level-1) + 1 == x:
        return npaty(level-1) + 1
    if 1 + nlayer(level-1) + 1 < x < 1 + nlayer(level-1) + 1 + nlayer(level-1):
        return npaty(level-1) + 1 + dfs(level-1, x-(1+nlayer(level-1)+1))
    return npaty(level)

def solve(n,x):

    return dfs(n, x)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x=readinput()
    ans=solve(n,x)
    printans(ans)
