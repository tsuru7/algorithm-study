import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from collections import Counter

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
    counter = Counter(a)
    m = max(a)
    ans=0
    for q in range(1, m+1):
        for r in range(1, m//q+1):
            if r not in counter:
                continue
            p = q * r
            if p not in counter:
                continue
            ans += counter[p]*counter[q]*counter[r]

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
