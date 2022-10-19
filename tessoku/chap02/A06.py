import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import accumulate

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
    n,q=m_input()
    a=l_input()
    queries = [l_input() for _ in range(q)]
    return n,q,a,queries

def solve(n,q,a,queries):
    cum = [0] + list(accumulate(a))
    ans=[]
    for l, r in queries:
        ans.append(cum[r] - cum[l-1])
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,q,a,queries=readinput()
    ans=solve(n,q,a,queries)
    printans(ans)
