import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from heapq import heappush, heappop

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
    n,k,x=m_input()
    a=l_input()
    return n,k,x,a

def solve(n,k,x,a):
    a.sort(reverse=True)
    # print(f'k: {k}, x: {x}, a: {a}')
    for i in range(n):
        tmp = a[i]
        j = tmp//x
        j = min(j, k)
        tmp -= j*x
        k -= j
        a[i] = tmp
    a.sort(reverse=True)
    # print(f'k: {k}, x: {x}, a: {a}')
    return sum(a[k:])

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,x,a=readinput()
    ans=solve(n,k,x,a)
    printans(ans)
