import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import permutations
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
    n=i_input()
    xylist = [ l_input() for _ in range(n) ]
    return n,xylist

def solve(n,xylist):
    ans=0
    count = 0
    for p in permutations(list(range(n))):
        dist = 0
        for i in range(n-1):
            j = p[i]
            k = p[i+1]
            x1, y1 = xylist[j]
            x2, y2 = xylist[k]
            dist += sqrt((x1-x2)**2+(y1-y2)**2)
        ans += dist
        count += 1
    ans /= count

    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,xylist=readinput()
    ans=solve(n,xylist)
    printans(ans)
