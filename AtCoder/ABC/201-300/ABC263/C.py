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
    n,m=m_input()
    return n,m

def solve(n,m):
    ans=[]
    for a in combinations(range(1, m+1), n):
        ans.append(a)
    return ans

def printans(ans):
    for a in ans:
        print(*a)

if __name__=='__main__':
    n,m=readinput()
    ans=solve(n,m)
    printans(ans)
