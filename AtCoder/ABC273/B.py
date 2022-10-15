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
    x,k=m_input()
    return x,k

def solve(x,k):
    base = 1
    for i in range(k):
        x, r = divmod(x, 10)
        if r >= 5:
            x += 1
        base *= 10
    return x*base

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,k=readinput()
    ans=solve(x,k)
    printans(ans)
