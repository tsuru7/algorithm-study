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
    x,y,n=m_input()
    return x,y,n

def solve(x,y,n):
    if 3*x > y:
        ny = n // 3
        nx = n % 3
    else:
        nx = n
        ny = 0
    ans=y*ny+x*nx
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,y,n=readinput()
    ans=solve(x,y,n)
    printans(ans)
