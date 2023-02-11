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
    n,p,q,r=m_input()
    a=l_input()
    return n,p,q,r,a

def main(n,p,q,r,a):
    cum = [0] + list(accumulate(a))
    cumset = set(cum)
    for x in range(n):
        if p + cum[x] not in cumset:
            continue
        y = bisect_left(cum, p+cum[x])
        if y >= len(cum) or q + cum[y] not in cumset:
            continue
        z = bisect_left(cum, q+cum[y])
        if z >= len(cum) or r + cum[z] not in cumset:
            continue
        return 'Yes'
    return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,p,q,r,a=readinput()
    ans=main(n,p,q,r,a)
    printans(ans)
