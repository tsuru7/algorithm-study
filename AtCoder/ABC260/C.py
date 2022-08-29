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
    n,x,y=m_input()
    return n,x,y


def solve(n,x,y):
    def red(n):
        if n == 1:
            return 0
        else:
            return (x+1)*red(n-1) + x*y*blue(n-1)

    def blue(n):
        if n == 1:
            return 1
        else:
            return red(n-1)+y*blue(n-1)

    return red(n)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y=readinput()
    ans=solve(n,x,y)
    printans(ans)
