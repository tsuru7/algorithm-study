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
    t=i_input()
    return t

def f(x):
    return x*x + 2*x + 3

def solve(t):

    # f(f(f(t)+t)+f(f(t)))

    ans=f(f(f(t)+t)+f(f(t)))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    t=readinput()
    ans=solve(t)
    printans(ans)
