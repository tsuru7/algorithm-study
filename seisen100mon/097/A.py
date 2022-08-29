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
    n,m=m_input()
    a=l_input()
    return n,m,a

def solve(n,m,a):
    if n == 1:
        b = [0]
        b[0] = a[0]//2
        return m//b[0] - m//(2*b[0])
    # n >= 2
    b = [a[i]//2 for i in range(n)]
    # print(f'b: {b}')
    lcm = b[0]*b[1]//gcd(b[0], b[1])
    for i in range(2, n):
        lcm = lcm*b[i]//gcd(lcm, b[i])
    
    # print(f'lcm: {lcm}')
    
    all_odd = True
    for i in range(n):
        if lcm//b[i] % 2 == 0:
            all_odd = False
    # print(f'all_odd: {all_odd}')
    if all_odd:
        return m // lcm - m // (2*lcm)
    else:
        return 0


def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a=readinput()
    ans=solve(n,m,a)
    printans(ans)
