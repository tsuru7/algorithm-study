import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappush, heappop, heapify

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
    x,y,a,b,c=m_input()
    p = l_input()
    q = l_input()
    r = l_input()
    return x,y,a,b,c,p,q,r

def solve(x,y,a,b,c,p,q,r):
    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)
    heap = []
    delicious = 0
    for i in range(x):
        heappush(heap, p[i])
        delicious += p[i]
    for i in range(y):
        heappush(heap, q[i])
        delicious += q[i]
    ans = delicious
    for i in range(c):
        sute = heappop(heap)
        delicious -= sute
        heappush(heap, r[i])
        delicious += r[i]
        ans = max(ans, delicious)
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    x,y,a,b,c,p,q,r=readinput()
    ans=solve(x,y,a,b,c,p,q,r)
    printans(ans)
