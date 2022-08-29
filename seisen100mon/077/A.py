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
    n,m=m_input()
    s = [i_input() for _ in range(n-1)]
    a = [i_input() for _ in range(m)]
    return n,m,s,a

def solve(n,m,s,a):
    shukuba = [0] + list(accumulate(s))
    ans=0
    now = 0
    for ai in a:
        next = now+ai
        ans += abs(shukuba[next]-shukuba[now])
        now = next
    return ans % 100000

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,s,a=readinput()
    ans=solve(n,m,s,a)
    printans(ans)
