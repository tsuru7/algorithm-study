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
    a,b=m_input()
    return a,b

def solve(a,b):
    if a//gcd(a, b) <= 10**18//b:
        return a*b//gcd(a, b)
    else:
        return 'Large'

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=solve(a,b)
    printans(ans)
