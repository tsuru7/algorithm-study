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
    x,y=m_input()
    return x,y

def solve(x,y):
    if (2*y-x) % 3 != 0:
        return 0
    if (2*x-y) % 3 != 0:
        return 0
    u = (2*y-x)//3
    r = (2*x-y)//3
    if u < 0:
        return 0
    if r < 0:
        return 0
    MOD = 10**9+7
    if u > r:
        u, r = r, u
    bunsi = 1
    bunbo = 1
    ans = 1
    for i in range(u):
        bunsi *= r+1+i
        bunsi %= MOD
        bunbo *= 1+i
        bunbo %= MOD
    return (bunsi * pow(bunbo, MOD-2, MOD)) % MOD

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,y=readinput()
    ans=solve(x,y)
    printans(ans)
