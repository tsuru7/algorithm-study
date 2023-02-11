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
    n,m,x,t,d=m_input()
    return n,m,x,t,d

def solve(n,m,x,t,d):
    t0 = t - d*x
    if m >= x:
        return t
    else:
        return t0+d*m

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,x,t,d=readinput()
    ans=solve(n,m,x,t,d)
    printans(ans)
