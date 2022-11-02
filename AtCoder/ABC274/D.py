import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
from itertools import accumulate
from collections import defaultdict

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
    n,x,y=m_input()
    a=l_input()
    return n,x,y,a

def solve(n,x,y,a):
    b = list(accumulate(a))
    dp = [set() for _ in range(n+1)]
    dp[n].add((x, y))
    for i in range(1, n)[::-1]:
        ai = a[i]
        bi = b[i-1]
        for xj, yj in dp[i+1]:
            for dx, dy in [(-1, 0), (1,0), (0, -1), (0, 1)]:
                xi = xj + dx*ai
                yi = yj + dy*ai
                if abs(xi) + abs(yi) > bi:
                    continue
                dp[i].add((xi, yi))

    # print(f'dp: {dp}')

    if (a[0], 0) in dp[1]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y,a=readinput()
    ans=solve(n,x,y,a)
    printans(ans)
