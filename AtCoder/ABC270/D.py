import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
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
    seta = set(a)
    b = []
    for i in range(k):
        ai = a[i]
        for j in range(k):
            aj = a[j]
            if ai + aj not in seta:
                b.append(ai+aj)
    setb = set(b)
    taka = True
    takahashi = 0
    aoki = 0
    x = n
    while x > 0:
        idx = bisect_right(a, x)
        if idx == len(a):
            idx -= 1
        if taka:
            takahashi += a[idx]
        else:
            aoki += a[idx]
        taka = not taka
        x -= a[idx]

    ans=takahashi
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,k,a=readinput()
    ans=solve(n,k,a)
    printans(ans)
