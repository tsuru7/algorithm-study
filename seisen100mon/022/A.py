import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import log, exp, pow

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
    p = float(input())
    return p

def f(x, p):
    return x + p*pow(2.0, -x/1.5)

def fprime(x, p):
    return 1.0 - p*log(2.0)*pow(2.0, -x/1.5) / 1.5

def solve(p):
    if fprime(0, p) >= 0:
        return p
    
    tac = 0
    twa = p
    tdelta = 0.000000001
    while twa - tac > tdelta:
        twj = (tac+twa)/2
        if fprime(twj, p) < 0:
            tac = twj
        else:
            twa = twj
    ans=f(tac, p)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    p=readinput()
    ans=solve(p)
    printans(ans)
