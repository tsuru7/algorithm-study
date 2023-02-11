import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import sqrt

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
    h=i_input()
    return h

def solve(h):
    ans = sqrt(h*(12800000+h))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    h=readinput()
    ans=solve(h)
    printans(ans)
