import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from math import sqrt

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
    xylist = [ l_input() for _ in range(n) ]
    return n,k,a,xylist

def solve(n,k,a,xylist):
    min_dist2_list = []
    for i in range(n):
        xi, yi = xylist[i]
        min_dist2 = INFTY
        for j in range(k):
            ak = a[j]-1
            xj, yj = xylist[ak]
            dist2 = (xi-xj)**2+(yi-yj)**2
            min_dist2 = min(min_dist2, dist2)
        min_dist2_list.append(min_dist2)
    ans = max(min_dist2_list)


    return sqrt(ans)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a,xylist=readinput()
    ans=solve(n,k,a,xylist)
    printans(ans)
