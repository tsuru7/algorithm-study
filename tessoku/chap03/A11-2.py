import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right

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
    a=l_input()
    return n,x,a

def solve(n,x,a):
    ans = bisect_right(a, x)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,a=readinput()
    ans=solve(n,x,a)
    printans(ans)
