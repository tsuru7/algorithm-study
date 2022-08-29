import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations

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
    p=l_input()
    q=l_input()
    return n,p,q

def solve(n,p,q):
    ans=0
    for c, x in enumerate(permutations(list(range(1,n+1)))):
        xl = list(x)
        if xl == p and xl == q:
            return 0
        elif xl == p or xl == q:
            ans = c - ans
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p,q=readinput()
    ans=solve(n,p,q)
    printans(ans)
