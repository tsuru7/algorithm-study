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
    p=l_input()
    return n,x,p

def solve(n,x,p):
    for i in range(n):
        if p[i] == x:
            return i+1

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,p=readinput()
    ans=solve(n,x,p)
    printans(ans)
