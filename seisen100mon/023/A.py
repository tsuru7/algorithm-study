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
    p = []
    for _ in range(n):
        p.append(i_input())
    return n,m,p

def solve(n,m,p):
    p.append(0)
    p2 = []
    for v in p:
        for w in p:
            p2.append(v+w)
    p2.sort()
    ans = 0
    for i in range(len(p2)):
        x = m - p2[i]
        if x < 0:
            continue
        elif x == 0:
            return m
        # ac = -1
        # wa = len(p2)
        # while wa-ac > 1:
        #     wj = (ac+wa)//2
        #     if p2[wj] <= x:
        #         ac = wj
        #     else:
        #         wa = wj
        ac = bisect_right(p2, x)
        if ac == 0:
            continue
        ans = max(ans, p2[ac-1]+p2[i])
        
    return ans

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,p=readinput()
    ans=solve(n,m,p)
    printans(ans)
