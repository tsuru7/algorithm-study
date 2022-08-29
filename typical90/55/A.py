import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import combinations

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
    n,p,q=m_input()
    a=l_input()
    return n,p,q,a

def solve(n,p,q,a):
    ans=0
    for com in combinations(range(n), 5):
        mul = 1
        for i in com:
            mul *= a[i]
            mul %= p
        if mul == q:
            ans += 1
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p,q,a=readinput()
    ans=solve(n,p,q,a)
    printans(ans)
