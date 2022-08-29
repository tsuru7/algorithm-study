import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from bisect import bisect_left, bisect_right
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
    a = a + a
    cum = [0] + list(accumulate(a))

    for head in range(1, n+1):
        wa = head-1
        ac = 2*n-1
        while ac - wa > 1:
            wj = (ac+wa)//2
            if (cum[wj] - cum[head-1])*10 >= whole:
                ac = wj
            else:
                wa = wj
        if (cum[ac] - cum[head-1])*10 == whole:
            return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=solve(n,a)
    printans(ans)
