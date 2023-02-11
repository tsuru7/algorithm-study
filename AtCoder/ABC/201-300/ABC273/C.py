import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right
from collections import defaultdict

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
    b = list(set(a))
    b.sort()
    count=defaultdict(int)
    for i in range(n):
        ai = a[i]
        idx = bisect_right(b, ai)
        num_lt = len(b) - idx
        count[num_lt] += 1
    ans = [0 for _ in range(n)]
    for k, v in count.items():
        ans[k] = v
    return ans

def printans(ans):
    print(*ans, sep='\n')

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
