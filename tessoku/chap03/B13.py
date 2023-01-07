import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import accumulate
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
    n,k=m_input()
    a=l_input()
    return n,k,a

def solve(n,k,a):
    b = [0] + list(accumulate(a))
    ans=0
    for l in range(n+1):
        r = bisect_right(b, b[l]+k)-1
        ans += r - l
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
