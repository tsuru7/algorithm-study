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
    n=i_input()
    a=l_input()
    q = i_input()
    queries = [l_input() for _ in range(q)]
    return n,a,q,queries

def solve(n,a,q,queries):
    cum = [0] + list(accumulate(a))
    ans=[]
    for l, r in queries:
        total = r - l + 1
        atari = cum[r] - cum[l-1]
        hazure = total - atari
        if atari > hazure:
            ans.append('win')
        elif atari < hazure:
            ans.append('lose')
        else:
            ans.append('draw')
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,q,queries=readinput()
    ans=solve(n,a,q,queries)
    printans(ans)
