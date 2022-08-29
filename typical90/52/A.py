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
    amat = [l_input() for _ in range(n)]
    return n,amat

def solve(n,amat):
    MOD = 10**9+7
    asum = [sum(amat[row]) for row in range(n)]
    ans=1
    for i in range(n):
        ans *= asum[i]
        ans %= MOD
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,amat=readinput()
    ans=solve(n,amat)
    printans(ans)
