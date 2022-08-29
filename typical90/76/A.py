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
    return n,a

def solve(n,a):
    whole = sum(a)
    a = a+a
    cum = [0] + list(accumulate(a))
    head = 1
    tail = 1
    while head <= n:
        while (cum[tail] - cum[head-1])*10 <= whole:
            if (cum[tail] - cum[head-1])*10 == whole:
                return 'Yes'
            tail += 1
        head += 1

    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
