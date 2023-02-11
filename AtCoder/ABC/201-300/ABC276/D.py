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
    n=i_input()
    a=l_input()
    return n,a

def solve(n,a):
    gcd_all = gcd(a[0], a[1])
    for i in range(2, n):
        gcd_all = gcd(gcd_all, a[i])
    ans=0
    for i in range(n):
        tmp = a[i] // gcd_all
        while tmp % 2 == 0:
            tmp //= 2
            ans += 1
        while tmp %3 == 0:
            tmp //= 3
            ans += 1
        if tmp != 1:
            return -1

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
