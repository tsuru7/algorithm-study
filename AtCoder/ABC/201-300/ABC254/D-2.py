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
    return n

def solve(n):
    ans=0
    for i in range(1, n+1):
        x = 1
        xmax = x
        while x*x <= n:
            if i % (x*x) == 0:
                xmax = x
            x += 1
        m = i // (xmax*xmax)
        j = 1
        while m*j*j <= n:
            ans += 1
            j += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n=readinput()
    ans=solve(n)
    printans(ans)
