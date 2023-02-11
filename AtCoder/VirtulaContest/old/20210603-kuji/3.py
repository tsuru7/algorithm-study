import sys
sys.setrecursionlimit(10**5)
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
    a,b,c,d=m_input()
    return a,b,c,d

def main(a,b,c,d):
    ans = b//c - (a-1)//c
    ans += b//d - (a-1)//d
    lcm = c*d//gcd(c,d)
    ans -= b//lcm - (a-1)//lcm
    ans=b-(a-1)-ans
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,c,d=readinput()
    ans=main(a,b,c,d)
    printans(ans)
