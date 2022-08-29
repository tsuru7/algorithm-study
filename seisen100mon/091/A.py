import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import atan, pi, degrees

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
    a,b,x=m_input()
    return a,b,x

def solve(a,b,x):
    if 2*x >= a*a*b:
        # case 1
        tantheta = 2*(a*a*b-x)/(a*a*a)
        theta = degrees(atan(tantheta))
    else:
        # case 2
        tantheta = a*b*b/(2*x)
        theta = degrees(atan(tantheta))
    return theta

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,x=readinput()
    ans=solve(a,b,x)
    printans(ans)
