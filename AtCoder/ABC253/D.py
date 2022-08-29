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
    n,a,b=m_input()
    return n,a,b

def solve(n,a,b):
    sum1 = n*(n+1)//2
    m = n//a
    sum2 = a*m*(m+1)//2
    l = n//b
    sum3 = b*l*(l+1)//2
    lcm = a*b//gcd(a,b)
    k = n//lcm
    sum4 = lcm*k*(k+1)//2
    ans=sum1-sum2-sum3+sum4
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a,b=readinput()
    ans=solve(n,a,b)
    printans(ans)
