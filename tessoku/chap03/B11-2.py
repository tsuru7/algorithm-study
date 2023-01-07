import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right

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
    a = l_input()
    q = i_input()
    x = [i_input() for _ in range(q)]
    return n,a,q,x

def solve(n,a,q,x):
    a.sort()
    ans=[]
    for v in x:
        idx = bisect_left(a, v)
        ans.append(idx)
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a,q,x=readinput()
    ans=solve(n,a,q,x)
    printans(ans)
