import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import cos, sin, pi

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
    a,b,d=m_input()
    return a,b,d

def solve(a,b,d):
    rad = d/180*pi
    # x = cos(rad)*a+sin(rad)*b
    # y = -sin(rad)*a+cos(rad)*b
    # print(x, y)
    z = complex(a, b)
    r = complex(cos(rad), sin(rad))
    ans = z*r
    # print(ans)
    return ans.real, ans.imag

def printans(ans):
    print(*ans)

if __name__=='__main__':
    a,b,d=readinput()
    ans=solve(a,b,d)
    printans(ans)
