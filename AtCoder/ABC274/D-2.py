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
    def to1d(x, y):
        return str(x)+':'+str(y)
    def to2d(xy):
        # print(f'xy: {xy}')
        tmp = xy.split(':')
        x = int(tmp[0])
        y = int(tmp[1])
        # print(f'x: {x}, y: {y}')
        return (x, y)
    b = list(accumulate(a))
    dp = [set() for _ in range(n+1)]
    dp[n].add(to1d(x, y))
    for i in range(1, n)[::-1]:
        ai = a[i]
        bi = b[i-1]
        for xyj in dp[i+1]:
            xj, yj = to2d(xyj)
            if i % 2 == 0:
                dxy = [(-1, 0), (1,0)]
            else:
                dxy = [(0, -1), (0, 1)]
            for dx, dy in dxy:
                xi = xj + dx*ai
                yi = yj + dy*ai
                if abs(xi) + abs(yi) > bi:
                    continue
                dp[i].add(to1d(xi, yi))

    # print(f'dp: {dp}')

    if to1d(a[0], 0) in dp[1]:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,x,y,a=readinput()
    ans=solve(n,x,y,a)
    printans(ans)
