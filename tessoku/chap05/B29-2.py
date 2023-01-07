import sys
sys.setrecursionlimit(10**6)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (1073741824//4, 1073741824//4))
INFTY = sys.maxsize

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

def fast_pow(x, k, P):
    re = 1
    while k:
        if k & 1:
            re = re * x % P
        x = x * x % P
        k >>= 1
    return re

def solve(a,b):
    MOD = 10**9 + 7
    return pow(a, b, MOD)

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b=readinput()
    ans=solve(a,b)
    printans(ans)
