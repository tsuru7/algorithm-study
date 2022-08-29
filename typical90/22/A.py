import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import gcd

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
    a,b,c=m_input()
    return a,b,c

def solve(a,b,c):
    tmp=gcd(gcd(a,b),c)
    # print(f'tmp: {tmp}')
    ans = (a//tmp-1) + (b//tmp-1) + (c//tmp-1)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c=readinput()
    ans=solve(a,b,c)
    printans(ans)
