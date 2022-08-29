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
    a,b,c,x,y=m_input()
    return a,b,c,x,y

def solve(a,b,c,x,y):
    ans = INFTY
    for nc in range(2*max(x,y)+1):
        na = max(0, x - nc//2)
        nb = max(0, y - nc//2)
        price = na*a + nb*b + nc*c
        ans = min(ans, price)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c,x,y=readinput()
    ans=solve(a,b,c,x,y)
    printans(ans)
