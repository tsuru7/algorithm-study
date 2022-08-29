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
    n,m=m_input()
    a=l_input()
    b=l_input()
    return n,m,a,b

def main(n,m,a,b):
    a.sort()
    b.sort()
    ans=INFTY
    for ai in a:
        bi = bisect_left(b, ai) 
        if bi < len(b):
            ans = min(ans, abs(ai-b[bi]))
        if bi > 0:
            ans = min(ans, abs(ai - b[bi-1]))
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,a,b=readinput()
    ans=main(n,m,a,b)
    printans(ans)
